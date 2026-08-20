# Module 8 (part 1 of 2) — Diabetes, Hypertension and Sickle Cell Disease
# Source: "Adolescent and Young Persons Peer Education — Updated slides", Module 8.
# Trilingual: English / Kiswahili / Sheng.

LESSON = {
 "file": "m08a-diabetes-hypertension-sickle-cell.html",
 "module_code": "M8",
 "module_slug": "non-communicable-diseases",
 "lesson_slug": "m08a-diabetes-hypertension-sickle-cell",
 "module_label": "Peer Educator · M8 · Part 1 of 2",
 "title": "Diabetes, Hypertension and Sickle Cell",
 "icon": "🫀",
 "duration": 60,

 "objectives": [
  ("Explain what non-communicable diseases are and why they are rising among young Kenyans",
   "Eleza magonjwa yasiyoambukiza ni nini na kwa nini yanaongezeka kwa vijana wa Kenya",
   "Explain non-communicable diseases ni nini na kwa nini zinaongezeka kwa vijana wa Kenya"),
  ("Describe diabetes, its types, risk factors and warning signs",
   "Eleza kisukari, aina zake, sababu za hatari na dalili za onyo",
   "Describe diabetes, types zake, risk factors na warning signs"),
  ("Explain why hypertension is called the silent condition",
   "Eleza kwa nini shinikizo la damu huitwa hali kimya",
   "Explain kwa nini hypertension inaitwa silent condition"),
  ("Describe how sickle cell disease is inherited and correct the myths around it",
   "Eleza jinsi ugonjwa wa selimundu unavyorithiwa na sahihisha imani potofu kuhusu huo",
   "Describe jinsi sickle cell inavyo-inheritiwa na correct myths kuihusu"),
 ],

 "big_question": (
  "<strong>🔍 Big Question:</strong> If you cannot catch it from anyone, and you feel completely fine, why would you ever get checked?",
  "<strong>🔍 Swali Kubwa:</strong> Kama huwezi kuambukizwa na mtu, na unajisikia vizuri kabisa, kwa nini ungepimwa?",
  "<strong>🔍 Big Question:</strong> Kama huwezi ku-catch kutoka kwa mtu, na unajiskia poa kabisa, kwa nini ungepimwa?"),

 "slides": [

  # ── 1. What NCDs are ──────────────────────────────────────────────
  {"icon": "📖",
   "head": ("Diseases You Cannot Catch", "Magonjwa Usiyoweza Kuambukizwa", "Magonjwa Huwezi Ku-catch"),
   "blocks": [
    {"type": "key_term", "term": ("🔑 Non-Communicable Disease (NCD)", "🔑 Ugonjwa Usioambukiza", "🔑 Non-Communicable Disease (NCD)"), "text": (
     "An illness that cannot be passed from one person to another. The main ones are heart disease, cancers, chronic lung disease and diabetes.",
     "Ugonjwa usioweza kuambukizwa kutoka kwa mtu mmoja hadi mwingine. Makuu ni magonjwa ya moyo, saratani, magonjwa sugu ya mapafu na kisukari.",
     "Ugonjwa ambao hauwezi ku-passiwa kutoka msee mmoja hadi mwingine. Makuu ni heart disease, cancers, chronic lung disease na diabetes.")},
    {"type": "p", "text": (
     "These are becoming common among young people in Kenya through unhealthy eating, lack of exercise and substance use. More adolescents are now facing obesity, high blood pressure and early diabetes.",
     "Haya yanazidi kuwa ya kawaida kwa vijana nchini Kenya kutokana na ulaji usiofaa, ukosefu wa mazoezi na matumizi ya dawa za kulevya. Vijana wengi zaidi sasa wanakabiliwa na unene, shinikizo la damu na kisukari cha mapema.",
     "Hizi zinazidi kuwa common kwa vijana Kenya kutokana na unhealthy eating, ukosefu wa exercise na substance use. Vijana wengi zaidi saa hii wanaface obesity, high blood pressure na early diabetes.")},
    {"type": "p", "text": (
     "This part covers three: diabetes, hypertension and sickle cell disease. Part 2 covers breast and cervical cancer.",
     "Sehemu hii inahusu matatu: kisukari, shinikizo la damu na ugonjwa wa selimundu. Sehemu ya 2 inahusu saratani ya matiti na ya shingo ya kizazi.",
     "Hii part inacover tatu: diabetes, hypertension na sickle cell. Part 2 inacover breast na cervical cancer.")},
    {"type": "warn", "title": ("⚠️ The myth to kill first", "⚠️ Imani potofu ya kuua kwanza", "⚠️ Myth ya ku-kill kwanza"), "text": (
     " None of these are contagious, none are a punishment, and none are only for the old or the rich. A peer educator who lets those three ideas stand has already lost the room.",
     " Hakuna hata moja inayoambukiza, hakuna ni adhabu, na hakuna ni ya wazee au matajiri tu. Mwelimishaji rika anayeacha mawazo hayo matatu yasimame tayari amepoteza chumba.",
     " Hakuna hata moja inayoambukiza, hakuna ni punishment, na hakuna ni ya wazee ama matajiri tu. Peer educator anayeacha hizo ideas tatu zisimame tayari amepoteza room.")},
   ]},

  # ── 2. Diabetes overview ──────────────────────────────────────────
  {"icon": "🩸",
   "head": ("Diabetes — What Is Actually Happening", "Kisukari — Kinachotokea Hasa", "Diabetes — Kinachohappen Hasa"),
   "blocks": [
    {"type": "p", "text": (
     "Diabetes is a long-term condition where the body cannot properly use or make enough insulin, so sugar builds up in the blood.",
     "Kisukari ni hali ya muda mrefu ambapo mwili hauwezi kutumia vizuri au kutengeneza insulini ya kutosha, hivyo sukari hujilimbikiza kwenye damu.",
     "Diabetes ni long-term condition ambapo mwili hauwezi kutumia properly ama kutengeneza insulin ya kutosha, so sugar inajilimbikiza kwa damu.")},
    {"type": "tip", "title": ("💡 The key and the door", "💡 Ufunguo na mlango", "💡 Key na door"), "text": (
     " Think of insulin as a key and your cells as locked doors. Sugar needs the key to get in and be used for energy. No key, or a key that no longer fits, and the sugar stays outside in the blood.",
     " Fikiria insulini kama ufunguo na seli zako kama milango iliyofungwa. Sukari inahitaji ufunguo kuingia na kutumika kama nguvu. Bila ufunguo, au ufunguo usiofaa tena, sukari hubaki nje kwenye damu.",
     " Fikiria insulin kama key na cells zako kama doors zilizofungwa. Sugar inahitaji key kuingia na kutumika kama energy. Bila key, ama key isiyofit tena, sugar inabaki nje kwa damu.")},
    {"type": "table",
     "headers": [("Type", "Aina", "Type"), ("What goes wrong", "Kinachoenda vibaya", "Kinachoenda vibaya")],
     "rows": [
      [("Type 1", "Aina ya 1", "Type 1"),
       ("No insulin at all — no key, so sugar cannot enter the cell. Not related to weight.",
        "Hakuna insulini kabisa — hakuna ufunguo, hivyo sukari haiwezi kuingia kwenye seli. Haihusiani na uzito.",
        "Hakuna insulin kabisa — hakuna key, so sugar haiwezi kuingia kwa cell. Hai-relate na weight.")],
      [("Type 2", "Aina ya 2", "Type 2"),
       ("Insulin cannot unlock the doors — the body resists it or cannot use it properly.",
        "Insulini haiwezi kufungua milango — mwili unaipinga au hauwezi kuitumia vizuri.",
        "Insulin haiwezi ku-unlock doors — mwili unai-resist ama hauwezi kuitumia properly.")],
      [("Gestational", "Ya ujauzito", "Gestational"),
       ("Occurs in women during pregnancy without a previous history of diabetes.",
        "Hutokea kwa wanawake wakati wa ujauzito bila historia ya awali ya kisukari.",
        "Inahappen kwa wanawake wakati wa pregnancy bila history ya awali ya diabetes.")],
     ]},
   ]},

  # ── 3. Diabetes signs & risks ─────────────────────────────────────
  {"icon": "🔍",
   "head": ("Diabetes — Signs and Risk Factors", "Kisukari — Dalili na Sababu za Hatari", "Diabetes — Signs na Risk Factors"),
   "blocks": [
    {"type": "table",
     "headers": [("Warning signs", "Dalili za onyo", "Warning signs"), ("Risk factors", "Sababu za hatari", "Risk factors")],
     "rows": [
      [("Frequent urination", "Kukojoa mara kwa mara", "Kukojoa mara kwa mara"), ("Physical inactivity", "Ukosefu wa mazoezi", "Physical inactivity")],
      [("Excessive thirst", "Kiu kikubwa", "Kiu kubwa"), ("Obesity and unhealthy diet", "Unene na ulaji usiofaa", "Obesity na unhealthy diet")],
      [("Extreme hunger", "Njaa kali", "Njaa kali"), ("Smoking and alcohol", "Uvutaji na pombe", "Smoking na pombe")],
      [("Increased fatigue", "Uchovu ulioongezeka", "Fatigue iliyoongezeka"), ("Family history", "Historia ya familia", "Family history")],
      [("Blurred vision", "Kuona kwa ukungu", "Blurred vision"), ("Advancing age", "Umri unaoongezeka", "Advancing age")],
      [("Unexplained weight loss", "Kupungua uzito bila sababu", "Kupungua weight bila sababu"), ("Stress and steroid use", "Msongo na matumizi ya steroidi", "Stress na steroid use")],
     ]},
    {"type": "warn", "title": ("⚠️ Complications if untreated", "⚠️ Matatizo kama haitatibiwa", "⚠️ Complications kama haita-treatiwa"), "text": (
     " Loss of sensation, numbness and tingling, and wounds that will not heal. A small cut that does not close is a reason to be tested, not a reason to wait.",
     " Kupoteza hisia, ganzi na mchecheto, na majeraha yasiyopona. Mkato mdogo usiofunga ni sababu ya kupimwa, si sababu ya kusubiri.",
     " Kupoteza sensation, numbness na tingling, na wounds zisizo-heal. Cut ndogo isiyo-close ni sababu ya kupimwa, si sababu ya kungoja.")},
   ]},

  # ── 4. Diabetes myths ─────────────────────────────────────────────
  {"icon": "🚫",
   "head": ("Diabetes — Myths You Will Meet", "Kisukari — Imani Potofu Utakazokutana Nazo", "Diabetes — Myths Utakutana Nazo"),
   "blocks": [
    {"type": "p", "text": (
     "These are the ten you will actually hear. Learn the fact beside each one — correcting them is a large part of your job.",
     "Hizi ndizo kumi utakazosikia hasa. Jifunze ukweli ulio kando ya kila moja — kuzisahihisha ni sehemu kubwa ya kazi yako.",
     "Hizi ndio kumi utasikia hasa. Jifunze fact iliyo kando ya kila moja — ku-correct hizi ni part kubwa ya job yako.")},
    {"type": "table",
     "headers": [("Myth", "Imani potofu", "Myth"), ("Fact", "Ukweli", "Fact")],
     "rows": [
      [("Diabetes only affects the rich", "Kisukari huathiri matajiri tu", "Diabetes inaathiri matajiri tu"),
       ("It is not a disease for the rich. It can affect anyone.", "Si ugonjwa wa matajiri. Unaweza kumwathiri yeyote.", "Si ugonjwa wa matajiri. Inaweza kuathiri yeyote.")],
      [("Only overweight people get it", "Wanene tu ndio hupata", "Wanene tu ndio wanapata"),
       ("It affects any weight. Type 1 has no link to weight at all.", "Huathiri uzito wowote. Aina ya 1 haihusiani na uzito kabisa.", "Inaathiri weight yoyote. Type 1 hai-relate na weight kabisa.")],
      [("Eating too much sugar causes it", "Kula sukari nyingi husababisha", "Kukula sugar nyingi inasababisha"),
       ("The main causes are genetic and lifestyle factors, not sugar alone.", "Sababu kuu ni za kijeni na mtindo wa maisha, si sukari peke yake.", "Main causes ni genetic na lifestyle factors, si sugar peke yake.")],
      [("They cannot eat carbohydrates", "Hawawezi kula wanga", "Hawawezi kukula carbs"),
       ("They can — intake is balanced against medication and activity.", "Wanaweza — kiasi hulinganishwa na dawa na mazoezi.", "Wanaweza — intake ina-balanciwa na medication na activity.")],
      [("Only older people get Type 2", "Wazee tu ndio hupata Aina ya 2", "Wazee tu ndio wanapata Type 2"),
       ("It also occurs in children and teenagers, especially with rising obesity.", "Pia hutokea kwa watoto na vijana, hasa na unene unaoongezeka.", "Pia inahappen kwa watoto na teenagers, hasa na obesity inayoongezeka.")],
      [("They should avoid exercise", "Wanapaswa kuepuka mazoezi", "Wanafaa ku-avoid exercise"),
       ("Regular activity is crucial — it helps control blood sugar.", "Mazoezi ya kawaida ni muhimu sana — husaidia kudhibiti sukari ya damu.", "Regular activity ni muhimu sana — inasaidia ku-control blood sugar.")],
      [("Diabetes is contagious", "Kisukari huambukiza", "Diabetes inaambukiza"),
       ("It cannot be passed between people like a virus or bacteria.", "Hauwezi kupitishwa kati ya watu kama virusi au bakteria.", "Haiwezi ku-passiwa kati ya wasee kama virus ama bacteria.")],
      [("You cannot live a normal life", "Huwezi kuishi maisha ya kawaida", "Huwezi kuishi normal life"),
       ("With proper management, people live long, healthy, active lives.", "Kwa usimamizi mzuri, watu huishi maisha marefu, yenye afya na shughuli.", "Na proper management, wasee wanaishi long, healthy, active lives.")],
      [("Medication can cure it", "Dawa zinaweza kuiponya", "Medication inaweza kui-cure"),
       ("There is no cure yet — but it can be managed effectively.", "Hakuna tiba bado — lakini unaweza kusimamiwa vizuri.", "Hakuna cure bado — lakini inaweza ku-managiwa effectively.")],
      [("Herbal medicine treats it", "Dawa za mitishamba huitibu", "Herbal medicine inai-treat"),
       ("Avoid herbal medication — use only what a health professional prescribes.", "Epuka dawa za mitishamba — tumia tu zilizoagizwa na mtaalamu wa afya.", "Avoid herbal medication — tumia tu iliyo-prescribiwa na health professional.")],
     ]},
    {"type": "facilitator", "minutes": 12, "text": (
     "Read each myth aloud and ask the group to vote true or false before revealing the fact. Expect the sugar one and the herbal one to split the room — those two are the most stubborn in practice.",
     "Soma kila imani potofu kwa sauti na uulize kundi lipige kura kweli au uongo kabla ya kufichua ukweli. Tarajia ile ya sukari na ile ya mitishamba kugawanya chumba — hizo mbili ndizo sugu zaidi kivitendo.",
     "Soma kila myth kwa sauti na uulize group i-vote true ama false kabla ya ku-reveal fact. Expect ile ya sugar na ile ya herbal ku-split room — hizo mbili ndio stubborn zaidi practically.")},
   ]},

  # ── 5. Hypertension ───────────────────────────────────────────────
  {"icon": "🤫",
   "head": ("Hypertension — The Silent One", "Shinikizo la Damu — Lile Kimya", "Hypertension — Ile Silent"),
   "blocks": [
    {"type": "p", "text": (
     "Blood pressure measures the force of blood pushing against the artery walls. It is written as a fraction, such as 140/90 mm Hg — read as 'one forty over ninety'.",
     "Shinikizo la damu hupima nguvu ya damu inayosukuma kuta za mishipa. Huandikwa kama sehemu, kama 140/90 mm Hg — husomwa 'mia moja arobaini juu ya tisini'.",
     "Blood pressure inapima force ya damu inayosukuma walls za arteries. Inaandikwa kama fraction, kama 140/90 mm Hg — inasomwa 'one forty over ninety'.")},
    {"type": "key_term", "term": ("🔑 Hypertension", "🔑 Shinikizo la Damu", "🔑 Hypertension"), "text": (
     "High blood pressure — when the top (systolic) reading is 140 or above, or the bottom (diastolic) reading is 90 or above, or both.",
     "Shinikizo la juu la damu — wakati usomaji wa juu (sistoli) ni 140 au zaidi, au wa chini (diastoli) ni 90 au zaidi, au vyote viwili.",
     "High blood pressure — wakati reading ya juu (systolic) ni 140 ama zaidi, ama ya chini (diastolic) ni 90 ama zaidi, ama zote mbili.")},
    {"type": "warn", "title": ("⚠️ Why it is called silent", "⚠️ Kwa nini huitwa kimya", "⚠️ Kwa nini inaitwa silent"), "text": (
     " About <strong>75% of people with hypertension have no symptoms at all</strong>. Even someone with very high blood pressure can feel completely fine. Feeling well is not evidence of a normal reading — only a check is.",
     " Takriban <strong>asilimia 75 ya watu wenye shinikizo la damu hawana dalili kabisa</strong>. Hata mwenye shinikizo la juu sana anaweza kujisikia vizuri kabisa. Kujisikia vizuri si ushahidi wa usomaji wa kawaida — kipimo pekee ndicho.",
     " Karibu <strong>75% ya wasee wenye hypertension hawana symptoms kabisa</strong>. Hata msee mwenye very high blood pressure anaweza kujiskia poa kabisa. Kujiskia poa si evidence ya normal reading — checkup pekee ndio.")},
    {"type": "list", "items": [
     ("<strong>Risk factors:</strong> obesity, tobacco, stress, family history, alcohol, excess salt, unhealthy diet, physical inactivity",
      "<strong>Sababu za hatari:</strong> unene, tumbaku, msongo, historia ya familia, pombe, chumvi nyingi, ulaji usiofaa, ukosefu wa mazoezi",
      "<strong>Risk factors:</strong> obesity, tobacco, stress, family history, pombe, chumvi nyingi, unhealthy diet, physical inactivity"),
     ("<strong>Know your family history</strong> and discuss monitoring with a health provider",
      "<strong>Jua historia ya familia yako</strong> na jadili ufuatiliaji na mtoa huduma za afya",
      "<strong>Jua family history yako</strong> na discuss monitoring na health provider"),
     ("<strong>Regular checks</strong> catch it early — that is the entire strategy",
      "<strong>Vipimo vya kawaida</strong> huigundua mapema — hiyo ndiyo mkakati mzima",
      "<strong>Regular checks</strong> zinaigundua mapema — hiyo ndio strategy nzima"),
    ]},
   ]},

  # ── 6. Sickle cell ────────────────────────────────────────────────
  {"icon": "🧬",
   "head": ("Sickle Cell Disease", "Ugonjwa wa Selimundu", "Sickle Cell Disease"),
   "blocks": [
    {"type": "p", "text": (
     "Sickle cell disease is a genetic illness affecting the red blood cells that carry oxygen around the body. People with SCD make an abnormal haemoglobin (HbS) that turns red cells hard and sticky — sickle-shaped.",
     "Ugonjwa wa selimundu ni ugonjwa wa kurithi unaoathiri chembechembe nyekundu za damu zinazobeba oksijeni mwilini. Wenye SCD hutengeneza himoglobini isiyo ya kawaida (HbS) inayofanya chembe nyekundu kuwa ngumu na kunata — umbo la mundu.",
     "Sickle cell disease ni genetic illness inayoathiri red blood cells zinazobeba oxygen mwilini. Wasee wenye SCD wanatengeneza abnormal haemoglobin (HbS) inayofanya red cells kuwa ngumu na sticky — sickle-shaped.")},
    {"type": "p", "text": (
     "Those stiff cells get stuck in blood vessels, block blood flow, and cause pain or damage to major organs.",
     "Chembe hizo ngumu hukwama kwenye mishipa ya damu, huzuia mtiririko wa damu, na kusababisha maumivu au uharibifu wa viungo vikuu.",
     "Hizo stiff cells zinakwama kwa blood vessels, zina-block blood flow, na kusababisha pain ama damage kwa major organs.")},
    {"type": "example", "title": ("🇰🇪 Where it is common in Kenya", "🇰🇪 Ilipo kawaida Kenya", "🇰🇪 Ilipo common Kenya"), "text": (
     "About 17 counties in the lake and coastal regions carry a high SCD burden, linked to malaria endemicity in those areas. If you work in those counties, you will meet this — and so will your peers.",
     "Takriban kaunti 17 katika maeneo ya ziwa na pwani zina mzigo mkubwa wa SCD, unaohusishwa na uenezi wa malaria katika maeneo hayo. Ukifanya kazi katika kaunti hizo, utakutana na hili — na wenzako pia.",
     "Karibu counties 17 kwa lake na coastal regions zina high SCD burden, iliyo-linkiwa na malaria endemicity kwa hizo areas. Ukifanya kazi kwa hizo counties, utakutana na hii — na wasee wako pia.")},
    {"type": "list", "items": [
     ("<strong>Pain</strong> — can occur in any part of the body",
      "<strong>Maumivu</strong> — yanaweza kutokea sehemu yoyote ya mwili",
      "<strong>Pain</strong> — inaweza kuhappen sehemu yoyote ya mwili"),
     ("<strong>Swelling of hands and feet</strong>, often with fever — mainly in babies up to 2 years",
      "<strong>Kuvimba kwa mikono na miguu</strong>, mara nyingi na homa — hasa kwa watoto hadi miaka 2",
      "<strong>Kuvimba kwa mikono na miguu</strong>, mara nyingi na fever — hasa kwa watoto hadi miaka 2"),
     ("<strong>Anaemia</strong> — tiredness, pale skin, shortness of breath, dizziness, fast heartbeat",
      "<strong>Upungufu wa damu</strong> — uchovu, ngozi iliyopauka, kupumua kwa shida, kizunguzungu, mapigo ya haraka",
      "<strong>Anaemia</strong> — uchovu, ngozi pale, shortness of breath, dizziness, fast heartbeat"),
     ("<strong>Jaundice</strong> — yellowing of the whites of the eyes, skin or urine",
      "<strong>Manjano</strong> — kuwa njano kwa weupe wa macho, ngozi au mkojo",
      "<strong>Jaundice</strong> — kuwa yellow kwa weupe wa macho, ngozi ama urine"),
    ]},
   ]},

  # ── 7. Inheritance ────────────────────────────────────────────────
  {"icon": "👨‍👩‍👧",
   "head": ("How Sickle Cell Is Inherited", "Jinsi Selimundu Inavyorithiwa", "Jinsi Sickle Cell Ina-inheritiwa"),
   "blocks": [
    {"type": "p", "text": (
     "This is the part peers get wrong most often. Sickle cell is present at birth and inherited from both parents — you cannot catch it, and nobody gave it to anybody on purpose.",
     "Hii ndiyo sehemu wenzako hukosea mara nyingi zaidi. Selimundu ipo tangu kuzaliwa na hurithiwa kutoka kwa wazazi wote wawili — huwezi kuiambukizwa, na hakuna aliyempa mtu kwa makusudi.",
     "Hii ndio part wasee wanakosea mara nyingi zaidi. Sickle cell iko tangu kuzaliwa na ina-inheritiwa kutoka kwa wazazi wote wawili — huwezi kui-catch, na hakuna aliyempa mtu kwa makusudi.")},
    {"type": "table",
     "headers": [("Genes", "Jeni", "Genes"), ("What it means", "Maana yake", "Maana yake")],
     "rows": [
      [("<strong>AA</strong>", "<strong>AA</strong>", "<strong>AA</strong>"),
       ("Normal haemoglobin. Not affected, not a carrier.", "Himoglobini ya kawaida. Hajaathiriwa, si mbebaji.", "Normal haemoglobin. Hajaathiriwa, si carrier.")],
      [("<strong>AS</strong>", "<strong>AS</strong>", "<strong>AS</strong>"),
       ("One sickle gene — a <strong>healthy carrier</strong>. Does not have the disease.", "Jeni moja ya selimundu — <strong>mbebaji mwenye afya</strong>. Hana ugonjwa.", "Gene moja ya sickle — <strong>healthy carrier</strong>. Hana ugonjwa.")],
      [("<strong>SS</strong>", "<strong>SS</strong>", "<strong>SS</strong>"),
       ("Two sickle genes, one from each parent — <strong>has sickle cell disease</strong>.", "Jeni mbili za selimundu, moja kutoka kwa kila mzazi — <strong>ana ugonjwa wa selimundu</strong>.", "Genes mbili za sickle, moja kutoka kwa kila mzazi — <strong>ana sickle cell disease</strong>.")],
     ]},
    {"type": "tip", "title": ("💡 Why carriers matter", "💡 Kwa nini wabebaji ni muhimu", "💡 Kwa nini carriers ni muhimu"), "text": (
     " A carrier (AS) is healthy and usually has no idea. But if two carriers have a child together, there is a real chance that child will have the disease (SS). That is why knowing your status before starting a family matters — not to blame anyone, but to plan.",
     " Mbebaji (AS) ana afya na kwa kawaida hajui. Lakini wabebaji wawili wakipata mtoto pamoja, kuna uwezekano halisi mtoto huyo atakuwa na ugonjwa (SS). Ndiyo maana kujua hali yako kabla ya kuanzisha familia ni muhimu — si kumlaumu yeyote, bali kupanga.",
     " Carrier (AS) ana afya na kwa kawaida hajui. Lakini carriers wawili wakipata mtoto pamoja, kuna real chance huyo mtoto atakuwa na ugonjwa (SS). Ndio maana kujua status yako kabla ya kuanza family ni muhimu — si ku-blame mtu, ni ku-plan.")},
    {"type": "sheng", "text": (
     "Hakuna mtu aliyechagua jeni zake. Ugonjwa wa selimundu si laana, si adhabu, wala si kosa la mtu. Ni damu — na damu inaweza kupimwa.",
     "Hakuna aliyechagua jeni zake. Selimundu si laana, si adhabu, wala si kosa la mtu. Ni damu — na damu inaweza kupimwa.",
     "Hakuna msee alichagua genes zake. Sickle cell si laana, si punishment, wala si kosa la mtu. Ni damu — na damu inaweza kupimwa.")},
   ]},

  # ── 8. Practice ───────────────────────────────────────────────────
  {"icon": "🎭",
   "head": ("Practice — What Would You Do?", "Mazoezi — Ungefanya Nini?", "Practice — Ungefanya Nini?"),
   "blocks": [
    {"type": "p", "text": ("Choose an answer and see what follows.", "Chagua jibu na uone kinachofuata.", "Chagua answer uone kinachofollow.")},
    {"type": "scenario",
     "context": (
      "In a session in Kisumu, a boy says his aunt was told she has sickle cell and that the family believes someone bewitched her. Others in the group nod.",
      "Katika kipindi Kisumu, mvulana anasema shangazi yake aliambiwa ana selimundu na familia inaamini mtu alimloga. Wengine kwenye kundi wanaitikia.",
      "Kwa session Kisumu, mse mmoja anasema aunt wake aliambiwa ana sickle cell na family inaamini mtu alimloga. Wengine kwa group wanaitikia."),
     "question": ("How do you handle this?", "Unashughulikia hili vipi?", "Una-handle hii aje?"),
     "choices": [
      {"kind": "bad",
       "text": ("Tell them that is nonsense and move on with the lesson",
                "Waambie hiyo ni upuuzi na uendelee na somo",
                "Waambie hiyo ni upuuzi na uendelee na lesson"),
       "outcome": ("Calling a family's belief nonsense closes the conversation and makes you the outsider. The belief does not go away — it just stops being said in front of you, which means you can no longer correct it.",
                   "Kuita imani ya familia upuuzi hufunga mazungumzo na kukufanya wewe mgeni. Imani haiondoki — inaacha tu kusemwa mbele yako, maana yake huwezi tena kuisahihisha.",
                   "Ku-call belief ya family upuuzi inafunga conversation na inakufanya wewe outsider. Belief hai-go away — inaacha tu kusemwa mbele yako, meaning huwezi tena kui-correct.")},
      {"kind": "good",
       "text": ("Explain the AA / AS / SS inheritance simply, without attacking the family",
                "Eleza urithi wa AA / AS / SS kwa urahisi, bila kushambulia familia",
                "Explain inheritance ya AA / AS / SS simply, bila ku-attack family"),
       "outcome": ("You said: 'Sickle cell comes from genes — two carriers can have a child with it, and neither of them did anything wrong. Nobody caused this.' The boy asked whether his own blood could be tested. That question is the whole point. ✅",
                   "Ulisema: 'Selimundu hutoka kwa jeni — wabebaji wawili wanaweza kupata mtoto nayo, na hakuna aliyefanya kosa. Hakuna aliyesababisha hili.' Mvulana aliuliza kama damu yake mwenyewe inaweza kupimwa. Swali hilo ndilo lengo lote. ✅",
                   "Ulisema: 'Sickle cell inatoka kwa genes — carriers wawili wanaweza kupata mtoto nayo, na hakuna aliyefanya kosa. Hakuna aliyesababisha hii.' Yule mse aliuliza kama damu yake mwenyewe inaweza kupimwa. Hiyo question ndio point yote. ✅")},
     ]},
    {"type": "scenario",
     "context": (
      "A 19-year-old tells you he does not need a blood pressure check because he plays football every week and feels completely healthy.",
      "Kijana wa miaka 19 anakuambia hahitaji kipimo cha shinikizo la damu kwa sababu anacheza mpira kila wiki na anajisikia mwenye afya kabisa.",
      "Msee wa 19 anakuambia hahitaji blood pressure check kwa sababu anacheza mpira kila wiki na anajiskia healthy kabisa."),
     "question": ("What is the accurate response?", "Jibu sahihi ni lipi?", "Response sahihi ni ipi?"),
     "choices": [
      {"kind": "bad",
       "text": ("Agree — being fit and active means his blood pressure is fine",
                "Kubaliana — kuwa na siha na shughuli maana yake shinikizo lake ni sawa",
                "Agree — kuwa fit na active meaning blood pressure yake ni poa"),
       "outcome": ("Fitness lowers risk, but it does not replace a reading. Around 75% of people with hypertension have no symptoms — including active ones. Agreeing here teaches him that feeling well is a substitute for being checked.",
                   "Siha hupunguza hatari, lakini haichukui nafasi ya kipimo. Karibu asilimia 75 ya wenye shinikizo la damu hawana dalili — wakiwemo wenye shughuli. Kukubaliana hapa kunamfundisha kwamba kujisikia vizuri ni mbadala wa kupimwa.",
                   "Fitness inapunguza risk, lakini hai-replace reading. Karibu 75% ya wasee wenye hypertension hawana symptoms — wakiwemo active ones. Ku-agree hapa inamfundisha ati kujiskia poa ni substitute ya kupimwa.")},
      {"kind": "good",
       "text": ("Explain that 75% of people with hypertension feel nothing at all",
                "Eleza kwamba asilimia 75 ya wenye shinikizo la damu hawajisikii chochote",
                "Explain ati 75% ya wasee wenye hypertension hawajiskii kitu"),
       "outcome": ("You said: 'Football helps — genuinely. But three out of four people with high blood pressure feel exactly like you do. The check takes two minutes and it's the only way to know.' He got checked at the next outreach. ✅",
                   "Ulisema: 'Mpira husaidia — kweli. Lakini watu watatu kati ya wanne wenye shinikizo la juu hujisikia sawa kabisa na wewe. Kipimo huchukua dakika mbili na ndiyo njia pekee ya kujua.' Alipimwa kwenye ufikiaji uliofuata. ✅",
                   "Ulisema: 'Mpira inasaidia — kweli. Lakini wasee watatu kati ya wanne wenye high blood pressure wanajiskia exactly kama wewe. Check inachukua dakika mbili na ndio njia pekee ya kujua.' Alipimwa kwa outreach iliyofuata. ✅")},
     ]},
   ]},

  # ── 9. Key messages ───────────────────────────────────────────────
  {"icon": "🔑",
   "head": ("Key Messages", "Ujumbe Muhimu", "Key Messages"),
   "blocks": [
    {"type": "list", "items": [
     ("Non-communicable diseases cannot be caught from another person.",
      "Magonjwa yasiyoambukiza hayawezi kuambukizwa kutoka kwa mtu mwingine.",
      "Non-communicable diseases haziwezi ku-catchiwa kutoka kwa msee mwingine."),
     ("They are rising among young Kenyans through diet, inactivity and substance use.",
      "Yanaongezeka kwa vijana wa Kenya kutokana na ulaji, ukosefu wa mazoezi na dawa za kulevya.",
      "Zinaongezeka kwa vijana wa Kenya kutokana na diet, inactivity na substance use."),
     ("Hypertension is silent — about 75% of people with it have no symptoms.",
      "Shinikizo la damu ni kimya — takriban asilimia 75 ya walio nalo hawana dalili.",
      "Hypertension ni silent — karibu 75% ya walio nayo hawana symptoms."),
     ("Sickle cell is inherited, not caught and not cursed. AA, AS, SS.",
      "Selimundu hurithiwa, haiambukizwi wala si laana. AA, AS, SS.",
      "Sickle cell ina-inheritiwa, haiambukizwi wala si laana. AA, AS, SS."),
     ("Early detection changes the outcome for every one of these conditions.",
      "Kugundua mapema hubadilisha matokeo kwa kila moja ya hali hizi.",
      "Early detection inabadilisha outcome kwa kila moja ya hizi conditions."),
    ]},
   ]},
 ],

 "quiz": [
  {"q": "What does 'non-communicable' mean?",
   "options": ["The disease has no known cure",
               "The disease cannot be passed from one person to another",
               "The disease has no symptoms",
               "The disease only affects older people"],
   "answer": "B",
   "explain": "NCDs cannot be transmitted between people. Diabetes, hypertension, sickle cell and cancers are all non-communicable."},

  {"q": "Insulin is best described as:",
   "options": ["A sugar the body burns for energy",
               "A key that lets sugar enter the cells",
               "A type of red blood cell",
               "A medicine only Type 2 patients take"],
   "answer": "B",
   "explain": "No key, or a key the cell no longer responds to, and sugar stays in the blood instead of being used."},

  {"q": "Which of these are MYTHS about diabetes? [SELECT ALL THAT APPLY]",
   "type": "msq",
   "options": ["It only affects the rich",
               "It is contagious",
               "People with diabetes should avoid exercise",
               "There is currently no cure, but it can be managed",
               "Only overweight people get it"],
   "answer": ["A", "B", "C", "E"],
   "explain": "Option D is the fact, not a myth. Exercise is in fact crucial for controlling blood sugar."},

  {"q": "Roughly what proportion of people with hypertension have no symptoms?",
   "options": ["About 10%", "About 25%", "About 50%", "About 75%"],
   "answer": "D",
   "explain": "Around three in four feel nothing at all — which is exactly why it is called the silent condition."},

  {"q": "A blood pressure reading of 140/90 mm Hg or above indicates:",
   "options": ["Normal pressure for an adolescent",
               "Hypertension",
               "Low blood pressure",
               "Diabetes"],
   "answer": "B",
   "explain": "Hypertension is a systolic reading of 140 or more, or a diastolic of 90 or more, or both."},

  {"q": "A person with genes AS has:",
   "options": ["Sickle cell disease",
               "Normal haemoglobin and no sickle gene",
               "One sickle gene — a healthy carrier",
               "A condition that will develop into SCD later"],
   "answer": "C",
   "explain": "AS is a healthy carrier. AA is unaffected, SS has the disease. Carriers usually do not know their status."},

  {"q": "Two healthy carriers (AS and AS) have a child. What is true?",
   "options": ["The child cannot have sickle cell disease",
               "There is a real chance the child will have sickle cell disease",
               "The child will definitely have sickle cell disease",
               "Only a girl could inherit it"],
   "answer": "B",
   "explain": "SS requires one sickle gene from each parent. Two carriers can therefore have an affected child — which is why knowing your status before starting a family matters."},

  {"q": "Which are warning signs of diabetes? [SELECT ALL THAT APPLY]",
   "type": "msq",
   "options": ["Frequent urination",
               "Excessive thirst",
               "Yellowing of the whites of the eyes",
               "Unexplained weight loss",
               "Wounds that will not heal"],
   "answer": ["A", "B", "D", "E"],
   "explain": "Jaundice — yellowing of the eyes — is a sign of sickle cell disease, not diabetes."},

  {"q": "Why do about 17 Kenyan counties carry a high sickle cell burden?",
   "options": ["They have poorer diets",
               "They are in the lake and coastal regions where malaria is endemic",
               "They have less access to hospitals",
               "The climate is hotter there"],
   "answer": "B",
   "explain": "The high burden in those lake and coastal counties is linked to malaria endemicity in those areas."},

  {"q": "A peer says his aunt's sickle cell was caused by witchcraft. What is the best response?",
   "options": ["Tell him that is nonsense and continue the lesson",
               "Agree, to avoid offending his family",
               "Explain AA/AS/SS inheritance simply, without attacking the family",
               "Refer him to a religious leader"],
   "answer": "C",
   "explain": "Dismissing the belief closes the conversation. Explaining the genetics without blame leaves room for the real question — can I be tested?"},
 ],
}
