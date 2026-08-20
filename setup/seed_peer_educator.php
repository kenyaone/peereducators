<?php
/**
 * Peer Educator — database build & seed
 *
 * Creates data/peereducator.db from sql/schema.sql, adds the
 * facilitator-shaped columns, and seeds the 19 modules of the national
 * "Adolescent and Young Persons Peer Education" curriculum.
 *
 * Safe to re-run: every statement is IF NOT EXISTS / INSERT OR IGNORE, and
 * it refuses to touch a database that already holds trainee records.
 *
 *   php setup/seed_peer_educator.php [--force]
 */

$root  = dirname(__DIR__);
$force = in_array('--force', $argv ?? [], true);

require_once $root . '/includes/config.php';

$dbPath = $root . '/data/peereducator.db';
if (!is_dir(dirname($dbPath))) mkdir(dirname($dbPath), 0775, true);

$fresh = !file_exists($dbPath);
$db = new SQLite3($dbPath);
$db->enableExceptions(true);
$db->busyTimeout(5000);
$db->exec('PRAGMA journal_mode=WAL');
$db->exec('PRAGMA foreign_keys=ON');

// ── Guard: never clobber a box that is already in service ──────────────
if (!$fresh && !$force) {
    $hasPeople = 0;
    try {
        $hasPeople = (int)$db->querySingle("SELECT COUNT(*) FROM students");
    } catch (Exception $e) { /* table not created yet */ }
    if ($hasPeople > 0) {
        fwrite(STDERR, "Refusing to seed: database already holds $hasPeople trainee records.\n");
        fwrite(STDERR, "Re-run with --force only if you intend to add missing modules in place.\n");
        exit(1);
    }
}

echo "Database: $dbPath" . ($fresh ? " (new)\n" : " (existing)\n");

// ── 1. Base schema ─────────────────────────────────────────────────────
$sql = file_get_contents($root . '/sql/schema.sql');
$db->exec('BEGIN');
foreach (array_filter(array_map('trim', explode(";\n", $sql))) as $stmt) {
    if ($stmt === '' || str_starts_with($stmt, '--')) continue;
    try { $db->exec($stmt); }
    catch (Exception $e) { fwrite(STDERR, "  schema warn: " . $e->getMessage() . "\n"); }
}
$db->exec('COMMIT');
echo "Base schema applied.\n";

// ── 2. Facilitator-shaped columns ──────────────────────────────────────
// The deck is a trainer curriculum: modules carry a national module code,
// a time allocation, learning objectives and closing key messages.
$add = [
    'modules' => [
        'module_code'         => "TEXT",
        'duration_minutes'    => "INTEGER DEFAULT 0",
        'learning_objectives' => "TEXT",   // JSON array
        'key_messages'        => "TEXT",   // JSON array
    ],
    'lessons' => [
        'duration_minutes'    => "INTEGER DEFAULT 0",
        'activity_type'       => "TEXT",   // illustration|demonstration|group_discussion|role_play
        'facilitator_notes'   => "TEXT",
    ],
];
foreach ($add as $table => $cols) {
    $have = [];
    $r = $db->query("PRAGMA table_info($table)");
    while ($row = $r->fetchArray(SQLITE3_ASSOC)) $have[] = $row['name'];
    foreach ($cols as $col => $decl) {
        if (!in_array($col, $have, true)) {
            $db->exec("ALTER TABLE $table ADD COLUMN $col $decl");
            echo "  + $table.$col\n";
        }
    }
}

