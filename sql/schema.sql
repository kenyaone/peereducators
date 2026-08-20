-- Peer Educator — base schema
-- Structure derived from the live ARISE database so every column the
-- forked PHP expects exists. NO ARISE DATA is carried over.
-- Generated for: Adolescent and Young Persons Peer Education

CREATE TABLE IF NOT EXISTS admin_permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    permission TEXT NOT NULL,
    UNIQUE(user_id, permission),
    FOREIGN KEY (user_id) REFERENCES admin_users(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    full_name TEXT,
    password_hash TEXT NOT NULL,
    role TEXT DEFAULT 'teacher',
    is_active INTEGER DEFAULT 1,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
, deleted_at DATETIME);
CREATE TABLE IF NOT EXISTS anonymous_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    module_id INTEGER,
    is_answered INTEGER DEFAULT 0,
    answer TEXT,
    answered_by INTEGER,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    answered_at DATETIME
, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, notified INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS arise_audit_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_id INTEGER,
    admin_name TEXT,
    action TEXT NOT NULL,
    target_type TEXT,
    target_id INTEGER,
    details TEXT,
    ip_address TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS backup_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    backup_type TEXT NOT NULL,
    filename TEXT NOT NULL,
    file_size_kb REAL,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS badges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    icon TEXT DEFAULT '?',
    xp_reward INTEGER DEFAULT 50,
    condition_type TEXT,
    condition_value INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS behavioral_surveys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    session_hash TEXT NOT NULL,
    module_id INTEGER NOT NULL,
    q1_changed INTEGER DEFAULT 0,
    q1_detail TEXT,
    q2_shared INTEGER DEFAULT 0,
    q2_detail TEXT,
    q3_confident INTEGER DEFAULT 0,
    q3_detail TEXT,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
