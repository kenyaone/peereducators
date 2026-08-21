#!/bin/bash
# ============================================================
# Peer Educator — install / update
#
# Installs the Peer Educator app to /var/www/peereducator and serves it
# at http://<server-ip>/peereducator/ , alongside ARISE at /arise/.
#
# Non-destructive: it never touches /var/www/arise, and it will not
# overwrite an existing peereducator.db unless you pass --reset-db.
# ============================================================

set -euo pipefail

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

APP_DIR="/var/www/peereducator"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RESET_DB=0
[[ "${1:-}" == "--reset-db" ]] && RESET_DB=1

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Must run as root:  sudo bash $0${NC}"; exit 1
fi
if [ ! -f "$SRC_DIR/includes/config.php" ]; then
    echo -e "${RED}ERROR: run this from the Peer Educator build directory.${NC}"; exit 1
fi

echo ""
echo "=============================================="
echo " PEER EDUCATOR — INSTALL"
echo " source: $SRC_DIR"
echo " target: $APP_DIR"
echo "=============================================="
echo ""

# ── 1. Dependencies (already present if ARISE is running) ───────────
echo -e "${GREEN}[1/6] Checking dependencies...${NC}"
MISSING=""
command -v php >/dev/null 2>&1 || MISSING="$MISSING php libapache2-mod-php"
php -m 2>/dev/null | grep -qi '^sqlite3$' || MISSING="$MISSING php-sqlite3"
command -v apache2 >/dev/null 2>&1 || MISSING="$MISSING apache2"
if [ -n "$MISSING" ]; then
    echo "      installing:$MISSING"
    export DEBIAN_FRONTEND=noninteractive
    apt-get update -y
    apt-get install -y --no-install-recommends $MISSING
else
    echo "      php $(php -r 'echo PHP_VERSION;') + sqlite3 present"
fi
a2enmod rewrite headers >/dev/null 2>&1 || true

# ── 2. Preserve existing data, then sync code ───────────────────────
echo -e "${GREEN}[2/6] Installing application files...${NC}"
KEEP_DB=""
if [ -f "$APP_DIR/data/peereducator.db" ] && [ "$RESET_DB" -eq 0 ]; then
    KEEP_DB="$(mktemp -d)/peereducator.db"
    cp -a "$APP_DIR/data/peereducator.db" "$KEEP_DB"
    echo -e "${YELLOW}      existing database preserved${NC}"
elif [ -f "$APP_DIR/data/peereducator.db" ] && [ "$RESET_DB" -eq 1 ]; then
    BK="/var/backups/peereducator"; mkdir -p "$BK"
    cp -a "$APP_DIR/data/peereducator.db" "$BK/peereducator.db.$(date +%Y%m%d_%H%M%S)"
    echo -e "${YELLOW}      --reset-db: old database backed up to $BK${NC}"
fi

mkdir -p "$APP_DIR"
# code only; data/ is handled separately so uploads survive an update
for d in public admin datapost includes setup sql deploy cloud; do
    [ -d "$SRC_DIR/$d" ] && { rm -rf "${APP_DIR:?}/$d"; cp -r "$SRC_DIR/$d" "$APP_DIR/"; }
done
[ -f "$SRC_DIR/.htaccess" ] && cp "$SRC_DIR/.htaccess" "$APP_DIR/"

mkdir -p "$APP_DIR"/data/{uploads/{interactive,logos,pdfs,thumbnails,media},datapost/deliveries,content/updates,backups}
# ship seeded lesson content without clobbering uploads added on the box
if [ -d "$SRC_DIR/data/uploads/interactive" ]; then
    cp -rn "$SRC_DIR/data/uploads/interactive/." "$APP_DIR/data/uploads/interactive/" 2>/dev/null || true
fi
[ -n "$KEEP_DB" ] && cp -a "$KEEP_DB" "$APP_DIR/data/peereducator.db"

