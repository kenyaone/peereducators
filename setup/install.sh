#!/bin/bash
# ============================================
# Peer Educator + DataPost — CLEAN INSTALL
# Ubuntu 24.04 LTS
# Wipes everything and starts fresh
# ============================================

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo "========================================"
echo " Peer Educator — CLEAN INSTALL"
echo " Ubuntu 24.04 LTS"
echo "========================================"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Please run as root: sudo bash setup/install.sh${NC}"
    exit 1
fi

PEER_DIR="/var/www/peereducator"

# ============================================
# WARNING — WIPE CONFIRMATION
# ============================================
if [ -d "$PEER_DIR" ]; then
    echo -e "${RED}⚠️  WARNING: This will DELETE everything in $PEER_DIR${NC}"
    echo -e "${RED}   Including the database, student data, and all content!${NC}"
    echo ""
    read -p "   Type 'YES' to confirm clean install: " CONFIRM
    CONFIRM_UPPER=$(echo "$CONFIRM" | tr '[:lower:]' '[:upper:]')
    if [ "$CONFIRM_UPPER" != "YES" ]; then
        echo "   Aborted. Nothing was changed."
        exit 0
    fi
    echo ""
    echo -e "${YELLOW}[0/7] Backing up old database (just in case)...${NC}"
    if [ -f "$PEER_DIR/data/peereducator.db" ]; then
        BACKUP_NAME="peer_backup_before_clean_$(date +%Y%m%d_%H%M%S).db"
        cp "$PEER_DIR/data/peereducator.db" "/tmp/$BACKUP_NAME"
        echo "   Old database saved to /tmp/$BACKUP_NAME"
    fi
    echo -e "${RED}[0/7] Removing old installation...${NC}"
    rm -rf "$PEER_DIR"
fi

# ============================================
# 1. INSTALL DEPENDENCIES
# ============================================
echo -e "${GREEN}[1/7] Installing Apache, PHP, SQLite...${NC}"
apt update -y
apt install -y apache2 php php-sqlite3 php-json php-zip php-mbstring php-gd libapache2-mod-php sqlite3

a2enmod rewrite
a2enmod headers

# ============================================
# 1b. CONFIGURE PHP FOR LARGE UPLOADS
# ============================================
echo -e "${GREEN}[1b] Configuring PHP for video uploads...${NC}"

PHP_INI=$(php -i 2>/dev/null | grep "Loaded Configuration File" | awk '{print $NF}')
if [ -n "$PHP_INI" ] && [ -f "$PHP_INI" ]; then
    # Set in the main php.ini
    sed -i 's/upload_max_filesize = .*/upload_max_filesize = 500M/' "$PHP_INI"
    sed -i 's/post_max_size = .*/post_max_size = 512M/' "$PHP_INI"
    sed -i 's/max_execution_time = .*/max_execution_time = 300/' "$PHP_INI"
fi

