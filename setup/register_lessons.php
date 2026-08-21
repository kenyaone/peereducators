<?php
/**
 * Peer Educator — register built lesson files into the lessons table.
 *
 * The builder (tools/build_lesson.py) writes standalone HTML into
 * data/uploads/interactive/. This links each file to its module so the app
 * serves it. Re-runnable: updates the row if the slug already exists.
 *
 *   php setup/register_lessons.php
 */

$root = dirname(__DIR__);
require_once $root . '/includes/config.php';

$dir = $root . '/data/uploads/interactive/';
$db  = new SQLite3($root . '/data/peereducator.db');
$db->enableExceptions(true);
$db->busyTimeout(5000);

// file  =>  [module_code, title, sort_order, duration, activity_type]
$LESSONS = [
    'm01-peer-education.html'       => ['M1',  'Peer Education',       1, 60, 'group_discussion'],
    'm08a-diabetes-hypertension-sickle-cell.html'
                                    => ['M8',  'Diabetes, Hypertension and Sickle Cell', 1, 60, 'group_discussion'],
    'm08b-breast-and-cervical-cancer.html'
                                    => ['M8',  'Breast and Cervical Cancer',             2, 45, 'demonstration'],
    'm04-personal-hygiene.html'     => ['M4',  'Personal Hygiene and Sanitation',        1, 45, 'demonstration'],
    'm05a-skills-for-yourself.html' => ['M5',  'Life Skills — Skills for Yourself',   1, 45, 'group_discussion'],
    'm05b-skills-with-others.html'  => ['M5',  'Life Skills — Others and Decisions',  2, 45, 'role_play'],
    'm06-nutrition.html'            => ['M6',  'Nutrition',                              1, 60, 'group_discussion'],
    'm07-physical-activity.html'    => ['M7',  'Physical Activity',                      1, 60, 'demonstration'],
    'm09a-mental-health-and-stress.html'
                                    => ['M9',  'Mental Health, Stress and Common Conditions',   1, 45, 'group_discussion'],
    'm09b-suicide-pressures-and-help.html'
                                    => ['M9',  'Suicide Risk, Modern Pressures and Getting Help',2, 45, 'role_play'],
    'm10a-understanding-drug-abuse.html'
                                    => ['M10', 'Understanding Drug and Substance Abuse',     1, 45, 'group_discussion'],
    'm10b-recognising-and-responding.html'
                                    => ['M10', 'Recognising Substance Abuse and Responding', 2, 45, 'role_play'],
    'm12a-understanding-gbv.html'   => ['M12', 'Understanding Gender Based Violence',      1, 45, 'group_discussion'],
    'm12b-responding-to-gbv.html'   => ['M12', 'Responding to GBV and Harmful Practices',  2, 60, 'role_play'],
    'm13b1-stis-and-condoms.html'   => ['M13B','STIs and Condoms',                        1, 45, 'demonstration'],
    'm13b2-hiv-prep-pep-ahd.html'   => ['M13B','HIV, PrEP, PEP and Advanced HIV Disease', 2, 60, 'role_play'],
    'm15-accidents-and-emergencies.html'
                                    => ['M15', 'Accidents, Injuries and Emergencies',    1, 60, 'role_play'],
    'm16-referral-and-linkage.html' => ['M16', 'Referral and Linkage', 1, 60, 'role_play'],
];

$linked = $skipped = 0;
foreach ($LESSONS as $file => [$code, $title, $order, $mins, $activity]) {
    $path = $dir . $file;
    if (!file_exists($path)) {
        echo "  SKIP  $file (not built yet)\n";
        $skipped++;
        continue;
    }

    $mod = $db->querySingle(
        "SELECT id, slug FROM modules WHERE module_code='" . SQLite3::escapeString($code) . "'", true);
    if (!$mod) {
        echo "  SKIP  $file (module $code not in database)\n";
        $skipped++;
        continue;
    }

    $slug = pathinfo($file, PATHINFO_FILENAME);
    $kb   = (int)round(filesize($path) / 1024);
    $exists = $db->querySingle(
        "SELECT id FROM lessons WHERE slug='" . SQLite3::escapeString($slug) . "'");

    if ($exists) {
        $st = $db->prepare("UPDATE lessons SET module_id=:m, title=:t, file_path=:f, file_name=:n,
                            file_size_kb=:k, sort_order=:o, lesson_type='interactive', is_active=1,
                            is_published=1, duration_minutes=:d, activity_type=:a WHERE id=:id");
        $st->bindValue(':id', $exists, SQLITE3_INTEGER);
    } else {
        $st = $db->prepare("INSERT INTO lessons
            (module_id, title, slug, lesson_type, file_path, file_name, file_size_kb,
             sort_order, is_active, is_published, duration_minutes, activity_type, created_at)
            VALUES (:m,:t,:s,'interactive',:f,:n,:k,:o,1,1,:d,:a,CURRENT_TIMESTAMP)");
        $st->bindValue(':s', $slug);
    }
    $st->bindValue(':m', $mod['id'], SQLITE3_INTEGER);
    $st->bindValue(':t', $title);
    // file_path is relative to UPLOAD_PATH — matches how ARISE stores it
    $st->bindValue(':f', 'interactive/' . $file);
    $st->bindValue(':n', $file);
    $st->bindValue(':k', $kb, SQLITE3_INTEGER);
    $st->bindValue(':o', $order, SQLITE3_INTEGER);
    $st->bindValue(':d', $mins, SQLITE3_INTEGER);
    $st->bindValue(':a', $activity);
    $st->execute();

    printf("  %-6s %-34s -> %s (%d KB)\n", $exists ? 'UPDATE' : 'LINK', $file, $mod['slug'], $kb);
    $linked++;
}

$total   = (int)$db->querySingle("SELECT COUNT(*) FROM lessons WHERE is_active=1");
$modules = (int)$db->querySingle("SELECT COUNT(*) FROM modules");
$withLesson = (int)$db->querySingle(
    "SELECT COUNT(DISTINCT module_id) FROM lessons WHERE is_active=1");

echo "\nLinked $linked, skipped $skipped.\n";
echo "Lessons live: $total | Modules with content: $withLesson / $modules\n";
$db->close();
