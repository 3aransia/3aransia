"""This file contains all poject defaults and constants"""

from collections import OrderedDict

# Project directories
BASE_DIR = './aaransia'
DATA_DIR = '/data'
LOG_DIR = '/log'

# Data sets
ALPHABET_FILE = '/alphabet.csv'
DICTIONARY_FILE = '/dictionary.csv'

# Test logs files
TEST_TRANSLITERATION_LOG_FILE = '/test_transliteration.log'

# Loggers
TEST_LOGGER_NAME = 'test_logger'

# Alphabet codes
ARABIC_ALPHABET_CODE = 'ar'
AFRIKAANS_ALPHABET_CODE = 'af'
ALBANIAN_ALPHABET_CODE = 'sq'
ALGERIAN_ALPHABET_CODE = 'al'
AZERBAIJANI_ALPHABET_CODE = 'az'
BASQUE_ALPHABET_CODE = 'eu'
BOSNIAN_ALPHABET_CODE = 'bo'
CATALAN_ALPHABET_CODE = 'ca'
CORSICAN_ALPHABET_CODE = 'co'
CROATIAN_ALPHABET_CODE = 'hr'
CZECH_ALPHABET_CODE = 'cs'
DANISH_ALPHABET_CODE = 'da'
DUTCH_ALPHABET_CODE = 'nl'
ENGLISH_ALPHABET_CODE = 'en'
ESPERANTO_ALPHABET_CODE = 'eo'
ESTONIAN_ALPHABET_CODE = 'et'
FILIPINO_ALPHABET_CODE = 'tl'
FINNISH_ALPHABET_CODE = 'fi'
FRENCH_ALPHABET_CODE = 'fr'
FRISIAN_ALPHABET_CODE = 'fs'
GALICIAN_ALPHABET_CODE = 'gl'
GERMAN_ALPHABET_CODE = 'de'
CREOLE_ALPHABET_CODE = 'ht'
HAUSA_ALPHABET_CODE = 'ha'
HAWAIIAN_ALPHABET_CODE = 'hw'
HUNGARIAN_ALPHABET_CODE = 'hu'
ICELANDIC_ALPHABET_CODE = 'is'
IGBO_ALPHABET_CODE = 'ig'
INDONESIAN_ALPHABET_CODE = 'id'
IRISH_ALPHABET_CODE = 'ga'
ITALIAN_ALPHABET_CODE = 'it'
KINYARWANDA_ALPHABET_CODE = 'ki'
KURDISH_ALPHABET_CODE = 'ku'
LATIN_ALPHABET_CODE = 'la'
LATVIAN_ALPHABET_CODE = 'lv'
LIBYAN_ALPHABET_CODE = 'li'
LITHUANIAN_ALPHABET_CODE = 'lt'
LUXEMBOURGISH_ALPHABET_CODE = 'lu'
MOROCCAN_ALPHABET_CODE = 'ma'
MALAGASY_ALPHABET_CODE = 'mg'
MALAY_ALPHABET_CODE = 'ms'
MALTESE_ALPHABET_CODE = 'mt'
MAORI_ALPHABET_CODE = 'mo'
NORWEGIAN_ALPHABET_CODE = 'no'
POLISH_ALPHABET_CODE = 'pl'
PORTUGUESE_ALPHABET_CODE = 'pt'
ROMANIAN_ALPHABET_CODE = 'ro'
SAMOAN_ALPHABET_CODE = 'sa'
GAELIC_ALPHABET_CODE = 'gc'
GREEK_ALPHABET_CODE = 'el'
SESOTHO_ALPHABET_CODE = 'ss'
SHONA_ALPHABET_CODE = 'sh'
SLOVAK_ALPHABET_CODE = 'sk'
SLOVENIAN_ALPHABET_CODE = 'sl'
SOMALI_ALPHABET_CODE = 'so'
SPANISH_ALPHABET_CODE = 'es'
SUNDANESE_ALPHABET_CODE = 'su'
SWAHILI_ALPHABET_CODE = 'sw'
SWEDISH_ALPHABET_CODE = 'sv'
TUNISIAN_ALPHABET_CODE = 'tn'
TURKISH_ALPHABET_CODE = 'tr'
TURKMEN_ALPHABET_CODE = 'tu'
UZBEK_ALPHABET_CODE = 'uz'
VIETNAMESE_ALPHABET_CODE = 'vi'
WELSH_ALPHABET_CODE = 'cy'
XHOSA_ALPHABET_CODE = 'xh'
YORUBA_ALPHABET_CODE = 'yo'
ZULU_ALPHABET_CODE = 'zu'
PERSIAN_ALPHABET_CODE = 'fa'
URDU_ALPHABET_CODE = 'ur'