# Also set via Apache for certainty
cat > /etc/php/*/apache2/conf.d/99-arise.ini << 'PHPINI'
upload_max_filesize = 500M
post_max_size = 512M
max_execution_time = 300
memory_limit = 256M
PHPINI

# ============================================
# 2. COPY FILES
# ============================================
echo -e "${GREEN}[2/7] Copying Peer Educator files...${NC}"

if [ -d "./public" ]; then
    mkdir -p "$PEER_DIR"
    cp -r . "$PEER_DIR/"
else
    echo -e "${RED}ERROR: Run this script from the Peer Educator project root directory${NC}"
    echo "   cd arise && sudo bash setup/install.sh"
    exit 1
fi

# ============================================
# 3. CREATE DIRECTORIES
# ============================================
echo -e "${GREEN}[3/7] Creating directory structure...${NC}"

mkdir -p "$PEER_DIR/data"
mkdir -p "$PEER_DIR/data/uploads"
mkdir -p "$PEER_DIR/data/uploads/logos"
mkdir -p "$PEER_DIR/data/datapost"
mkdir -p "$PEER_DIR/data/datapost/deliveries"
mkdir -p "$PEER_DIR/data/content"
mkdir -p "$PEER_DIR/data/content/updates"
mkdir -p "$PEER_DIR/data/backups"

# ============================================
# 4. SET PERMISSIONS
# ============================================
echo -e "${GREEN}[4/7] Setting permissions...${NC}"
chown -R www-data:www-data "$PEER_DIR"
chmod -R 755 "$PEER_DIR"
chmod -R 775 "$PEER_DIR/data"

# ============================================
# 5. CONFIGURE APACHE
# ============================================
echo -e "${GREEN}[5/7] Configuring Apache...${NC}"

cat > /etc/apache2/sites-available/arise.conf << 'APACHECONF'
<VirtualHost *:80>
    ServerName peereducator.local
    DocumentRoot /var/www/peereducator/public

    <Directory /var/www/peereducator/public>
        AllowOverride All
        Require all granted
        Options -Indexes +FollowSymLinks
    </Directory>

    # DataPost
    Alias /datapost /var/www/peereducator/datapost
    <Directory /var/www/peereducator/datapost>
        AllowOverride All
        Require all granted
    </Directory>

    # Admin
    Alias /admin /var/www/peereducator/admin
    <Directory /var/www/peereducator/admin>
        AllowOverride All
        Require all granted
    </Directory>

    # Logo files accessible publicly
    Alias /logos /var/www/peereducator/data/uploads/logos
    <Directory /var/www/peereducator/data/uploads/logos>
        Require all granted
        Options -Indexes
    </Directory>

    # Uploaded lesson files (videos, PDFs) accessible publicly
    Alias /uploads /var/www/peereducator/data/uploads
    <Directory /var/www/peereducator/data/uploads>
        Require all granted
        Options -Indexes
    </Directory>

    # Block everything else in data/ (DB, backups, datapost)
    <Directory /var/www/peereducator/data>
        Require all denied
    </Directory>

    # Re-allow uploads subdirectory (overrides above deny)
    <Directory /var/www/peereducator/data/uploads>
        Require all granted
    </Directory>

    # Block includes
    <Directory /var/www/peereducator/includes>
        Require all denied
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/peer_error.log
    CustomLog ${APACHE_LOG_DIR}/peer_access.log combined
</VirtualHost>
APACHECONF

a2dissite 000-default.conf 2>/dev/null || true
a2ensite arise.conf

# ============================================
# 6. INITIALIZE DATABASE
# ============================================
echo -e "${GREEN}[6/7] Initializing fresh database...${NC}"

php -r "
require_once '$PEER_DIR/includes/config.php';
initDatabase();
echo \"Database initialized with all tables and default modules.\n\";
"

chown www-data:www-data "$PEER_DIR/data/peereducator.db"
chmod 664 "$PEER_DIR/data/peereducator.db"

# ============================================
# 7. RESTART APACHE
# ============================================
echo -e "${GREEN}[7/7] Restarting Apache...${NC}"
systemctl restart apache2
systemctl enable apache2

# ============================================
# DONE
# ============================================
SERVER_IP=$(hostname -I | awk '{print $1}')

echo ""
echo "========================================"
echo -e "${GREEN} ✅ Peer Educator CLEAN INSTALL COMPLETE!${NC}"
echo "========================================"
echo ""
echo " 🌐 Student Site:  http://$SERVER_IP/"
echo " ⚙️  Admin Panel:   http://$SERVER_IP/admin/"
echo " 📡 DataPost:      http://$SERVER_IP/datapost/"
echo ""
echo -e "${YELLOW} 🔑 Default Login:${NC}"
echo "    Username: admin"
echo "    Password: peer2026"
echo ""
echo -e "${YELLOW} 📋 FIRST STEPS:${NC}"
echo "    1. Login to admin panel"
echo "    2. Go to Setup → configure school name & upload logo"
echo "    3. Go to Content → add lessons and quiz questions"
echo "    4. Go to Users → create teacher accounts"
echo "    5. Change the default password!"
echo ""
echo "========================================"