, q4_pregnancy INTEGER DEFAULT NULL);
CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cert_number TEXT UNIQUE NOT NULL,
    student_id INTEGER,
    student_name TEXT NOT NULL,
    module_id INTEGER NOT NULL,
    module_title TEXT NOT NULL,
    score INTEGER NOT NULL,
    percentage REAL NOT NULL,
    issued_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (module_id) REFERENCES modules(id)
);
CREATE TABLE IF NOT EXISTS challenge_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    challenge_id INTEGER NOT NULL,
    student_id INTEGER,
    session_hash TEXT NOT NULL,
    student_name TEXT,
    response_text TEXT NOT NULL,
    word_count INTEGER DEFAULT 0,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    level TEXT,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (school_id) REFERENCES schools(id)
);
CREATE TABLE IF NOT EXISTS clusters (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
, lat REAL DEFAULT NULL, lng REAL DEFAULT NULL);
CREATE TABLE IF NOT EXISTS daily_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stat_date DATE UNIQUE NOT NULL,
    unique_devices INTEGER DEFAULT 0,
    total_sessions INTEGER DEFAULT 0,
    total_page_views INTEGER DEFAULT 0,
    total_quiz_attempts INTEGER DEFAULT 0,
    total_questions_asked INTEGER DEFAULT 0
);
CREATE TABLE IF NOT EXISTS datapost_config (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_id TEXT UNIQUE NOT NULL,
    school_name TEXT NOT NULL,
    county TEXT,
    sub_county TEXT,
    contact_person TEXT,
    contact_phone TEXT,
    auto_backup_enabled INTEGER DEFAULT 1,
    auto_backup_path TEXT DEFAULT '/var/www/arise/data/backups/',
    setup_date DATETIME DEFAULT CURRENT_TIMESTAMP
, email_endpoint TEXT DEFAULT '', webhook_url TEXT DEFAULT '', smtp_host TEXT DEFAULT 'smtp.gmail.com', smtp_port INTEGER DEFAULT 587, smtp_user TEXT DEFAULT '', smtp_pass TEXT DEFAULT '', smtp_from TEXT DEFAULT '', cloud_sync_url TEXT DEFAULT 'https://ariseci.org/arise-sync.php', cloud_last_synced_at TEXT DEFAULT NULL, cloud_last_sync_count INTEGER DEFAULT 0);
CREATE TABLE IF NOT EXISTS datapost_deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    courier_email TEXT NOT NULL,
    courier_name TEXT,
    delivery_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    package_name TEXT,
    package_size_kb INTEGER,
    notes TEXT
);
CREATE TABLE IF NOT EXISTS datapost_pickups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    courier_email TEXT NOT NULL,
    courier_name TEXT,
    pickup_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_from DATE NOT NULL,
    data_to DATE NOT NULL,
    bundle_size_kb INTEGER,
    bundle_hash TEXT
);
CREATE TABLE IF NOT EXISTS datapost_sync_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sync_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_snapshot TEXT,
    posted_at DATETIME
);
CREATE TABLE IF NOT EXISTS essay_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    session_hash TEXT NOT NULL,
    question_id INTEGER NOT NULL,
    module_id INTEGER NOT NULL,
    response_text TEXT NOT NULL,
    word_count INTEGER DEFAULT 0,
    is_graded INTEGER DEFAULT 0,
    grade INTEGER,
    feedback TEXT,
    graded_by INTEGER,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    graded_at DATETIME, notified INTEGER DEFAULT 0,
    FOREIGN KEY (question_id) REFERENCES quiz_questions(id),
    FOREIGN KEY (module_id) REFERENCES modules(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
CREATE TABLE IF NOT EXISTS facilitator_sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    facilitator_id INTEGER NOT NULL,
    cluster_name TEXT,
    school_name TEXT,
    session_code TEXT UNIQUE NOT NULL,
    is_active INTEGER DEFAULT 1,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    ended_at DATETIME
);
CREATE TABLE IF NOT EXISTS forum_posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER DEFAULT NULL,
    student_id INTEGER,
    student_name TEXT NOT NULL,
    module_id INTEGER,
    title TEXT,
    body TEXT NOT NULL,
    is_pinned INTEGER DEFAULT 0,
    is_hidden INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS forum_upvotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    session_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(post_id, session_hash)
);
CREATE TABLE IF NOT EXISTS lesson_interactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_hash TEXT NOT NULL,
    student_id INTEGER,
    module_id INTEGER NOT NULL,
    lesson_slug TEXT,
    interaction_type TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    done INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS lesson_progress (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, lesson_id INTEGER NOT NULL, last_slide INTEGER DEFAULT 0, completed INTEGER DEFAULT 0, completed_at DATETIME, session_hash TEXT, UNIQUE(student_id, lesson_id));
CREATE TABLE IF NOT EXISTS lesson_scores (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER NOT NULL, lesson_slug TEXT NOT NULL, module_slug TEXT NOT NULL, score INTEGER NOT NULL, total INTEGER NOT NULL, percent REAL NOT NULL, passed INTEGER DEFAULT 0, saved_at DATETIME DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE IF NOT EXISTS lesson_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_id INTEGER NOT NULL,
    title TEXT,
    content TEXT,
    saved_by INTEGER,
    saved_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    content TEXT,
    lesson_type TEXT DEFAULT 'text',
    file_path TEXT,
    file_name TEXT,
    file_size_kb REAL,
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, video_path TEXT, pdf_path TEXT, pdf_name TEXT, thumbnail TEXT, is_published INTEGER DEFAULT 0,
    FOREIGN KEY (module_id) REFERENCES modules(id)
);
CREATE TABLE IF NOT EXISTS module_feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    session_hash TEXT NOT NULL,
    student_id INTEGER,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    most_useful TEXT,
    unclear TEXT,
    would_recommend INTEGER DEFAULT 1,
    submitted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS modules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    description TEXT,
    icon TEXT DEFAULT '📚',
    sort_order INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