# Alphabet Names
ARABIC_ALPHABET_NAME = 'Arabic Alphabet'
AFRIKAANS_ALPHABET_NAME = 'Afrikaans Alphabet'
ALBANIAN_ALPHABET_NAME = 'Albanian Alphabet'
ALGERIAN_ALPHABET_NAME = 'Algerian Alphabet'
AZERBAIJANI_ALPHABET_NAME = 'Azerbaijani Alphabet'
BASQUE_ALPHABET_NAME = 'Basque Alphabet'
BOSNIAN_ALPHABET_NAME = 'Bosnian Alphabet'
CATALAN_ALPHABET_NAME = 'Catalan Alphabet'
CORSICAN_ALPHABET_NAME = 'Corsican Alphabet'
CROATIAN_ALPHABET_NAME = 'Croatian Alphabet'
CZECH_ALPHABET_NAME = 'Czech Alphabet'
DANISH_ALPHABET_NAME = 'Danish Alphabet'
DUTCH_ALPHABET_NAME = 'Dutch Alphabet'
ENGLISH_ALPHABET_NAME = 'English Alphabet'
ESPERANTO_ALPHABET_NAME = 'Esperanto Alphabet'
ESTONIAN_ALPHABET_NAME = 'Estonian Alphabet'
FILIPINO_ALPHABET_NAME = 'Filipino Alphabet'
FINNISH_ALPHABET_NAME = 'Finnish Alphabet'
FRENCH_ALPHABET_NAME = 'French Alphabet'
FRISIAN_ALPHABET_NAME = 'Frisian Alphabet'
GALICIAN_ALPHABET_NAME = 'Galician Alphabet'
GERMAN_ALPHABET_NAME = 'German Alphabet'
CREOLE_ALPHABET_NAME = 'Creole Alphabet'
HAUSA_ALPHABET_NAME = 'Hausa Alphabet'
HAWAIIAN_ALPHABET_NAME = 'Hawaiian Alphabet'
HUNGARIAN_ALPHABET_NAME = 'Hungarian Alphabet'
ICELANDIC_ALPHABET_NAME = 'Icelandic Alphabet'
IGBO_ALPHABET_NAME = 'Igbo Alphabet'
INDONESIAN_ALPHABET_NAME = 'Indonesian Alphabet'
IRISH_ALPHABET_NAME = 'Irish Alphabet'
ITALIAN_ALPHABET_NAME = 'Italian Alphabet'
KINYARWANDA_ALPHABET_NAME = 'Kinyarwanda Alphabet'
KURDISH_ALPHABET_NAME = 'Kurdish Alphabet'
LATIN_ALPHABET_NAME = 'Latin Alphabet'
LATVIAN_ALPHABET_NAME = 'Latvian Alphabet'
LIBYAN_ALPHABET_NAME = 'Libyan Alphabet'
LITHUANIAN_ALPHABET_NAME = 'Lithuanian Alphabet'
LUXEMBOURGISH_ALPHABET_NAME = 'Luxembourgish Alphabet'
MOROCCAN_ALPHABET_NAME = 'Moroccan Alphabet'
MALAGASY_ALPHABET_NAME = 'Malagasy Alphabet'
MALAY_ALPHABET_NAME = 'Malay Alphabet'
MALTESE_ALPHABET_NAME = 'Maltese Alphabet'
MAORI_ALPHABET_NAME = 'Maori Alphabet'
NORWEGIAN_ALPHABET_NAME = 'Norwegian Alphabet'
POLISH_ALPHABET_NAME = 'Polish Alphabet'
PORTUGUESE_ALPHABET_NAME = 'Portuguese Alphabet'
ROMANIAN_ALPHABET_NAME = 'Romanian Alphabet'
SAMOAN_ALPHABET_NAME = 'Samoan Alphabet'
GAELIC_ALPHABET_NAME = 'Gaelic Alphabet'
GREEK_ALPHABET_NAME = 'Greek Alphabet'
SESOTHO_ALPHABET_NAME = 'Sesotho Alphabet'
SHONA_ALPHABET_NAME = 'Shona Alphabet'
SLOVAK_ALPHABET_NAME = 'Slovak Alphabet'
SLOVENIAN_ALPHABET_NAME = 'Slovenian Alphabet'
SOMALI_ALPHABET_NAME = 'Somali Alphabet'
SPANISH_ALPHABET_NAME = 'Spanish Alphabet'
SUNDANESE_ALPHABET_NAME = 'Sundanese Alphabet'
SWAHILI_ALPHABET_NAME = 'Swahili Alphabet'
SWEDISH_ALPHABET_NAME = 'Swedish Alphabet'
TUNISIAN_ALPHABET_NAME = 'Tunisian Alphabet'
TURKISH_ALPHABET_NAME = 'Turkish Alphabet'
TURKMEN_ALPHABET_NAME = 'Turkmen Alphabet'
UZBEK_ALPHABET_NAME = 'Uzbek Alphabet'
VIETNAMESE_ALPHABET_NAME = 'Vietnamese Alphabet'
WELSH_ALPHABET_NAME = 'Welsh Alphabet'
XHOSA_ALPHABET_NAME = 'Xhosa Alphabet'
YORUBA_ALPHABET_NAME = 'Yoruba Alphabet'
ZULU_ALPHABET_NAME = 'Zulu Alphabet'
PERSIAN_ALPHABET_NAME = 'Persian Alphabet'
URDU_ALPHABET_NAME = 'Urdu Alphabet'

