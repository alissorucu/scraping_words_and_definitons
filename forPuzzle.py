import time

import selenium.common.exceptions
from selenium import webdriver

driver = webdriver.Chrome()
words=[
"gathering",
"partial",
"imminent",
"solo",
"partially",
"compliance",
"proceeds",
"scope",
"plea",
"resignation",
"disposal",
"amend",
"sceptical",
"plead",
"dense",
"residue",
"profound",
"militant",
"humanitarian",
"assurance",
"beast",
"noon",
"density",
"license",
"subscriber",
"troubled",
"sacrifice",
"implementation",
"divine",
"adhere",
"clash",
"contend",
"mainstream",
"collision",
"bulk",
"peculiar",
"pledge",
"overturn",
"inequality",
"pad",
"deprive",
"sketch",
"substitute",
"gallon",
"bonus",
"oral",
"analogy",
"configuration",
"newsletter",
"prestigious",
"accountability",
"sensitivity",
"fatal",
"inclusion",
"consensus",
"overwhelming",
"ranking",
"circulate",
"pirate",
"heighten",
"aspiration",
"slam",
"affection",
"memo",
"hatred",
"long-time",
"curiosity",
"backup",
"whilst",
"missile",
"casino",
"congregation",
"buck",
"deem",
"conceal",
"tactic",
"statistical",
"inspect",
"copyright",
"specification",
"declaration",
"inclined",
"optical",
"tenant",
"ideology",
"escalate",
"preside",
"supreme",
"petition",
"influential",
"align",
"tremendous",
"non-profit",
"arbitrary",
"wipe",
"toll",
"stab",
"aggression",
"nursery",
"rotation",
"detention",
"verify",
"parameter",
"utterly",
"harmony",
"alert",
"incur",
"testify",
"tribute",
"stake",
"insider",
"ensue",
"substantially",
"legislative",
"magistrate",
"flawed",
"allowance",
"retrieve",
"massacre",
"flaw",
"bizarre",
"memorial",
"defensive",
"invoke",
"eager",
"naval",
"gambling",
"operational",
"solely",
"cutting",
"humble",
"casualty",
"portfolio",
"hydrogen",
"verse",
"forth",
"foreigner",
"neglect",
"theology",
"ironic",
"cognitive",
"spectrum",
"seize",
"warrant",
"accomplishment",
"enrol",
"notably",
"pastor",
"prominent",
"versus",
"surge",
"continually",
"morality",
"coordinator",
"displace",
"retreat",
"regime",
"craft",
"educator",
"execute",
"rehabilitation",
"horizon",
"handy",
"underlying",
"sensation",
"charter",
"allegation",
"combat",
"symbolic",
"condemn",
"bow",
"crystal",
"recount",
"inmate",
"probe",
"ratio",
"accessible",
"endless",
"interactive",
"encouragement",
"adoption",
"patrol",
"novel",
"accordingly",
"specimen",
"referendum",
"synthesis",
"guerrilla",
"endorse",
"burden",
"summit",
"reproduction",
"seemingly",
"kidney",
"earnings",
"correction",
"legacy",
"counselling",
"withdrawal",
"prescription",
"consciousness",
"striking",
"grief",
"coincide",
"confrontation",
"contradiction",
"manuscript",
"deteriorate",
"anchor",
"thought-provoking",
"recipient",
"medieval",
"top",
"competence",
"maintenance",
"surplus",
"enrich",
"turnout",
"contributor",
"vicious",
"commentator",
"hierarchy",
"province",
"contention",
"feminist",
"processing",
"superb",
"notorious",
"stimulus",
"expenditure",
"thrilled",
"dedicated",
"efficiency",
"delicate",
"abundance",
"spark",
"embarrassment",
"dispose",
"diagnose",
"postpone",
"widow",
"faculty",
"intellectual",
"conceive",
"commence",
"skip",
"spare",
"acceptance",
"appoint",
"slavery",
"coordinate",
"minimal",
"decisive",
"deficit",
"devil",
"rental",
"turnover",
"testimony",
"hopeful",
"landmark",
"hardware",
"intact",
"bureaucracy",
"contemplate",
"surgical",
"surveillance",
"activist",
"deposit",
"strand",
"dependence",
"representation",
"preliminary",
"veteran",
"alien",
"correlate",
"machinery",
"demon",
"fit",
"suspicion",
"liberation",
"indigenous",
"applicable",
"encompass",
"essence",
"deputy",
"clarity",
"harsh",
"abuse",
"supplement",
"attorney",
"disturbing",
"inadequate",
"allegedly",
"accumulate",
"desirable",
"mercy",
"discharge",
"refuge",
"infect",
"large-scale",
"stun",
"cautious",
"portray",
"adverse",
"tactical",
"cooperate",
"constitutional",
"mandate",
"plunge",
"momentum",
"asylum",
"justification",
"initiate",
"flourish",
"harassment",
"rejection",
"jurisdiction",
"accountable",
"endeavour",
"regardless",
"cabinet",
"overwhelm",
"fierce",
"melody",
"defy",
"interior",
"comply",
"dynamic",
"sheer",
"kidnap",
"obsession",
"tenure",
"ecological",
"rebellion",
"productivity",
"linger",
"remains",
"investigator",
"exile",
"sanction",
"terminate",
"halfway",
"pole",
"endorsement",
"unprecedented",
"tolerate",
"proclaim",
"allocation",
"sexuality",
"namely",
"intervene",
"hail",
"appreciation",
"empirical",
"shed",
"just",
"post-war",
"constituency",
"adaptation",
"hostage",
"frankly",
"isolation",
"exclusively",
"confine",
"inhibit",
"methodology",
"regain",
"serial",
"philosopher",
"caution",
"gravity",
"odds",
"interfere",
"blast",
"net",
"compile",
"irrelevant",
"erect",
"compel",
"intriguing",
"warfare",
"minimize",
"strive",
"debris",
"protocol",
"authentic",
"inability",
"gaze",
"attain",
"assassination",
"senator",
"copper",
"liberty",
"adjacent",
"encouraging",
"outsider",
"carve",
"rod",
"stability",
"consecutive",
"sake",
"equality",
"doctrine",
"merchant",
"timber",
"creator",
"radar",
"dimension",
"suite",
"neighbouring",
"inspiration",
"cling",
"suspension",
"simultaneously",
"disclose",
"presumably",
"successor",
"handful",
"robust",
"trophy",
"quest",
"directory",
"worship",
"liver",
"exclusive",
"breed",
"intervention",
"aesthetic",
"confession",
"standing",
"duo",
"migration",
"psychiatric",
"spine",
"width",
"tackle",
"intimate",
"decision-making",
"counsellor",
"comparable",
"shatter",
"pond",
"trustee",
"devastate",
"destructive",
"feat",
"filter",
"wit",
"substantial",
"relevance",
"architectural",
"suck",
"deficiency",
"stereotype",
"governance",
"default",
"patent",
"apparatus",
"monopoly",
"humanity",
"transit",
"horn",
"eligible",
"intensify",
"distress",
"instruct",
"thereafter",
"scrutiny",
"breakdown",
"storage",
"reasoning",
"pit",
"delegation",
"corruption",
"intensity",
"parliamentary",
"rifle",
"atrocity",
"blade",
"toss",
"resemble",
"alignment",
"merit",
"tighten",
"presidential",
"councillor",
"terminal",
"notify",
"notable",
"mentor",
"productive",
"endure",
"residential",
"propaganda",
"accelerate",
"vanish",
"ignorance",
"diagnosis",
"contender",
"congressional",
"vacuum",
"offering",
"diminish",
"outbreak",
"privilege",
"prevail",
"premise",
"alliance",
"conception",
"reliability",
"remedy",
"disrupt",
"cattle",
"patron",
"snap",
"dose",
"imagery",
"pronounced",
"explosive",
"amid",
"junction",
"presume",
"unify",
"total",
"line-up",
"nominee",
"dedication",
"instinct",
"injection",
"straightforward",
"cluster",
"exit",
"audit",
"ironically",
"threshold",
"shrug",
"burst",
"workout",
"arguably",
"integration",
"arm",
"modification",
"niche",
"sue",
"worthwhile",
"taxpayer",
"consolidate",
"handling",
"magnetic",
"advocate",
"commodity",
"distinction",
"indictment",
"defect",
"ward",
"seldom",
"documentation",
"grip",
"lesbian",
"abolish",
"instrumental",
"indicator",
"say",
"exert",
"replacement",
"backing",
"orientation",
"residence",
"rumour",
"ballot",
"accused",
"dispute",
"firearm",
"interface",
"upgrade",
"await",
"flesh",
"thankfully",
"transformation",
"catalogue",
"guilt",
"broadband",
"latter",
"reproduce",
"outing",
"discrimination",
"well",
"offspring",
"judicial",
"chronic",
"transcript",
"albeit",
"subsidy",
"collective",
"supervisor",
"tolerance",
"segment",
"explicitly",
"municipal",
"pop",
"buffer",
"sword",
"conscience",
"administer",
"well-being",
"treaty",
"appetite",
"terrain",
"torture",
"prevalence",
"outrage",
"toxic",
"descend",
"ray",
"tender",
"mobility",
"amendment",
"supervise",
"concession",
"bass",
"boundary",
"manifest",
"idiot",
"processor",
"sole",
"uphold",
"likelihood",
"canvas",
"bounce",
"descent",
"commerce",
"tobacco",
"successive",
"prescribe",
"limb",
"objection",
"screw",
"driving",
"capability",
"constitute",
"poll",
"whip",
"realization",
"sound",
"correspondence",
"exclusion",
"characterize",
"compensation",
"theatrical",
"leak",
"predator",
"enterprise",
"slot",
"breakthrough",
"prosecution",
"crude",
"gut",
"ease",
"domain",
"respective",
"franchise",
"smash",
"alike",
"problematic",
"bind",
"fairness",
"timely",
"crown",
"rip",
"pregnancy",
"confer",
"superior",
"drain",
"suspicious",
"epidemic",
"nod",
"lobby",
"aftermath",
"lap",
"buddy",
"nationwide",
"motorist",
"cargo",
"content",
"intensive",
"effectiveness",
"anonymous",
"supposedly",
"administrative",
"separation",
"reign",
"hostility",
"imprison",
"vein",
"legislature",
"amateur",
"corresponding",
"desktop",
"breach",
"correspondent",
"saint",
"motive",
"confront",
"guidance",
"dignity",
"realm",
"collaborate",
"classification",
"gear",
"passing",
"nonsense",
"discretion",
"wholly",
"trailer",
"hostile",
"aide",
"span",
"fine",
"abortion",
"verdict",
"coastal",
"favourable",
"constraint",
"precision",
"competent",
"oversee",
"squad",
"beneath",
"prosperity",
"ideological",
"squeeze",
"glance",
"lad",
"march",
"dictate",
"involvement",
"revival",
"log",
"rotate",
"establishment",
"loom",
"twist",
"charm",
"premium",
"sovereignty",
"exaggerate",
"rally",
"meaningful",
"cemetery",
"trio",
"excess",
"coordination",
"citizenship",
"empower",
"provision",
"embed",
"strip",
"legendary",
"prey",
"oblige",
"simulate",
"discourse",
"render",
"philosophical",
"supportive",
"conviction",
"availability",
"insufficient",
"mathematical",
"critique",
"reflection",
"devise",
"yell",
"cater",
"soak",
"formula",
"dual",
"embody",
"revenge",
"quota",
"weave",
"respectively",
"vulnerability",
"socialist",
"dub",
"elaborate",
"strain",
"logic",
"marginal",
"detection",
"hazard",
"pipeline",
"disclosure",
"stir",
"interference",
"undermine",
"commissioner",
"debut",
"injustice",
"foster",
"coup",
"drift",
"equation",
"verbal",
"assert",
"aspire",
"strategic",
"bishop",
"indulge",
"counter",
"flee",
"shrink",
"lawn",
"nonetheless",
"complement",
"mature",
"suicide",
"assembly",
"appealing",
"ministry",
"glory",
"presently",
"selective",
"steer",
"reportedly",
"crawl",
"nest",
"communist",
"engaging",
"sustain",
"articulate",
"mob",
"transaction",
"heritage",
"spy",
"radical",
"merely",
"premier",
"rebel",
"rhetoric",
"regulatory",
"predominantly",
"merge",
"immense",
"prosecute",
"thrive",
"excellence",
"incidence",
"optimism",
"cop",
"long-standing",
"violation",
"misleading",
"mainland",
"bat",
"restraint",
"enthusiast",
"ritual",
"obsess",
"disastrous",
"capitalism",
"dismissal",
"correspond",
"mutual",
"enforcement",
"magical",
"mill",
"accumulation",
"subscription",
"listing",
"soar",
"assault",
"sentiment",
"funeral",
"explicit",
"tuition",
"punch",
"warehouse",
"induce",
"stumble",
"transparent",
"yield",
"adjustment",
"practitioner",
"confirmation",
"spectacle",
"reassure",
"admission",
"proposition",
"expire",
"willingness",
"meantime",
"youngster",
"structural",
"attendance",
"tribunal",
"unveil",
"shipping",
"vague",
"surrender",
"inappropriate",
"vow",
"inject",
"fixture",
"texture",
"opt",
"pump",
"glorious",
"undergraduate",
"mining",
"insertion",
"contrary",
"stark",
"misery",
"solidarity",
"personnel",
"worthy",
"frustration",
"landlord",
"moderate",
"rage",
"administrator",
"pathway",
"utility",
"collaboration",
"revelation",
"variable",
"thoughtful",
"fade",
"bay",
"mere",
"countless",
"literacy",
"tide",
"legislation",
"lesser",
"columnist",
"film-maker",
"genocide",
"swing",
"embark",
"riot",
"militia",
"arena",
"secular",
"maximize",
"chaos",
"lethal",
"damaging",
"detain",
"removal",
"parish",
"applaud",
"precedent",
"credible",
"infamous",
"rock",
"bench",
"overly",
"capitalist",
"preach",
"lawsuit",
"harvest",
"halt",
"occurrence",
"forthcoming",
"allege",
"fluid",
"ally",
"vibrant",
"republic",
"sigh",
"interim",
"whatever",
"mandatory",
"utilize",
"reform",
"stem",
"systematic",
"courtesy",
"cultivate",
"grasp",
"principal",
"reminder",
"simulation",
"constitution",
"institutional",
"concede",
"hook",
"monk",
"raid",
"distort",
"trigger",
"overlook",
"evacuate",
"consent",
"emergence",
"auto",
"frustrating",
"marketplace",
"angel",
"biography",
"blend",
"enact",
"pulse",
"seal",
"submission",
"lengthy",
"civic",
"dilemma",
"ash",
"meditation",
"betray",
"shoot",
"passive",
"venture",
"contempt",
"compassion",
"complication",
"linear",
"upcoming",
"plug",
"engagement",
"boast",
"benchmark",
"allocate",
"compute",
"composition",
"crush",
"fragile",
"grin",
"presidency",
"physician",
"conquer",
"barrel",
"patch",
"bleed",
"beneficiary",
"slash",
"vessel",
"solicitor",
"functional",
"congratulate",
"dip",
"grid",
"invisible",
"dumb",
"prospective",
"transmission",
"denial",
"peak",
"resistance",
"dissolve",
"occasional",
"exploitation",
"provoke",
"kingdom",
"trail",
"cynical",
"restoration",
"thread",
"mobilize",
"projection",
"grave",
"insult",
"subtle",
"memoir",
"ruling",
"legitimate",
"consultation",
"high-profile",
"specialized",
"banner",
"vulnerable",
"flexibility",
"outlet",
"denounce",
"revolutionary",
"delegate",
"chamber",
"discard",
"academy",
"eternal",
"predecessor",
"prevention",
"virtue",
"irony",
"gross",
"embassy",
"archive",
"counterpart",
"companion",
"identification",
"attribute",
"burial",
"fate",
"acre",
"theoretical",
"sin",
"exceptional",
"compromise",
"array",
"fleet",
"reverse",
"set-up",
"ambassador",
"intermediate",
"sacred",
"blessing",
"miracle",
"formulate",
"trauma",
"differentiate",
"validity",
"acid",
"succession",
"viable",
"accordance",
"glimpse",
"provincial",
"trademark",
"stabilize",
"backdrop",
"profitable",
"creep",
"slap",
"consistency",
"liberal",
"acquisition",
"peasant",
"extract",
"cease",
"generic",
"entity",
"suppress",
"imprisonment",
"readily",
"absurd",
"warrior",
"enquire",
"dawn",
"activation",
"dam",
"terrific",
"convict",
"spouse",
"trace",
"spam",
"cult",
"grind",
"ego",
"sphere",
"conserve",
"compelling",
"shareholder",
"renew",
"inspection",
"dominance",
"midst",
"frustrated",
"organizational",
"elite",
"cocktail",
"extremist",
"tribal",
"aluminium",
"brutal",
"compensate",
"assertion",
"whatsoever",
"privatization",
"experimental",
"persist",
"intent",
"authorize",
"integrity",
"autonomy",
"loyalty",
"evoke",
"beam",
"revive",
"integral",
"reconstruction",
"originate",
"conversion",
"boom",
"situated",
"designate",
"lifelong",
"divert",
"substitution",
"corrupt",
"assemble",
"absent",
"proceeding",
"execution",
"protective",
"colonial",
"echo",
"magnitude",
"tempt",
"preservation",
"correlation",
"browser",
"renowned",
"layout",
"regulator",
"drown",
"vice",
"marine",
"mask",
"civilian",
"credibility",
"leap",
"inflict",
"settlement",
"merger",
"refusal",
"whereby",
"integrated",
"pioneer",
"dictator",
"resume",
"noble",
"intake",
"entitle",
"acute",
"homeland",
"bless",
"infant",
"agricultural",
"beloved",
"varied",
"bail",
"parental",
"villager",
"persistent",
"circulation",
"thereby",
"costly",
"prejudice",
"liable",
"diplomatic",
"behalf",
"cooperative",
"manipulation",
"clinical",
"syndrome",
"inherent",
"deed",
"spotlight",
"violate",
"widen",
"absence",
"carriage",
"bare",
"spin",
"calculation",
"donor",
"query",
"manipulate",
"laser",
"adolescent",
"prosecutor",
"rear",
"outlook",
"footage",
"facilitate",
"reluctant",
"supervision",
"commentary",
"complexity",
"distinctive",
"spell",
"vocal",
"hint",
"nomination",
"suburban",
"coalition",
"transparency",
"elevate",
"fibre",
"electoral",
"battlefield",
"weaken",
"weed",
"evolutionary",
"contractor",
"faction",
"rape",
"sack",
"undoubtedly",
"minute",
"enforce",
"forge",
"haunt",
"depict",
"custody",
"scattered",
"deploy",
"accusation",
"diplomat",
"disruption",
"deployment",
"chunk",
"reside",
"closure",
"loop",
"fundraising",
"remainder",
"grace",
"triumph",
"rational",
"nominate",
]


def scrapQuestions(words):

    for i in range(len(words)):

        if len(words[i]) <4:
            continue

        driver.get(f"https://translate.google.com/?hl=tr&sl=en&tl=tr&text={words[i]}&op=translate")
        time.sleep(0.4)

        try:
            definition = driver.find_element_by_class_name('fw3eif').text
        except selenium.common.exceptions.NoSuchElementException:
            continue



        print(f'Question("{words[i]}","{definition}"),')



def tryyy(words):
    for i in range(len(words)):

        driver.get(f"https://ssl.gstatic.com/dictionary/static/sounds/20200429/{words[i]}--_gb_1.mp3")
        time.sleep(0.3)

scrapQuestions(words)
#tryyy(words)