# ── 3. Apache — mount at /peereducator/ ─────────────────────────────
echo -e "${GREEN}[3/6] Configuring Apache...${NC}"
cat > /etc/apache2/conf-available/peereducator.conf << 'APACHECONF'
# Peer Educator — served under /peereducator/ , alongside ARISE at /arise/.
# The app uses absolute /peereducator/... links and each .htaccess sets
# "RewriteBase /peereducator/", so this prefix is required.

# Most specific aliases first — Apache takes the first match.
Alias /peereducator/data/uploads /var/www/peereducator/data/uploads
Alias /peereducator/uploads      /var/www/peereducator/data/uploads
Alias /peereducator/admin        /var/www/peereducator/admin
Alias /peereducator/datapost     /var/www/peereducator/datapost
Alias /peereducator              /var/www/peereducator/public

<Directory /var/www/peereducator/public>
    AllowOverride All
    Require all granted
    Options -Indexes +FollowSymLinks
    DirectoryIndex index.php index.html
</Directory>

<Directory /var/www/peereducator/admin>
    AllowOverride All
    Require all granted
    Options -Indexes +FollowSymLinks
    DirectoryIndex index.php
</Directory>

<Directory /var/www/peereducator/datapost>
    AllowOverride All
    Require all granted
    Options -Indexes +FollowSymLinks
    DirectoryIndex index.php
</Directory>

# Deny the data tree (holds the database and backups)...
<Directory /var/www/peereducator/data>
    Require all denied
</Directory>

# ...then re-allow only uploaded lesson media.
<Directory /var/www/peereducator/data/uploads>
    Require all granted
    Options -Indexes +FollowSymLinks
</Directory>

<Directory /var/www/peereducator/includes>
    Require all denied
</Directory>
APACHECONF
a2enconf peereducator >/dev/null

# ── 4. Permissions ──────────────────────────────────────────────────
echo -e "${GREEN}[4/6] Setting permissions...${NC}"
chown -R www-data:www-data "$APP_DIR"
find "$APP_DIR" -type d -exec chmod 755 {} \;
find "$APP_DIR" -type f -exec chmod 644 {} \;
chmod -R 775 "$APP_DIR/data"
# SQLite WAL needs to create -wal/-shm beside the database, so the
# directory itself must be group-writable, not just the file.
chmod 775 "$APP_DIR/data"

# ── 5. Database ─────────────────────────────────────────────────────
echo -e "${GREEN}[5/6] Building database...${NC}"
if [ ! -f "$APP_DIR/data/peereducator.db" ]; then
    sudo -u www-data php "$APP_DIR/setup/seed_peer_educator.php"
else
    echo "      database exists — adding any missing modules"
    sudo -u www-data php "$APP_DIR/setup/seed_peer_educator.php" --force || true
fi

# Link the lesson HTML files to their modules. Without this the site installs
# cleanly, reports 19 modules, and shows no lessons at all.
echo -e "${GREEN}      linking lessons...${NC}"
sudo -u www-data php "$APP_DIR/setup/register_lessons.php"
chown www-data:www-data "$APP_DIR/data/peereducator.db"
chmod 664 "$APP_DIR/data/peereducator.db"

# ── 6. Reload ───────────────────────────────────────────────────────
echo -e "${GREEN}[6/6] Validating and reloading Apache...${NC}"
apache2ctl configtest
systemctl reload apache2 || systemctl restart apache2

IP="$(hostname -I | awk '{print $1}')"
echo ""
echo "=============================================="
echo -e "${GREEN} PEER EDUCATOR INSTALLED${NC}"
echo "=============================================="
echo ""
echo "  Training site :  http://${IP}/peereducator/"
echo "  Admin panel   :  http://${IP}/peereducator/admin/"
echo "  DataPost      :  http://${IP}/peereducator/datapost/"
echo ""
echo -e "${YELLOW}  Login: admin / peer2026  — change this after first login${NC}"
echo ""
echo "  ARISE is untouched at http://${IP}/arise/"
echo ""