# Alphabets
ALPHABETS = {
    ARABIC_ALPHABET_CODE: ARABIC_ALPHABET_NAME,
    AFRIKAANS_ALPHABET_CODE: AFRIKAANS_ALPHABET_NAME,
    ALBANIAN_ALPHABET_CODE: ALBANIAN_ALPHABET_NAME,
    ALGERIAN_ALPHABET_CODE: ALGERIAN_ALPHABET_NAME,
    AZERBAIJANI_ALPHABET_CODE: AZERBAIJANI_ALPHABET_NAME,
    BASQUE_ALPHABET_CODE: BASQUE_ALPHABET_NAME,
    BOSNIAN_ALPHABET_CODE: BOSNIAN_ALPHABET_NAME,
    CATALAN_ALPHABET_CODE: CATALAN_ALPHABET_NAME,
    CORSICAN_ALPHABET_CODE: CORSICAN_ALPHABET_NAME,
    CROATIAN_ALPHABET_CODE: CROATIAN_ALPHABET_NAME,
    CZECH_ALPHABET_CODE: CZECH_ALPHABET_NAME,
    DANISH_ALPHABET_CODE: DANISH_ALPHABET_NAME,
    DUTCH_ALPHABET_CODE: DUTCH_ALPHABET_NAME,
    ENGLISH_ALPHABET_CODE: ENGLISH_ALPHABET_NAME,
    ESPERANTO_ALPHABET_CODE: ESPERANTO_ALPHABET_NAME,
    ESTONIAN_ALPHABET_CODE: ESTONIAN_ALPHABET_NAME,
    FILIPINO_ALPHABET_CODE: FILIPINO_ALPHABET_NAME,
    FINNISH_ALPHABET_CODE: FINNISH_ALPHABET_NAME,
    FRENCH_ALPHABET_CODE: FRENCH_ALPHABET_NAME,
    FRISIAN_ALPHABET_CODE: FRISIAN_ALPHABET_NAME,
    GALICIAN_ALPHABET_CODE: GALICIAN_ALPHABET_NAME,
    GERMAN_ALPHABET_CODE: GERMAN_ALPHABET_NAME,
    CREOLE_ALPHABET_CODE: CREOLE_ALPHABET_NAME,
    HAUSA_ALPHABET_CODE: HAUSA_ALPHABET_NAME,
    HAWAIIAN_ALPHABET_CODE: HAWAIIAN_ALPHABET_NAME,
    HUNGARIAN_ALPHABET_CODE: HUNGARIAN_ALPHABET_NAME,
    ICELANDIC_ALPHABET_CODE: ICELANDIC_ALPHABET_NAME,
    IGBO_ALPHABET_CODE: IGBO_ALPHABET_NAME,
    INDONESIAN_ALPHABET_CODE: INDONESIAN_ALPHABET_NAME,
    IRISH_ALPHABET_CODE: IRISH_ALPHABET_NAME,
    ITALIAN_ALPHABET_CODE: ITALIAN_ALPHABET_NAME,
    KINYARWANDA_ALPHABET_CODE: KINYARWANDA_ALPHABET_NAME,
    KURDISH_ALPHABET_CODE: KURDISH_ALPHABET_NAME,
    LATIN_ALPHABET_CODE: LATIN_ALPHABET_NAME,
    LATVIAN_ALPHABET_CODE: LATVIAN_ALPHABET_NAME,
    LIBYAN_ALPHABET_CODE: LIBYAN_ALPHABET_NAME,
    LITHUANIAN_ALPHABET_CODE: LITHUANIAN_ALPHABET_NAME,
    LUXEMBOURGISH_ALPHABET_CODE: LUXEMBOURGISH_ALPHABET_NAME,
    MOROCCAN_ALPHABET_CODE: MOROCCAN_ALPHABET_NAME,
    MALAGASY_ALPHABET_CODE: MALAGASY_ALPHABET_NAME,
    MALAY_ALPHABET_CODE: MALAY_ALPHABET_NAME,
    MALTESE_ALPHABET_CODE: MALTESE_ALPHABET_NAME,
    MAORI_ALPHABET_CODE: MAORI_ALPHABET_NAME,
    NORWEGIAN_ALPHABET_CODE: NORWEGIAN_ALPHABET_NAME,
    POLISH_ALPHABET_CODE: POLISH_ALPHABET_NAME,
    PORTUGUESE_ALPHABET_CODE: PORTUGUESE_ALPHABET_NAME,
    ROMANIAN_ALPHABET_CODE: ROMANIAN_ALPHABET_NAME,
    SAMOAN_ALPHABET_CODE: SAMOAN_ALPHABET_NAME,
    GAELIC_ALPHABET_CODE: GAELIC_ALPHABET_NAME,
    GREEK_ALPHABET_CODE: GREEK_ALPHABET_NAME,
    SESOTHO_ALPHABET_CODE: SESOTHO_ALPHABET_NAME,
    SHONA_ALPHABET_CODE: SHONA_ALPHABET_NAME,
    SLOVAK_ALPHABET_CODE: SLOVAK_ALPHABET_NAME,
    SLOVENIAN_ALPHABET_CODE: SLOVENIAN_ALPHABET_NAME,
    SOMALI_ALPHABET_CODE: SOMALI_ALPHABET_NAME,
    SPANISH_ALPHABET_CODE: SPANISH_ALPHABET_NAME,
    SUNDANESE_ALPHABET_CODE: SUNDANESE_ALPHABET_NAME,
    SWAHILI_ALPHABET_CODE: SWAHILI_ALPHABET_NAME,
    SWEDISH_ALPHABET_CODE: SWEDISH_ALPHABET_NAME,
    TUNISIAN_ALPHABET_CODE: TUNISIAN_ALPHABET_NAME,
    TURKISH_ALPHABET_CODE: TURKISH_ALPHABET_NAME,
    TURKMEN_ALPHABET_CODE: TURKMEN_ALPHABET_NAME,
    UZBEK_ALPHABET_CODE: UZBEK_ALPHABET_NAME,
    VIETNAMESE_ALPHABET_CODE: VIETNAMESE_ALPHABET_NAME,
    WELSH_ALPHABET_CODE: WELSH_ALPHABET_NAME,
    XHOSA_ALPHABET_CODE: XHOSA_ALPHABET_NAME,
    YORUBA_ALPHABET_CODE: YORUBA_ALPHABET_NAME,
    ZULU_ALPHABET_CODE: ZULU_ALPHABET_NAME,
    PERSIAN_ALPHABET_CODE: PERSIAN_ALPHABET_NAME,
    URDU_ALPHABET_CODE: URDU_ALPHABET_NAME,
}

