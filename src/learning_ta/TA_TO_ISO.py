# Ref: https://en.wikipedia.org/wiki/Tamil_script
TA_TO_ISO = {
    "அ": "a",
    "ஆ": "ā",
    "இ": "i",
    "ஈ": "ī",
    "உ": "u",
    "ஊ": "ū",
    "எ": "e",
    "ஏ": "ē",
    "ஐ": "ai",
    "ஒ": "o",
    "ஓ": "ō",
    "ஔ": "au",
    "க": "ka",
    "கா": "kā",
    "கி": "ki",
    "கீ": "kī",
    "கு": "ku",
    "கூ": "kū",
    "கெ": "ke",
    "கே": "kē",
    "கை": "kai",
    "கொ": "ko",
    "கோ": "kō",
    "கௌ": "kau",
    "க்": "k",
    "ங": "ṅa",
    "ஙா": "ṅā",
    "ஙி": "ṅi",
    "ஙீ": "ṅī",
    "ஙு": "ṅu",
    "ஙூ": "ṅū",
    "ஙெ": "ṅe",
    "ஙே": "ṅē",
    "ஙை": "ṅai",
    "ஙொ": "ṅo",
    "ஙோ": "ṅō",
    "ஙௌ": "ṅau",
    "ங்": "ṅ",
    "ச": "ca",
    "சா": "cā",
    "சி": "ci",
    "சீ": "cī",
    "சு": "cu",
    "சூ": "cū",
    "செ": "ce",
    "சே": "cē",
    "சை": "cai",
    "சொ": "co",
    "சோ": "cō",
    "சௌ": "cau",
    "ச்": "c",
    "ஞ": "ña",
    "ஞா": "ñā",
    "ஞி": "ñi",
    "ஞீ": "ñī",
    "ஞு": "ñu",
    "ஞூ": "ñū",
    "ஞெ": "ñe",
    "ஞே": "ñē",
    "ஞை": "ñai",
    "ஞொ": "ño",
    "ஞோ": "ñō",
    "ஞௌ": "ñau",
    "ஞ்": "ñ",
    "ட": "ṭa",
    "டா": "ṭā",
    "டி": "ṭi",
    "டீ": "ṭī",
    "டு": "ṭu",
    "டூ": "ṭū",
    "டெ": "ṭe",
    "டே": "ṭē",
    "டை": "ṭai",
    "டொ": "ṭo",
    "டோ": "ṭō",
    "டௌ": "ṭau",
    "ட்": "ṭ",
    "ண": "ṇa",
    "ணா": "ṇā",
    "ணி": "ṇi",
    "ணீ": "ṇī",
    "ணு": "ṇu",
    "ணூ": "ṇū",
    "ணெ": "ṇe",
    "ணே": "ṇē",
    "ணை": "ṇai",
    "ணொ": "ṇo",
    "ணோ": "ṇō",
    "ணௌ": "ṇau",
    "ண்": "ṇ",
    "த": "ta",
    "தா": "tā",
    "தி": "ti",
    "தீ": "tī",
    "து": "tu",
    "தூ": "tū",
    "தெ": "te",
    "தே": "tē",
    "தை": "tai",
    "தொ": "to",
    "தோ": "tō",
    "தௌ": "tau",
    "த்": "t",
    "ந": "na",
    "நா": "nā",
    "நி": "ni",
    "நீ": "nī",
    "நு": "nu",
    "நூ": "nū",
    "நெ": "ne",
    "நே": "nē",
    "நை": "nai",
    "நொ": "no",
    "நோ": "nō",
    "நௌ": "nau",
    "ந்": "n",
    "ப": "pa",
    "பா": "pā",
    "பி": "pi",
    "பீ": "pī",
    "பு": "pu",
    "பூ": "pū",
    "பெ": "pe",
    "பே": "pē",
    "பை": "pai",
    "பொ": "po",
    "போ": "pō",
    "பௌ": "pau",
    "ப்": "p",
    "ம": "ma",
    "மா": "mā",
    "மி": "mi",
    "மீ": "mī",
    "மு": "mu",
    "மூ": "mū",
    "மெ": "me",
    "மே": "mē",
    "மை": "mai",
    "மொ": "mo",
    "மோ": "mō",
    "மௌ": "mau",
    "ம்": "m",
    "ய": "ya",
    "யா": "yā",
    "யி": "yi",
    "யீ": "yī",
    "யு": "yu",
    "யூ": "yū",
    "யெ": "ye",
    "யே": "yē",
    "யை": "yai",
    "யொ": "yo",
    "யோ": "yō",
    "யௌ": "yau",
    "ய்": "y",
    "ர": "ra",
    "ரா": "rā",
    "ரி": "ri",
    "ரீ": "rī",
    "ரு": "ru",
    "ரூ": "rū",
    "ரெ": "re",
    "ரே": "rē",
    "ரை": "rai",
    "ரொ": "ro",
    "ரோ": "rō",
    "ரௌ": "rau",
    "ர்": "r",
    "ல": "la",
    "லா": "lā",
    "லி": "li",
    "லீ": "lī",
    "லு": "lu",
    "லூ": "lū",
    "லெ": "le",
    "லே": "lē",
    "லை": "lai",
    "லொ": "lo",
    "லோ": "lō",
    "லௌ": "lau",
    "ல்": "l",
    "வ": "va",
    "வா": "vā",
    "வி": "vi",
    "வீ": "vī",
    "வு": "vu",
    "வூ": "vū",
    "வெ": "ve",
    "வே": "vē",
    "வை": "vai",
    "வொ": "vo",
    "வோ": "vō",
    "வௌ": "vau",
    "வ்": "v",
    "ழ": "ḻa",
    "ழா": "ḻā",
    "ழி": "ḻi",
    "ழீ": "ḻī",
    "ழு": "ḻu",
    "ழூ": "ḻū",
    "ழெ": "ḻe",
    "ழே": "ḻē",
    "ழை": "ḻai",
    "ழொ": "ḻo",
    "ழோ": "ḻō",
    "ழௌ": "ḻau",
    "ழ்": "ḻ",
    "ள": "ḷa",
    "ளா": "ḷā",
    "ளி": "ḷi",
    "ளீ": "ḷī",
    "ளு": "ḷu",
    "ளூ": "ḷū",
    "ளெ": "ḷe",
    "ளே": "ḷē",
    "ளை": "ḷai",
    "ளொ": "ḷo",
    "ளோ": "ḷō",
    "ளௌ": "ḷau",
    "ள்": "ḷ",
    "ற": "ṟa",
    "றா": "ṟā",
    "றி": "ṟi",
    "றீ": "ṟī",
    "று": "ṟu",
    "றூ": "ṟū",
    "றெ": "ṟe",
    "றே": "ṟē",
    "றை": "ṟai",
    "றொ": "ṟo",
    "றோ": "ṟō",
    "றௌ": "ṟau",
    "ற்": "ṟ",
    "ன": "ṉa",
    "னா": "ṉā",
    "னி": "ṉi",
    "னீ": "ṉī",
    "னு": "ṉu",
    "னூ": "ṉū",
    "னெ": "ṉe",
    "னே": "ṉē",
    "னை": "ṉai",
    "னொ": "ṉo",
    "னோ": "ṉō",
    "னௌ": "ṉau",
    "ன்": "ṉ",
    "ஜ": "ja",
    "ஜா": "jā",
    "ஜி": "ji",
    "ஜீ": "jī",
    "ஜு": "ju",
    "ஜூ": "jū",
    "ஜெ": "je",
    "ஜே": "jē",
    "ஜை": "jai",
    "ஜொ": "jo",
    "ஜோ": "jō",
    "ஜௌ": "jau",
    "ஜ்": "j",
    "ஷ": "sha",
    "ஷா": "shā",
    "ஷி": "shi",
    "ஷீ": "shī",
    "ஷு": "shu",
    "ஷூ": "shū",
    "ஷெ": "she",
    "ஷே": "shē",
    "ஷை": "shai",
    "ஷொ": "sho",
    "ஷோ": "shō",
    "ஷௌ": "shau",
    "ஷ்": "sh",
    "ஸ": "sa",
    "ஸா": "sā",
    "ஸி": "si",
    "ஸீ": "sī",
    "ஸு": "su",
    "ஸூ": "sū",
    "ஸெ": "se",
    "ஸே": "sē",
    "ஸை": "sai",
    "ஸொ": "so",
    "ஸோ": "sō",
    "ஸௌ": "sau",
    "ஸ்": "s",
    "ஹ": "ha",
    "ஹா": "hā",
    "ஹி": "hi",
    "ஹீ": "hī",
    "ஹு": "hu",
    "ஹூ": "hū",
    "ஹெ": "he",
    "ஹே": "hē",
    "ஹை": "hai",
    "ஹொ": "ho",
    "ஹோ": "hō",
    "ஹௌ": "hau",
    "ஹ்": "h",
    "க்ஷ": "ksha",
    "க்ஷா": "kshā",
    "க்ஷி": "kshi",
    "க்ஷீ": "kshī",
    "க்ஷு": "kshu",
    "க்ஷூ": "kshū",
    "க்ஷெ": "kshe",
    "க்ஷே": "kshē",
    "க்ஷை": "kshai",
    "க்ஷொ": "ksho",
    "க்ஷோ": "kshō",
    "க்ஷௌ": "kshau",
    "க்ஷ்": "ksh",
    "ஃ": "akh",
    "்": "",  # Adding the missing transliteration for "்"
}