// ── 3. The 19 modules of the national curriculum ───────────────────────
// Source: "Adolescent and Young Persons Peer Education — Updated slides"
// (336pp). The deck numbers 1–18 but splits 13 into 13A/13B, giving 19.
$modules = [
 ['M1','peer-education','Peer Education','🤝',60,
  'What peer education is, what a peer educator does, and the communication skills the role needs.',
  ['Explain the concept and roles of peer education',
   'Describe the qualities of an effective peer educator',
   'Apply communication skills for effective health education',
   'Select appropriate methods and tools for a peer session'],
  ['Peer education builds trust, empowers peers and reaches hard-to-reach groups.',
   'Peer educators are role models who share accurate information and link peers to services.',
   'Effective peer educators are confident, approachable, non-judgmental and keep confidentiality.',
   'Peer educators are usually volunteers.']],

 ['M2','adolescent-rights','Adolescent Rights','⚖️',60,
  'The national and international law protecting adolescents in Kenya, and what those rights mean day to day.',
  ['Define rights in the context of adolescents',
   'Identify the main laws and policies protecting adolescent rights in Kenya',
   'Explain key adolescent rights and what they mean in practice',
   'Recognise harmful practices that violate those rights'],
  ['Every adolescent holds rights that are protected by Kenyan and international law.',
   'Rights carry responsibilities toward yourself and others.',
   'Child marriage, FGM and hazardous work are violations, not traditions.',
   'Knowing where to report a violation is part of knowing your rights.']],

 ['M3','growth-and-development','Growth and Development','🌱',60,
  'Physical, emotional and social change through adolescence, and how to support peers through it.',
  ['Describe the stages of adolescent growth and development',
   'Explain the physical, emotional and social changes of puberty',
   'Distinguish normal variation from cause for concern',
   'Support peers who are anxious about the changes they are experiencing'],
  ['Puberty arrives at different ages for different people — there is no single normal.',
   'Physical change is matched by emotional and social change.',
   'Accurate information reduces the shame and fear around puberty.',
   'Adolescence is a period of opportunity, not just risk.']],

 ['M4','personal-hygiene','Personal Hygiene and Sanitation','🧼',45,
  'Everyday hygiene practice, and why it matters more during adolescence.',
  ['Explain the importance of personal hygiene during adolescence',
   'Demonstrate correct handwashing and daily hygiene routines',
   'Describe safe menstrual hygiene management',
   'Identify links between poor sanitation and common illness'],
  ['Hygiene needs increase during puberty as the body changes.',
   'Handwashing at critical moments prevents most common infections.',
   'Menstrual hygiene is a health and dignity issue, not a private embarrassment.',
   'Clean water, latrines and soap are rights, not luxuries.']],

 ['M5','life-skills','Life Skills','🧠',90,
  'The psychosocial skills that let young people handle pressure, decisions and conflict.',
  ['Define life skills and explain their value for adolescents',
   'Distinguish assertive, aggressive and passive communication',
   'Apply decision-making and problem-solving models',
   'Use refusal skills under peer pressure'],
  ['Life skills are learned through practice, not lectures.',
   'Assertive communication protects both the relationship and yourself.',
   'A structured decision keeps emotion from taking over.',
   'Saying no is a skill that improves with rehearsal.']],

 ['M6','nutrition','Nutrition','🥗',60,
  'What adolescent bodies need to grow, and the nutrition problems most common in young people.',
  ['Explain why good nutrition matters for adolescent growth and health',
   'Identify the main food groups and what the body uses them for',
   'Describe common nutrition problems among young people',
   'Apply practical healthy-eating choices at school and at home'],
  ['Adolescence is the second fastest growth period in life — nutrition demand peaks here.',
   'Macronutrients build the body; micronutrients run it.',
   'Good nutrition now lowers the risk of non-communicable disease later.',
   'Small, consistent choices beat occasional dramatic ones.']],

 ['M7','physical-activity','Physical Activity','🏃',60,
  'Movement as health, and how to lead inclusive activity sessions for peers.',
  ['Explain the benefits of physical activity for body and mind',
   'Demonstrate safe, age-appropriate activities including warm-up and cool-down',
   'Use inclusive approaches for peers of differing abilities',
   'Organise and sustain a peer-led activity session'],
  ['Physical activity improves mood and concentration, not just fitness.',
   'Warm-up and cool-down prevent most avoidable injuries.',
   'An inclusive session is one where the least confident peer still takes part.',
   'Consistency matters more than intensity.']],

 ['M8','non-communicable-diseases','Non-Communicable Diseases','🫀',105,
  'Diabetes, hypertension, sickle cell disease and breast and cervical cancer in young Kenyans.',
  ['Explain what diabetes, hypertension, sickle cell disease and breast and cervical cancer are',
   'Describe the risk factors for each',
   'Identify their signs and symptoms',
   'Explain prevention, control and common complications'],
  ['Non-communicable diseases cannot be caught from another person.',
   'They are rising among young Kenyans through diet, inactivity and substance use.',
   'Early detection changes the outcome for every one of them.',
   'Screening is not only for the old or the unwell.']],

 ['M9','mental-health','Mental Health','💚',90,
  'Mental wellbeing, common conditions, stigma, and how a peer educator responds.',
  ['Define mental health and mental illness',
   'Identify common mental health conditions among adolescents',
   'Recognise warning signs including suicidal thinking',
   'Respond supportively and refer to appropriate help'],
  ['Mental health is health — it is not weakness or a character flaw.',
   'Most adolescent mental health conditions are treatable when identified early.',
   'Listening without judgement is itself an intervention.',
   'Any mention of suicide is referred, never kept secret.']],

 ['M10','drug-substance-abuse','Drug and Substance Abuse','🚭',90,
  'Commonly abused substances in Kenya, their effects, and refusal and referral skills.',
  ['Identify substances commonly abused by young people in Kenya',
   'Explain the short and long term effects of substance use',
   'Describe the progression from experimentation to dependence',
   'Apply refusal skills and refer peers to treatment services'],
  ['Most dependence begins with experimentation during adolescence.',
   'Alcohol and tobacco are drugs, whatever their legal status.',
   'Dependence is a health condition, not a moral failure.',
   'NACADA (1192) offers free counselling and referral countrywide.']],

 ['M11','sexual-reproductive-health','Sexual Reproductive Health','🌺',90,
  'Reproductive anatomy, contraception, teenage pregnancy and informed choice.',
  ['Describe male and female reproductive anatomy and the menstrual cycle',
   'Explain how pregnancy occurs and how it is prevented',
   'Discuss teenage pregnancy, its causes and its consequences',
   'Identify youth-friendly SRH services and how to reach them'],
  ['Accurate anatomy knowledge is protective, not corrupting.',
   'Teenage pregnancy carries higher medical risk for both mother and baby.',
   'Every young person has the right to youth-friendly SRH services.',
   'Informed choice requires information first.']],

 ['M12','gender-based-violence','Gender Based Violence','🛡️',105,
  'Recognising GBV, supporting survivors, and the 72-hour window that changes outcomes.',
  ['Define gender-based violence and describe its forms',
   'Identify harmful practices including FGM and child marriage',
   'Explain the immediate steps after an assault, including the 72-hour window',
   'Support a survivor and refer to legal, medical and psychosocial services'],
  ['GBV is never the survivor\'s fault, whatever the circumstances.',
   'Care within 72 hours allows PEP and emergency contraception.',
   'Reporting is the survivor\'s decision — support it, do not force it.',
   'Confidentiality protects the survivor and your credibility.']],

 ['M13A','stis-hiv-early-adolescents','STIs, HIV and AHD — Ages 10 to 14','🎗️',60,
  'HIV and STI basics pitched for early adolescents, with an emphasis on facts over fear.',
  ['Explain what HIV and STIs are in age-appropriate terms',
   'Describe how HIV is and is not transmitted',
   'Explain why testing matters and where to get it',
   'Challenge the myths and stigma surrounding HIV'],
  ['HIV is not spread by sharing food, hugging or mosquito bites.',
   'A person living with HIV on treatment can live a full, healthy life.',
   'Testing is free, confidential and available to young people.',
   'Stigma harms more people than the virus does.']],

 ['M13B','stis-hiv-young-people','STIs, HIV and AHD — Ages 15 to 24','🎗️',105,
  'Prevention, testing, treatment and Advanced HIV Disease for older adolescents and youth.',
  ['Describe common STIs, their symptoms and their treatment',
   'Explain HIV prevention including condoms, PrEP and PEP',
   'Explain the 72-hour PEP window after possible exposure',
   'Define Advanced HIV Disease and explain why late diagnosis is dangerous'],
  ['Most STIs are curable; all are more manageable when treated early.',
   'PEP must start within 72 hours of exposure to work.',
   'Advanced HIV Disease is the result of late diagnosis, not inevitable progression.',
   'Undetectable means untransmittable.']],

 ['M14','tuberculosis','Tuberculosis','🫁',90,
  'How TB spreads, how it is found and treated, and how to break the stigma around it.',
  ['Explain what tuberculosis is and how it spreads',
   'Identify the signs and symptoms that require testing',
   'Describe TB treatment and why completing it matters',
   'Address the stigma attached to a TB diagnosis'],
  ['TB spreads through the air, not through touch, food or sharing utensils.',
   'A cough lasting more than two weeks should be tested.',
   'TB is curable, and treatment is free in Kenya.',
   'Supporting rather than judging someone with TB helps break the stigma.']],

 ['M15','accidents-and-emergencies','Accidents, Injuries and Emergencies','🚑',60,
  'Preventing common injuries and knowing how to get help fast when they happen.',
  ['Identify common types of accidents and injuries',
   'Explain the causes and risk factors in schools, homes and communities',
   'Demonstrate prevention strategies for different environments',
   'Recognise an emergency and summon timely help'],
  ['Most adolescent injuries are predictable and therefore preventable.',
   'Knowing the emergency number matters as much as knowing first aid.',
   'Do not move a seriously injured person unless they are in further danger.',
   'Calm, clear reporting gets help to the scene faster.']],

 ['M16','referral-and-linkage','Referral and Linkage','🔗',60,
  'The core peer educator competency — connecting a young person to the service they need and following through.',
  ['Explain what referral and linkage mean for adolescent services',
   'Identify when a referral is needed and what services exist',
   'Demonstrate supportive communication when making a referral',
   'Apply case scenarios to practise referral in a youth-friendly way'],
  ['A referral is a deliberate hand-off, not a phone number handed over.',
   'Linkage means following up until the service is actually received.',
   'Record every referral — undocumented referrals cannot be followed up.',
   'Re-refer or escalate when the first attempt does not land.']],

 ['M17','advocacy-and-sbcc','Advocacy and Social Behaviour Change Communication','📣',90,
  'Moving beyond one-to-one work to influencing behaviour and decisions at community level.',
  ['Define advocacy and social behaviour change communication',
   'Identify the audiences and channels that shape adolescent behaviour',
   'Develop a simple advocacy message for a chosen issue',
   'Plan a community-level SBCC activity'],
  ['Information alone rarely changes behaviour — context and motivation do.',
   'Advocacy targets decision-makers; SBCC targets the community.',
   'A message tested with the audience beats a message written for them.',
   'Change is measured in behaviour, not in sessions delivered.']],

 ['M18','monitoring-and-evaluation','Monitoring and Evaluation','📊',60,
  'Checking whether the work is actually helping young people, and reading your own data.',
  ['Explain the difference between monitoring and evaluation',
   'Identify the indicators that matter in adolescent health',
   'Record peer education activity accurately and consistently',
   'Read a dashboard and act on what it shows'],
  ['Monitoring watches what is happening; evaluation asks whether it helped.',
   'Data recorded badly is worse than no data — it misleads.',
   'M&E exists to improve the programme, not only to satisfy donors.',
   'Young people\'s voices belong in the evaluation, not just the numbers.']],
];

