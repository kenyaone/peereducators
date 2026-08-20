# Module 8 (part 2 of 2) — Breast and Cervical Cancer
# Source: "Adolescent and Young Persons Peer Education — Updated slides", Module 8.
# Trilingual: English / Kiswahili / Sheng.

LESSON = {
 "file": "m08b-breast-and-cervical-cancer.html",
 "module_code": "M8",
 "module_slug": "non-communicable-diseases",
 "lesson_slug": "m08b-breast-and-cervical-cancer",
 "module_label": "Peer Educator · M8 · Part 2 of 2",
 "title": "Breast and Cervical Cancer",
 "icon": "🎀",
 "duration": 45,

 "objectives": [
  ("Explain what cancer is and name the cancers most common in Kenya",
   "Eleza saratani ni nini na utaje saratani zilizo za kawaida zaidi Kenya",
   "Explain cancer ni nini na uname cancers common zaidi Kenya"),
  ("Describe the risk factors and warning signs of breast cancer",
   "Eleza sababu za hatari na dalili za onyo za saratani ya matiti",
   "Describe risk factors na warning signs za breast cancer"),
  ("Demonstrate the five steps of breast self-examination",
   "Onyesha hatua tano za kujichunguza matiti",
   "Onyesha steps tano za breast self-examination"),
  ("Explain how cervical cancer is caused, screened for and prevented in Kenya",
   "Eleza jinsi saratani ya shingo ya kizazi inavyosababishwa, kupimwa na kuzuiwa Kenya",
   "Explain jinsi cervical cancer inavyosababishwa, kupimwa na ku-preventiwa Kenya"),
 ],

 "big_question": (
  "<strong>🔍 Big Question:</strong> Nine women die of cervical cancer in Kenya every day, and there is a free vaccine that prevents it. Why is that still happening?",
  "<strong>🔍 Swali Kubwa:</strong> Wanawake tisa hufa kwa saratani ya shingo ya kizazi Kenya kila siku, na kuna chanjo ya bure inayoizuia. Kwa nini hilo bado linatokea?",
  "<strong>🔍 Big Question:</strong> Wanawake tisa wanakufa kwa cervical cancer Kenya kila siku, na kuna free vaccine inayoi-prevent. Kwa nini hiyo bado inahappen?"),

 "slides": [

  # ── 1. What cancer is ─────────────────────────────────────────────
  {"icon": "📖",
   "head": ("What Cancer Actually Is", "Saratani Ni Nini Hasa", "Cancer Ni Nini Hasa"),
   "blocks": [
    {"type": "key_term", "term": ("🔑 Cancer", "🔑 Saratani", "🔑 Cancer"), "text": (
     "A group of diseases in which some body cells become abnormal, grow uncontrollably, spread beyond their usual boundaries and invade other parts of the body.",
     "Kundi la magonjwa ambapo baadhi ya seli za mwili huwa zisizo za kawaida, hukua bila kudhibitiwa, huenea zaidi ya mipaka yake na kuvamia sehemu nyingine za mwili.",
     "Group ya magonjwa ambapo baadhi ya body cells zinakuwa abnormal, zinakua bila control, zinaspread beyond boundaries zake na ku-invade sehemu zingine za mwili.")},
    {"type": "p", "text": (
     "There are more than 200 types. Some grow and spread fast, others slowly. The commonest in Kenya are breast, cervix, prostate, oesophagus and colorectal.",
     "Kuna aina zaidi ya 200. Zingine hukua na kuenea haraka, zingine polepole. Za kawaida zaidi Kenya ni ya matiti, shingo ya kizazi, tezi dume, umio na utumbo mpana.",
     "Kuna types zaidi ya 200. Zingine zinakua na ku-spread fast, zingine polepole. Common zaidi Kenya ni breast, cervix, prostate, oesophagus na colorectal.")},
    {"type": "warn", "title": ("⚠️ The hardest fact to teach", "⚠️ Ukweli mgumu zaidi kufundisha", "⚠️ Fact ngumu zaidi kufundisha"), "text": (
     " At early stages <strong>most cancers have no symptoms at all</strong>. Waiting to feel unwell is waiting until it is harder to treat. This is why screening exists — it looks for what you cannot yet feel.",
     " Katika hatua za awali <strong>saratani nyingi hazina dalili kabisa</strong>. Kusubiri kujisikia mgonjwa ni kusubiri hadi iwe vigumu zaidi kutibu. Ndiyo maana upimaji upo — hutafuta usichoweza kuhisi bado.",
     " Kwa early stages <strong>cancers nyingi hazina symptoms kabisa</strong>. Kungoja kujiskia mgonjwa ni kungoja mpaka iwe ngumu zaidi ku-treat. Ndio maana screening iko — inatafuta usichoweza kufeel bado.")},
   ]},

  # ── 2. Breast cancer ──────────────────────────────────────────────
  {"icon": "🎗️",
   "head": ("Breast Cancer", "Saratani ya Matiti", "Breast Cancer"),
   "blocks": [
    {"type": "p", "text": (
     "Breast cancer arises from breast tissue. It is the most common cancer among women in Kenya, mostly between ages 30 and 50. Men can develop it too, though rarely.",
     "Saratani ya matiti hutokea kwenye tishu za matiti. Ndiyo saratani ya kawaida zaidi kwa wanawake Kenya, hasa kati ya miaka 30 na 50. Wanaume wanaweza pia kuipata, ingawa ni nadra.",
     "Breast cancer inatoka kwa breast tissue. Ndio cancer common zaidi kwa wanawake Kenya, hasa kati ya miaka 30 na 50. Wanaume wanaweza pia kuipata, ingawa ni rare.")},
    {"type": "table",
     "headers": [("Risk factor", "Sababu ya hatari", "Risk factor"), ("Detail", "Maelezo", "Detail")],
     "rows": [
      [("Gender", "Jinsia", "Gender"), ("More common in women, though men can get it", "Ya kawaida zaidi kwa wanawake, ingawa wanaume wanaweza", "Common zaidi kwa wanawake, ingawa wanaume wanaweza")],
      [("Age", "Umri", "Age"), ("Risk increases with age, especially after 50", "Hatari huongezeka na umri, hasa baada ya 50", "Risk inaongezeka na age, hasa baada ya 50")],
      [("Family history", "Historia ya familia", "Family history"), ("Higher if close relatives had breast or ovarian cancer", "Juu zaidi kama ndugu wa karibu walikuwa na saratani ya matiti au ya kizazi", "Higher kama close relatives walikuwa na breast ama ovarian cancer")],
      [("Hormonal factors", "Sababu za homoni", "Hormonal factors"), ("High oestrogen, hormone therapy, periods starting before 12", "Estrojeni nyingi, tiba ya homoni, hedhi kuanza kabla ya miaka 12", "High oestrogen, hormone therapy, periods kuanza kabla ya 12")],
      [("Lifestyle", "Mtindo wa maisha", "Lifestyle"), ("Obesity, alcohol, lack of exercise, smoking", "Unene, pombe, ukosefu wa mazoezi, uvutaji", "Obesity, pombe, ukosefu wa exercise, smoking")],
     ]},
    {"type": "p", "text": (
     "Symptoms vary widely — lumps, swellings, skin changes — and many women have no obvious symptoms at all. Early growth cannot be seen or felt; it is found by imaging.",
     "Dalili hutofautiana sana — uvimbe, mabonge, mabadiliko ya ngozi — na wanawake wengi hawana dalili dhahiri kabisa. Ukuaji wa mapema hauwezi kuonekana au kuhisiwa; hupatikana kwa upigaji picha.",
     "Symptoms zinatofautiana sana — lumps, swellings, skin changes — na wanawake wengi hawana obvious symptoms kabisa. Early growth haiwezi kuonekana ama kuhisiwa; inapatikana kwa imaging.")},
   ]},

  # ── 3. Self-examination ───────────────────────────────────────────
  {"icon": "🪞",
   "head": ("Breast Self-Examination — Five Steps", "Kujichunguza Matiti — Hatua Tano", "Breast Self-Examination — Steps Tano"),
   "blocks": [
    {"type": "list", "ordered": True, "items": [
     ("Examine your breasts in a mirror with hands on hips",
      "Chunguza matiti yako kwenye kioo mikono ikiwa kiunoni",
      "Examine matiti yako kwa mirror mikono iko kiunoni"),
     ("Raise your arms and examine your breasts again",
      "Inua mikono yako na uchunguze matiti yako tena",
      "Raise mikono yako na u-examine matiti yako tena"),
     ("Look for any signs of fluid coming from the nipples",
      "Angalia dalili zozote za majimaji yanayotoka kwenye chuchu",
      "Angalia signs zozote za fluid inayotoka kwa nipples"),
     ("Feel for lumps while lying down",
      "Hisi uvimbe ukiwa umelala",
      "Feel lumps ukiwa umelala"),
     ("Feel your breasts for lumps while standing or sitting",
      "Hisi matiti yako kwa uvimbe ukiwa umesimama au umekaa",
      "Feel matiti yako kwa lumps ukiwa umesimama ama umekaa"),
    ]},
    {"type": "tip", "title": ("💡 When to do it", "💡 Wakati wa kufanya", "💡 Wakati wa kufanya"), "text": (
     " About a week after your period ends, when the breasts are not tender or swollen. Doing it at the same point each month is what lets you notice a change — you are comparing against yourself, not against anyone else.",
     " Takriban wiki moja baada ya hedhi kuisha, wakati matiti hayana maumivu wala hayajavimba. Kuifanya wakati mmoja kila mwezi ndiko kunakuwezesha kugundua mabadiliko — unajilinganisha na wewe mwenyewe, si na mtu mwingine.",
     " Karibu wiki moja baada ya periods kuisha, wakati matiti hayana pain wala hayaja-swell. Kuifanya wakati mmoja kila mwezi ndio inakuwezesha ku-notice change — una-compare na wewe mwenyewe, si na msee mwingine.")},
    {"type": "facilitator", "minutes": 10, "text": (
     "Demonstrate the five steps on yourself over clothing, or with a diagram. Keep it matter-of-fact — if you are embarrassed, the group will be too. In mixed groups, state plainly that men should learn this so they can encourage the women in their families.",
     "Onyesha hatua tano juu ya nguo zako, au kwa mchoro. Iweke kawaida — ukiwa na aibu, kundi litakuwa na aibu pia. Katika makundi mchanganyiko, sema wazi kwamba wanaume wanapaswa kujifunza hili ili waweze kuwahimiza wanawake katika familia zao.",
     "Demo steps tano juu ya nguo zako, ama na diagram. Iweke matter-of-fact — ukiwa na aibu, group itakuwa na aibu pia. Kwa mixed groups, sema wazi ati wanaume wanafaa kujifunza hii ili waweze ku-encourage wanawake kwa families zao.")},
   ]},

  # ── 4. Cervical cancer ────────────────────────────────────────────
  {"icon": "🌸",
   "head": ("Cervical Cancer", "Saratani ya Shingo ya Kizazi", "Cervical Cancer"),
   "blocks": [
    {"type": "p", "text": (
     "The cervix is the opening or 'mouth' of the womb, where it opens into the vagina. Cervical cancer occurs when cells there grow abnormally.",
     "Shingo ya kizazi ni mlango au 'mdomo' wa tumbo la uzazi, unapofunguka kwenye uke. Saratani ya shingo ya kizazi hutokea seli hapo zinapokua kwa njia isiyo ya kawaida.",
     "Cervix ni opening ama 'mdomo' wa womb, inapofunguka kwa vagina. Cervical cancer inahappen wakati cells hapo zinakua abnormally.")},
    {"type": "list", "items": [
     ("<strong>All women are at risk</strong>, most commonly between ages 35 and 49",
      "<strong>Wanawake wote wako hatarini</strong>, hasa kati ya miaka 35 na 49",
      "<strong>Wanawake wote wako at risk</strong>, hasa kati ya miaka 35 na 49"),
     ("In Kenya, <strong>nine women die of it every day</strong> — the second most common cancer among women after breast cancer",
      "Nchini Kenya, <strong>wanawake tisa hufa kwayo kila siku</strong> — saratani ya pili kwa ukawaida kwa wanawake baada ya ya matiti",
      "Kenya, <strong>wanawake tisa wanakufa kwayo kila siku</strong> — cancer ya pili kwa ukawaida kwa wanawake baada ya breast cancer"),
     ("It is caused by <strong>Human Papilloma Virus (HPV)</strong>, a sexually transmitted infection",
      "Husababishwa na <strong>Virusi vya Human Papilloma (HPV)</strong>, maambukizi ya zinaa",
      "Inasababishwa na <strong>Human Papilloma Virus (HPV)</strong>, STI"),
     ("Uncleared HPV takes <strong>10 to 15 years</strong> to turn cervical cells cancerous — which is a long window to catch it",
      "HPV isiyoondoka huchukua <strong>miaka 10 hadi 15</strong> kugeuza seli za shingo ya kizazi kuwa za saratani — ambao ni muda mrefu wa kuigundua",
      "HPV isiyo-clear inachukua <strong>miaka 10 hadi 15</strong> kugeuza cervical cells kuwa cancerous — ambayo ni window ndefu ya kuigundua"),
    ]},
    {"type": "table",
     "headers": [("Risk factors", "Sababu za hatari", "Risk factors"), ("Warning signs", "Dalili za onyo", "Warning signs")],
     "rows": [
      [("Other STIs", "Magonjwa mengine ya zinaa", "STIs zingine"), ("Bleeding outside the monthly period", "Kutokwa damu nje ya hedhi ya mwezi", "Bleeding nje ya monthly period")],
      [("Poor immunity, including HIV", "Kinga dhaifu, ikiwemo HIV", "Poor immunity, ikiwemo HIV"), ("Pain during sex, or bleeding after sex", "Maumivu wakati wa ngono, au kutokwa damu baadaye", "Pain wakati wa sex, ama bleeding baadaye")],
      [("Multiple sexual partners", "Wapenzi wengi wa ngono", "Sexual partners wengi"), ("A bloody discharge", "Majimaji yenye damu", "Bloody discharge")],
      [("A partner with multiple partners", "Mpenzi mwenye wapenzi wengi", "Partner mwenye partners wengi"), ("A bad vaginal smell that will not go away", "Harufu mbaya ukeni isiyoisha", "Bad vaginal smell isiyoisha")],
      [("Starting sex at an early age", "Kuanza ngono katika umri mdogo", "Kuanza sex kwa age ndogo"), ("Pain in the lower abdomen", "Maumivu tumbo la chini", "Pain kwa lower abdomen")],
      [("Tobacco use", "Matumizi ya tumbaku", "Tobacco use"), ("Bleeding again after menopause", "Kutokwa damu tena baada ya kukoma hedhi", "Bleeding tena baada ya menopause")],
     ]},
   ]},

  # ── 5. Screening & vaccine ────────────────────────────────────────
  {"icon": "🛡️",
   "head": ("Screening and the HPV Vaccine", "Upimaji na Chanjo ya HPV", "Screening na HPV Vaccine"),
   "blocks": [
    {"type": "p", "text": (
     "This is the part worth memorising, because it is the part that saves lives — and most peers have never been told it.",
     "Hii ndiyo sehemu inayostahili kukaririwa, kwa sababu ndiyo sehemu inayookoa maisha — na wenzako wengi hawajawahi kuambiwa.",
     "Hii ndio part inayostahili ku-memoriwa, kwa sababu ndio part inayookoa maisha — na wasee wengi hawajawahi kuambiwa.")},
    {"type": "table",
     "headers": [("Who and when", "Nani na lini", "Nani na lini"), ("Interval", "Kipindi", "Interval")],
     "rows": [
      [("Any woman over 25 who has ever had sex", "Mwanamke yeyote zaidi ya 25 aliyewahi kufanya ngono", "Mwanamke yeyote zaidi ya 25 aliyewahi kufanya sex"),
       ("Eligible for screening", "Anastahili kupimwa", "Anastahili screening")],
      [("Women who test HIV-negative", "Wanawake wasio na VVU", "Wanawake HIV-negative"),
       ("<strong>Every 5 years</strong>", "<strong>Kila miaka 5</strong>", "<strong>Kila miaka 5</strong>")],
      [("Women living with HIV", "Wanawake wanaoishi na VVU", "Wanawake wanaoishi na HIV"),
       ("<strong>Every year</strong>", "<strong>Kila mwaka</strong>", "<strong>Kila mwaka</strong>")],
      [("Using an HPV test", "Kwa kutumia kipimo cha HPV", "Ukitumia HPV test"),
       ("<strong>Every 3 years</strong>", "<strong>Kila miaka 3</strong>", "<strong>Kila miaka 3</strong>")],
     ]},
    {"type": "example", "title": ("🇰🇪 The free vaccine", "🇰🇪 Chanjo ya bure", "🇰🇪 Free vaccine"), "text": (
     "The HPV vaccine prevents cervical cancer. In Kenya it is given <strong>free to 10-year-old girls in public health facilities, as a single dose</strong>. If you know a family with a daughter that age, that is a conversation worth having.",
     "Chanjo ya HPV huzuia saratani ya shingo ya kizazi. Nchini Kenya hutolewa <strong>bure kwa wasichana wa miaka 10 katika vituo vya afya vya umma, kama dozi moja</strong>. Ukijua familia yenye binti wa umri huo, hayo ni mazungumzo yanayostahili kufanyika.",
     "HPV vaccine ina-prevent cervical cancer. Kenya inatolewa <strong>free kwa wasichana wa miaka 10 kwa public health facilities, kama single dose</strong>. Ukijua family yenye dem wa hiyo age, hiyo ni conversation inayostahili kufanyika.")},
    {"type": "tip", "title": ("💡 The headline", "💡 Kichwa cha habari", "💡 Headline"), "text": (
     " Cervical cancer is <strong>highly treatable if diagnosed early</strong>. Between a free vaccine at 10 and a screening window of 10 to 15 years, almost every one of those nine daily deaths was preventable.",
     " Saratani ya shingo ya kizazi <strong>inatibika sana ikigunduliwa mapema</strong>. Kati ya chanjo ya bure ya miaka 10 na dirisha la upimaji la miaka 10 hadi 15, karibu kila kimoja cha vifo hivyo tisa vya kila siku kingeweza kuzuiwa.",
     " Cervical cancer <strong>ina-treatika sana ikigunduliwa early</strong>. Kati ya free vaccine ya miaka 10 na screening window ya miaka 10 hadi 15, karibu kila moja ya hizo deaths tisa za kila siku ingeweza ku-preventiwa.")},
   ]},

  # ── 6. Practice ───────────────────────────────────────────────────
  {"icon": "🎭",
   "head": ("Practice — What Would You Do?", "Mazoezi — Ungefanya Nini?", "Practice — Ungefanya Nini?"),
   "blocks": [
    {"type": "p", "text": ("Choose an answer and see what follows.", "Chagua jibu na uone kinachofuata.", "Chagua answer uone kinachofollow.")},
    {"type": "scenario",
     "context": (
      "A mother in your community says she will not let her 10-year-old daughter have the HPV vaccine, because she believes it will encourage her to start having sex.",
      "Mama katika jamii yako anasema hatamruhusu binti yake wa miaka 10 kupata chanjo ya HPV, kwa sababu anaamini itamhimiza kuanza ngono.",
      "Mama kwa community yako anasema hatamruhusu dem wake wa miaka 10 kupata HPV vaccine, kwa sababu anaamini itamhimiza kuanza sex."),
     "question": ("How do you respond?", "Unajibu vipi?", "Una-respond aje?"),
     "choices": [
      {"kind": "bad",
       "text": ("Tell her she is wrong and that refusing is dangerous for her daughter",
                "Mwambie amekosea na kukataa ni hatari kwa binti yake",
                "Mwambie amekosea na kukataa ni hatari kwa dem wake"),
       "outcome": ("Telling a parent they are endangering their child puts them on the defensive immediately. The vaccine still does not get given — and now she will not raise the subject with you again.",
                   "Kumwambia mzazi anahatarisha mtoto wake humweka kujitetea mara moja. Chanjo bado haitolewi — na sasa hataleta suala hilo kwako tena.",
                   "Kumwambia mzazi ana-endanger mtoto wake inamweka defensive mara moja. Vaccine bado haitolewi — na saa hii hataleta hiyo topic kwako tena.")},
      {"kind": "good",
       "text": ("Explain that the vaccine works against a virus, and is given early because it must come before any exposure",
                "Eleza kwamba chanjo hufanya kazi dhidi ya virusi, na hutolewa mapema kwa sababu lazima itangulie kuambukizwa kokote",
                "Explain ati vaccine inawork dhidi ya virus, na inatolewa early kwa sababu lazima itangulie exposure yoyote"),
       "outcome": ("You said: 'It's not about sex — it's a vaccine against a virus, like measles. It's given at 10 because it has to be in place long before anyone could ever be exposed. It doesn't change what she does; it changes what her body can fight.' She took her daughter that month. ✅",
                   "Ulisema: 'Si kuhusu ngono — ni chanjo dhidi ya virusi, kama surua. Hutolewa akiwa na miaka 10 kwa sababu lazima iwepo muda mrefu kabla mtu hajaweza kuambukizwa. Haibadilishi anachofanya; inabadilisha mwili wake unachoweza kupambana nacho.' Alimpeleka binti yake mwezi huo. ✅",
                   "Ulisema: 'Si kuhusu sex — ni vaccine dhidi ya virus, kama measles. Inatolewa akiwa 10 kwa sababu lazima iwepo muda mrefu kabla mtu awe exposed. Haibadilishi anachofanya; inabadilisha mwili wake unachoweza ku-fight.' Alimpeleka dem wake mwezi huo. ✅")},
     ]},
    {"type": "scenario",
     "context": (
      "A 26-year-old woman tells you she does not need cervical screening because she feels perfectly healthy and has only ever had one partner.",
      "Mwanamke wa miaka 26 anakuambia hahitaji kupimwa saratani ya shingo ya kizazi kwa sababu anajisikia mwenye afya kabisa na amewahi kuwa na mpenzi mmoja tu.",
      "Mwanamke wa miaka 26 anakuambia hahitaji cervical screening kwa sababu anajiskia healthy kabisa na amewahi kuwa na partner mmoja tu."),
     "question": ("What is the accurate response?", "Jibu sahihi ni lipi?", "Response sahihi ni ipi?"),
     "choices": [
      {"kind": "bad",
       "text": ("Agree — one partner and no symptoms means she is not at risk",
                "Kubaliana — mpenzi mmoja na hakuna dalili maana yake hayuko hatarini",
                "Agree — partner mmoja na hakuna symptoms meaning hayuko at risk"),
       "outcome": ("All women who have ever had sex are eligible from 25, and early cervical cancer has no symptoms. A partner's own history also counts. Agreeing here costs her a screening she is entitled to.",
                   "Wanawake wote waliowahi kufanya ngono wanastahili kuanzia miaka 25, na saratani ya shingo ya kizazi ya mapema haina dalili. Historia ya mpenzi wake pia inahesabika. Kukubaliana hapa kunamgharimu upimaji anaostahili.",
                   "Wanawake wote waliowahi kufanya sex wanastahili kuanzia 25, na early cervical cancer haina symptoms. History ya partner wake pia inacount. Ku-agree hapa inamgharimu screening anayostahili.")},
      {"kind": "good",
       "text": ("Explain that she is eligible at 25, and that early cervical cancer has no symptoms",
                "Eleza kwamba anastahili akiwa na miaka 25, na saratani ya mapema haina dalili",
                "Explain ati anastahili akiwa 25, na early cervical cancer haina symptoms"),
       "outcome": ("You said: 'Any woman over 25 who's ever had sex should be screened — every five years. It's not about how many partners. Early cervical cancer feels like nothing at all, which is exactly why the screening exists.' She booked it. ✅",
                   "Ulisema: 'Mwanamke yeyote zaidi ya miaka 25 aliyewahi kufanya ngono anapaswa kupimwa — kila miaka mitano. Si kuhusu wapenzi wangapi. Saratani ya mapema haihisiwi kabisa, ndiyo maana upimaji upo.' Alipanga miadi. ✅",
                   "Ulisema: 'Mwanamke yeyote zaidi ya 25 aliyewahi kufanya sex anafaa kupimwa — kila miaka mitano. Si kuhusu partners wangapi. Early cervical cancer haifeeliki kabisa, ndio maana screening iko.' Aliweka appointment. ✅")},
     ]},
   ]},

  # ── 7. Key messages ───────────────────────────────────────────────
  {"icon": "🔑",
   "head": ("Key Messages", "Ujumbe Muhimu", "Key Messages"),
   "blocks": [
    {"type": "list", "items": [
     ("Know your body and report unusual changes early.",
      "Jua mwili wako na ripoti mabadiliko yasiyo ya kawaida mapema.",
      "Jua mwili wako na report unusual changes early."),
     ("Early detection through screening saves lives.",
      "Kugundua mapema kupitia upimaji huokoa maisha.",
      "Early detection kupitia screening inaokoa maisha."),
     ("Healthy habits — exercise, good diet, no alcohol or tobacco — reduce risk.",
      "Tabia nzuri — mazoezi, lishe bora, bila pombe au tumbaku — hupunguza hatari.",
      "Healthy habits — exercise, good diet, bila pombe ama tobacco — zinapunguza risk."),
     ("Family history matters — talk to your parents and guardians.",
      "Historia ya familia ni muhimu — zungumza na wazazi na walezi wako.",
      "Family history ni muhimu — ongea na wazazi na guardians wako."),
     ("Support each other to speak up and seek care without fear.",
      "Saidianeni kusema na kutafuta huduma bila hofu.",
      "Supportianeni kusema na kutafuta care bila fear."),
    ]},
    {"type": "sheng", "label": "Bottom Line", "text": (
     "Saratani ya mapema haiumi. Ndiyo maana watu husubiri. Na ndiyo maana kusubiri ndiko kunakoua — si saratani yenyewe pekee.",
     "Saratani ya mapema haiumi. Ndiyo maana watu husubiri. Na ndiyo maana kusubiri ndiko kunakoua — si saratani yenyewe pekee.",
     "Early cancer haiumi. Ndio maana wasee wanangoja. Na ndio maana kungoja ndio kunaua — si cancer yenyewe pekee.")},
   ]},
 ],

 "quiz": [
  {"q": "At early stages, most cancers:",
   "options": ["Cause severe pain", "Have no symptoms at all", "Cause visible lumps immediately", "Cause fever"],
   "answer": "B",
   "explain": "This is why screening exists — it looks for what cannot yet be felt. Waiting to feel unwell means waiting until treatment is harder."},

  {"q": "Which cancer is the most common among women in Kenya?",
   "options": ["Cervical cancer", "Breast cancer", "Colorectal cancer", "Oesophageal cancer"],
   "answer": "B",
   "explain": "Breast cancer is the most common, mostly between ages 30 and 50. Cervical cancer is second."},

  {"q": "When is the best time to do a breast self-examination?",
   "options": ["During your period",
               "About a week after your period ends",
               "Immediately before your period starts",
               "It makes no difference"],
   "answer": "B",
   "explain": "About a week after the period ends, when breasts are not tender or swollen. Doing it at the same point each month is what makes a change noticeable."},

  {"q": "What causes cervical cancer?",
   "options": ["Poor hygiene",
               "Human Papilloma Virus (HPV), a sexually transmitted infection",
               "Using contraception",
               "Having children too young"],
   "answer": "B",
   "explain": "HPV also causes cancers of the vagina, vulva and anus. Uncleared infection takes 10–15 years to turn cells cancerous."},

  {"q": "How often should a woman living with HIV be screened for cervical cancer?",
   "options": ["Every year", "Every 3 years", "Every 5 years", "Only if she has symptoms"],
   "answer": "A",
   "explain": "Annually. HIV-negative women are screened every 5 years, or every 3 years if using an HPV test."},

  {"q": "In Kenya, the HPV vaccine is:",
   "options": ["Sold privately to women over 25",
               "Given free to 10-year-old girls in public facilities, as a single dose",
               "Given only to women already diagnosed with HPV",
               "Not available in Kenya"],
   "answer": "B",
   "explain": "Free, single dose, at age 10 in public health facilities — given early because it must be in place before any possible exposure."},

  {"q": "Which are risk factors for cervical cancer? [SELECT ALL THAT APPLY]",
   "type": "msq",
   "options": ["Having other STIs",
               "Poor immunity, including from HIV",
               "Starting sexual activity at an early age",
               "Using tobacco",
               "Eating a high-sugar diet"],
   "answer": ["A", "B", "C", "D"],
   "explain": "A high-sugar diet is not among the listed cervical cancer risk factors. The other four are."},

  {"q": "Which are warning signs that should send a woman for a cervical check? [SELECT ALL THAT APPLY]",
   "type": "msq",
   "options": ["Bleeding outside the monthly period",
               "Pain during sex or bleeding after sex",
               "A bad vaginal smell that will not go away",
               "Bleeding again after menopause",
               "Breast tenderness before a period"],
   "answer": ["A", "B", "C", "D"],
   "explain": "Breast tenderness before a period is a normal cyclical change, not a cervical warning sign."},

  {"q": "A mother refuses the HPV vaccine for her 10-year-old, fearing it encourages sex. What is the best response?",
   "options": ["Tell her she is endangering her daughter",
               "Explain it is a vaccine against a virus, given early because it must precede any exposure",
               "Agree that 10 is too young",
               "Suggest she wait until the girl is 18"],
   "answer": "B",
   "explain": "Framing it as a virus vaccine — like measles — and explaining the timing addresses the real concern without putting the parent on the defensive."},

  {"q": "Roughly how many women die of cervical cancer in Kenya each day?",
   "options": ["One", "Nine", "Thirty", "Ninety"],
   "answer": "B",
   "explain": "Nine every day — and with a free vaccine at 10 and a 10–15 year screening window, most of those deaths were preventable."},
 ],
}
