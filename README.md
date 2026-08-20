# Peer Educator

**Adolescent and Young Persons Peer Education** — a facilitator training platform
delivering the 19-module national peer-education curriculum, offline-first, in
English, Kiswahili and Sheng.

Built on the same architecture as ARISE (Apache + PHP + SQLite), but a separate
application with its own database, its own admin accounts and its own URL prefix.
ARISE serves learners at `/arise/`; this serves peer educators at `/peereducator/`.

## Architecture

```
/var/www/peereducator/            → http://<host>/peereducator/
├── public/     student-facing training site
├── admin/      admin panel (content, users, setup)
├── datapost/   courier interface for offline data sync
├── includes/   config.php — constants, DB, session isolation
├── data/       peereducator.db + uploaded lesson content
├── sql/        schema.sql (41 tables, full)
├── setup/      install, seed, lesson registration
└── tools/      lesson builder + trilingual lesson sources
```

## Install

```bash
sudo bash setup/install-peereducator.sh          # install / update in place
sudo bash setup/install-peereducator.sh --reset-db   # wipe and rebuild the DB
```

Non-destructive by default: it never touches `/var/www/arise`, and it preserves an
existing `peereducator.db` unless `--reset-db` is passed.

| URL | Purpose |
|-----|---------|
| `http://<host>/peereducator/` | Training site |
| `http://<host>/peereducator/admin/` | Admin panel |
| `http://<host>/peereducator/datapost/` | DataPost courier |

Default login `admin` / `peer2026` — **change it after first login.**

## Curriculum

19 modules from the national deck (numbered 1–18, with 13 split into 13A/13B),
totalling 24 hours. Each module carries its national `module_code`, a time
allocation, learning objectives and key messages.

## Authoring lessons

Lessons are content data, not hand-written HTML:

```bash
python3 tools/build_lesson.py tools/lessons/m01_peer_education.py
php setup/register_lessons.php
```

`tools/build_lesson.py` emits a standalone trilingual lesson matching the ARISE
lesson contract — `.en`/`.sw`/`.sh` spans, slide navigation, scenario pickers,
MCQ/MSQ scoring, and progress posted to `?p=api_lesson`. Add the new file to the
manifest in `setup/register_lessons.php` to link it to its module.

Every string exists three times. A lesson with unbalanced language spans is a bug.

## Scope boundary

The source curriculum contains full clinical dosing tables (PrEP regimens in
M13B). Peer educators are not prescribers — lessons name products and explain who
they are for, and route dosing and eligibility to the health facility. See the
"Where your role ends" slide in M13B part 2.

## Relationship to ARISE

Separate SQLite databases by design — SQLite is single-writer, so sharing one file
would put both apps on the same write lock. For cross-app reporting, attach the
other database rather than merging them:

```sql
ATTACH DATABASE '/var/www/arise/data/arise.db' AS arise;
SELECT s.name, COUNT(f.id) FROM arise.schools s LEFT JOIN facilitators f ...;
```

Sessions are isolated via `session_name('PEEREDUSESSID')` and a cookie path of
`/peereducator/`, set in `includes/config.php`. Without this, both apps would share
`PHPSESSID` on a common host and an ARISE admin login would be honoured here.

## Project by

- **World Possible Kenya** — worldpossiblekenya.org
- **M.T.T.I** — Masomotele Technical Training Institute