, thumbnail TEXT, content_warning TEXT, school_id TEXT, require_pretest INTEGER DEFAULT 1, require_posttest INTEGER DEFAULT 1);
CREATE TABLE IF NOT EXISTS page_views (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_hash TEXT NOT NULL,
    student_id INTEGER,
    page_type TEXT NOT NULL,
    page_slug TEXT,
    module_id INTEGER,
    viewed_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS pretest_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    session_hash TEXT NOT NULL,
    module_id INTEGER NOT NULL,
    test_type TEXT DEFAULT 'pre',
    score INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    percentage REAL DEFAULT 0,
    taken_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS quiz_answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attempt_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    chosen_option TEXT,
    is_correct INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_hash TEXT NOT NULL,
    student_id INTEGER,
    module_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    percentage REAL NOT NULL,
    completed_at DATETIME DEFAULT CURRENT_TIMESTAMP, test_type TEXT DEFAULT 'quiz', lesson_slug TEXT,
    FOREIGN KEY (module_id) REFERENCES modules(id),
    FOREIGN KEY (student_id) REFERENCES students(id)
);
CREATE TABLE IF NOT EXISTS quiz_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    module_id INTEGER NOT NULL,
    question_type TEXT DEFAULT 'mcq',
    question TEXT NOT NULL,
    option_a TEXT,
    option_b TEXT,
    option_c TEXT,
    option_d TEXT,
    correct_option TEXT,
    explanation TEXT,
    essay_hint TEXT,
    min_words INTEGER DEFAULT 0,
    max_marks INTEGER DEFAULT 1,
    sort_order INTEGER DEFAULT 0, competency TEXT, difficulty TEXT DEFAULT 'MEDIUM', is_published INTEGER DEFAULT 0, option_e TEXT DEFAULT '', section TEXT DEFAULT 'lesson',
    FOREIGN KEY (module_id) REFERENCES modules(id)
);
CREATE TABLE IF NOT EXISTS quiz_retry_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_hash TEXT NOT NULL,
    module_id INTEGER NOT NULL,
    last_attempt DATETIME DEFAULT CURRENT_TIMESTAMP,
    attempt_count INTEGER DEFAULT 1
);
CREATE TABLE IF NOT EXISTS retention_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    session_hash TEXT NOT NULL,
    module_id INTEGER NOT NULL,
    score INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    percentage REAL DEFAULT 0,
    taken_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    county TEXT,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
, lat REAL DEFAULT NULL, lng REAL DEFAULT NULL, cluster_id INTEGER REFERENCES clusters(id), password_hash TEXT DEFAULT NULL);
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_hash TEXT UNIQUE NOT NULL,
    student_id INTEGER,
    device_hash TEXT NOT NULL,
    started_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_active DATETIME DEFAULT CURRENT_TIMESTAMP,
    language TEXT DEFAULT 'en', last_seen DATETIME,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
CREATE TABLE IF NOT EXISTS student_badges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    badge_id INTEGER NOT NULL,
    earned_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(student_id, badge_id)
);
CREATE TABLE IF NOT EXISTS student_xp (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL UNIQUE,
    xp_points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    streak_days INTEGER DEFAULT 0,
    last_activity DATE,
    total_lessons_completed INTEGER DEFAULT 0,
    total_quizzes_passed INTEGER DEFAULT 0,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    school_name TEXT,
    class_name TEXT,
    session_hash TEXT,
    is_active INTEGER DEFAULT 1,
    registered_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
, language_pref TEXT DEFAULT 'en', streak_days INTEGER DEFAULT 0, last_streak_date TEXT, text_size TEXT DEFAULT 'md', total_certs INTEGER DEFAULT 0, notifications TEXT DEFAULT '[]', password_hash TEXT, deleted_at DATETIME);
CREATE TABLE IF NOT EXISTS weekly_challenges (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    module_id INTEGER,
    week_start DATE NOT NULL,
    week_end DATE NOT NULL,
    is_active INTEGER DEFAULT 1,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS xp_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    action TEXT NOT NULL,
    xp_earned INTEGER NOT NULL,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_li_session_module ON lesson_interactions(session_hash, module_id, interaction_type);
CREATE UNIQUE INDEX IF NOT EXISTS uniq_feedback ON module_feedback(module_id, session_hash);