$ins = $db->prepare("INSERT OR IGNORE INTO modules
    (title, slug, description, icon, sort_order, is_active, module_code,
     duration_minutes, learning_objectives, key_messages, created_at)
    VALUES (:t,:s,:d,:i,:o,1,:c,:m,:lo,:km,CURRENT_TIMESTAMP)");

$n = 0;
foreach ($modules as $i => $m) {
    [$code,$slug,$title,$icon,$mins,$desc,$objs,$kms] = $m;
    $ins->reset();
    $ins->bindValue(':t',  $title);
    $ins->bindValue(':s',  $slug);
    $ins->bindValue(':d',  $desc);
    $ins->bindValue(':i',  $icon);
    $ins->bindValue(':o',  $i + 1, SQLITE3_INTEGER);
    $ins->bindValue(':c',  $code);
    $ins->bindValue(':m',  $mins, SQLITE3_INTEGER);
    $ins->bindValue(':lo', json_encode($objs, JSON_UNESCAPED_UNICODE));
    $ins->bindValue(':km', json_encode($kms,  JSON_UNESCAPED_UNICODE));
    $ins->execute();
    if ($db->changes() > 0) $n++;
}
echo "Modules seeded: $n new (" . count($modules) . " defined).\n";

// ── 4. Admin account (separate from ARISE by design) ───────────────────
$hasAdmin = (int)$db->querySingle("SELECT COUNT(*) FROM admin_users");
if ($hasAdmin === 0) {
    // admin/index.php authenticates with password_verify() against password_hash
    $st = $db->prepare("INSERT INTO admin_users
        (username, full_name, password_hash, role, is_active)
        VALUES ('admin', 'Peer Educator Admin', :p, 'superadmin', 1)");
    $st->bindValue(':p', password_hash('peer2026', PASSWORD_DEFAULT));
    $st->execute();
    echo "Admin created: admin / peer2026  (change it after first login)\n";
} else {
    echo "Admin already present ($hasAdmin) — left unchanged.\n";
}

$total = (int)$db->querySingle("SELECT COUNT(*) FROM modules");
echo "\nDone. Modules in database: $total\n";
$db->close();