# Language count
LEN_LANGUAGES = len(ALPHABETS)

# Double Letters
DOUBLE_LETTERS = {
    ARABIC_ALPHABET_CODE: ['كز', 'كس'],
    URDU_ALPHABET_CODE: ['كز', 'كس'],
    PERSIAN_ALPHABET_CODE: ['كز', 'كس'],
    GREEK_ALPHABET_CODE: ['μπ', 'λα', 'oυ'],
    AFRIKAANS_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ALBANIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ALGERIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    AZERBAIJANI_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    BASQUE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    BOSNIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    CATALAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    CORSICAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    CROATIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    CZECH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    DANISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    DUTCH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ENGLISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ESPERANTO_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ESTONIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    FILIPINO_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    FINNISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    FRENCH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    FRISIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    GALICIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    GERMAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    CREOLE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    HAUSA_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    HAWAIIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    HUNGARIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ICELANDIC_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    IGBO_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    INDONESIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    IRISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ITALIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    KINYARWANDA_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    KURDISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    LATIN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    LATVIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    LIBYAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    LITHUANIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    LUXEMBOURGISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    MOROCCAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    MALAGASY_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    MALAY_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    MALTESE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    MAORI_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    NORWEGIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    POLISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    PORTUGUESE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ROMANIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SAMOAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    GAELIC_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    GREEK_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SESOTHO_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SHONA_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SLOVAK_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SLOVENIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SOMALI_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SPANISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SUNDANESE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SWAHILI_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    SWEDISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    TUNISIAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    TURKISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    TURKMEN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    UZBEK_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    VIETNAMESE_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    WELSH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    XHOSA_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    YORUBA_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ZULU_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
}

# Exceptions
SOURCE_LANGUAGE_EXCEPTION_MESSAGE = "Source alphabet language doesn't match the input text"

# Special characters
SPECIAL_CHARACTERS = '[@_!#$%^&*()<>/\|}{~:].;@$-+=`\'"'
