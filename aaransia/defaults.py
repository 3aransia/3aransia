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
TEST_STATS_LOG_FILE = '/test_stats.log'
TEST_TRANSLITERATION_LOG_FILE = '/test_transliteration.log'

# Loggers
TEST_STATS_LOGGER_NAME = 'test_stats_logger'
TEST_LOGGER_NAME = 'test_logger'

# Alphabet codes
MOROCCAN_ALPHABET_CODE = 'ma'
ARABIC_ALPHABET_CODE = 'ar'
ENGLISH_ALPHABET_CODE = 'en'
GREEK_ALPHABET_CODE = 'gr'

ALPHABET_CODE_LIST = [
    MOROCCAN_ALPHABET_CODE, ARABIC_ALPHABET_CODE, ENGLISH_ALPHABET_CODE,
    GREEK_ALPHABET_CODE
]

# Alphabets
MOROCCAN_ALPHABET_NAME = 'Moroccan Alphabet'
ARABIC_ALPHABET_NAME = 'Arabic Alphabet'
ENGLISH_ALPHABET_NAME = 'English Alphabet'
GREEK_ALPHABET_NAME = 'Greek Alphabet'

ALPHABET_NAMES_LIST = [
    MOROCCAN_ALPHABET_NAME, ARABIC_ALPHABET_NAME, ENGLISH_ALPHABET_NAME,
    GREEK_ALPHABET_NAME
]

# Language list
ALPHABETS = {
    ALPHABET_CODE_LIST[0]: ALPHABET_NAMES_LIST[0],
    ALPHABET_CODE_LIST[1]: ALPHABET_NAMES_LIST[1],
    ALPHABET_CODE_LIST[2]: ALPHABET_NAMES_LIST[2],
    ALPHABET_CODE_LIST[3]: ALPHABET_NAMES_LIST[3],
}

# Language count
LEN_LANGUAGES = len(ALPHABETS)

# Double Letters
DOUBLE_LETTERS = {
    MOROCCAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ARABIC_ALPHABET_CODE: ['كز', 'كس'],
    ENGLISH_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    GREEK_ALPHABET_CODE: ['μπ', 'λα', 'oυ']
}

# Exceptions
SOURCE_LANGUAGE_EXCEPTION_MESSAGE = "Source alphabet language doesn't match the input text"

# Special characters
SPECIAL_CHARACTERS = '[@_!#$%^&*()<>/\|}{~:].;@$-+=`\'"'

# The Alphabet
ALPHABET = [OrderedDict([('Moroccan Alphabet', ','),
              ('Arabic Alphabet', '،'),
              ('English Alphabet', ','),
              ('Greek Alphabet', ',')]),
 OrderedDict([('Moroccan Alphabet', '?'),
              ('Arabic Alphabet', '؟'),
              ('English Alphabet', '?'),
              ('Greek Alphabet', '?')]),
 OrderedDict([('Moroccan Alphabet', 'a'),
              ('Arabic Alphabet', 'ا'),
              ('English Alphabet', 'a'),
              ('Greek Alphabet', 'α')]),
 OrderedDict([('Moroccan Alphabet', 'b'),
              ('Arabic Alphabet', 'ب'),
              ('English Alphabet', 'b'),
              ('Greek Alphabet', 'μπ')]),
 OrderedDict([('Moroccan Alphabet', 's'),
              ('Arabic Alphabet', 'س'),
              ('English Alphabet', 's'),
              ('Greek Alphabet', 'σ')]),
 OrderedDict([('Moroccan Alphabet', 's'),
              ('Arabic Alphabet', 'س'),
              ('English Alphabet', 's'),
              ('Greek Alphabet', 'ς')]),
 OrderedDict([('Moroccan Alphabet', 'ch'),
              ('Arabic Alphabet', 'ش'),
              ('English Alphabet', 'ch'),
              ('Greek Alphabet', 'σ')]),
 OrderedDict([('Moroccan Alphabet', 'd'),
              ('Arabic Alphabet', 'د'),
              ('English Alphabet', 'd'),
              ('Greek Alphabet', 'δ')]),
 OrderedDict([('Moroccan Alphabet', 'd'),
              ('Arabic Alphabet', 'ذ'),
              ('English Alphabet', 'd'),
              ('Greek Alphabet', 'δ')]),
 OrderedDict([('Moroccan Alphabet', 'd'),
              ('Arabic Alphabet', 'ض'),
              ('English Alphabet', 'd'),
              ('Greek Alphabet', 'δ')]),
 OrderedDict([('Moroccan Alphabet', 'd'),
              ('Arabic Alphabet', 'ظ'),
              ('English Alphabet', 'd'),
              ('Greek Alphabet', 'δ')]),
 OrderedDict([('Moroccan Alphabet', 'e'),
              ('Arabic Alphabet', ''),
              ('English Alphabet', 'e'),
              ('Greek Alphabet', 'ε')]),
 OrderedDict([('Moroccan Alphabet', 'e'),
              ('Arabic Alphabet', 'ا'),
              ('English Alphabet', 'e'),
              ('Greek Alphabet', 'ε')]),
 OrderedDict([('Moroccan Alphabet', 'f'),
              ('Arabic Alphabet', 'ف'),
              ('English Alphabet', 'f'),
              ('Greek Alphabet', 'φ')]),
 OrderedDict([('Moroccan Alphabet', 'g'),
              ('Arabic Alphabet', 'ڭ'),
              ('English Alphabet', 'g'),
              ('Greek Alphabet', 'γ')]),
 OrderedDict([('Moroccan Alphabet', 'gh'),
              ('Arabic Alphabet', 'غ'),
              ('English Alphabet', 'gh'),
              ('Greek Alphabet', 'ρ')]),
 OrderedDict([('Moroccan Alphabet', 'h'),
              ('Arabic Alphabet', 'ه'),
              ('English Alphabet', 'h'),
              ('Greek Alphabet', 'χ')]),
 OrderedDict([('Moroccan Alphabet', 'h'),
              ('Arabic Alphabet', 'ح'),
              ('English Alphabet', 'h'),
              ('Greek Alphabet', 'χ')]),
 OrderedDict([('Moroccan Alphabet', 'h'),
              ('Arabic Alphabet', 'ح'),
              ('English Alphabet', 'h'),
              ('Greek Alphabet', 'η')]),
 OrderedDict([('Moroccan Alphabet', 'y'),
              ('Arabic Alphabet', 'ي'),
              ('English Alphabet', 'y'),
              ('Greek Alphabet', 'υ')]),
 OrderedDict([('Moroccan Alphabet', 'i'),
              ('Arabic Alphabet', 'ي'),
              ('English Alphabet', 'i'),
              ('Greek Alphabet', 'ι')]),
 OrderedDict([('Moroccan Alphabet', 'ee'),
              ('Arabic Alphabet', 'ي'),
              ('English Alphabet', 'ee'),
              ('Greek Alphabet', 'εε')]),
 OrderedDict([('Moroccan Alphabet', 'i'),
              ('Arabic Alphabet', 'ا'),
              ('English Alphabet', 'i'),
              ('Greek Alphabet', 'ι')]),
 OrderedDict([('Moroccan Alphabet', 'j'),
              ('Arabic Alphabet', 'ج'),
              ('English Alphabet', 'j'),
              ('Greek Alphabet', 'ζ')]),
 OrderedDict([('Moroccan Alphabet', 'k'),
              ('Arabic Alphabet', 'ك'),
              ('English Alphabet', 'k'),
              ('Greek Alphabet', 'κ')]),
 OrderedDict([('Moroccan Alphabet', 'c'),
              ('Arabic Alphabet', 'ك'),
              ('English Alphabet', 'c'),
              ('Greek Alphabet', 'σ')]),
 OrderedDict([('Moroccan Alphabet', 'kh'),
              ('Arabic Alphabet', 'خ'),
              ('English Alphabet', 'kh'),
              ('Greek Alphabet', 'χ')]),
 OrderedDict([('Moroccan Alphabet', 'l'),
              ('Arabic Alphabet', 'ل'),
              ('English Alphabet', 'l'),
              ('Greek Alphabet', 'λ')]),
 OrderedDict([('Moroccan Alphabet', 'la'),
              ('Arabic Alphabet', 'لا'),
              ('English Alphabet', 'la'),
              ('Greek Alphabet', 'λα')]),
 OrderedDict([('Moroccan Alphabet', 'm'),
              ('Arabic Alphabet', 'م'),
              ('English Alphabet', 'm'),
              ('Greek Alphabet', 'μ')]),
 OrderedDict([('Moroccan Alphabet', 'n'),
              ('Arabic Alphabet', 'ن'),
              ('English Alphabet', 'n'),
              ('Greek Alphabet', 'ν')]),
 OrderedDict([('Moroccan Alphabet', 'o'),
              ('Arabic Alphabet', 'و'),
              ('English Alphabet', 'o'),
              ('Greek Alphabet', 'ο')]),
 OrderedDict([('Moroccan Alphabet', 'o'),
              ('Arabic Alphabet', 'و'),
              ('English Alphabet', 'o'),
              ('Greek Alphabet', 'ω')]),
 OrderedDict([('Moroccan Alphabet', 'o'),
              ('Arabic Alphabet', 'ا'),
              ('English Alphabet', 'o'),
              ('Greek Alphabet', 'ο')]),
 OrderedDict([('Moroccan Alphabet', 'ou'),
              ('Arabic Alphabet', 'و'),
              ('English Alphabet', 'ou'),
              ('Greek Alphabet', 'oυ')]),
 OrderedDict([('Moroccan Alphabet', 'p'),
              ('Arabic Alphabet', 'پ'),
              ('English Alphabet', 'p'),
              ('Greek Alphabet', 'π')]),
 OrderedDict([('Moroccan Alphabet', 'q'),
              ('Arabic Alphabet', 'ق'),
              ('English Alphabet', 'q'),
              ('Greek Alphabet', 'κ')]),
 OrderedDict([('Moroccan Alphabet', 'r'),
              ('Arabic Alphabet', 'ر'),
              ('English Alphabet', 'r'),
              ('Greek Alphabet', 'ρ')]),
 OrderedDict([('Moroccan Alphabet', 's'),
              ('Arabic Alphabet', 'ص'),
              ('English Alphabet', 's'),
              ('Greek Alphabet', 'σ')]),
 OrderedDict([('Moroccan Alphabet', 'ss'),
              ('Arabic Alphabet', 'ص'),
              ('English Alphabet', 'ss'),
              ('Greek Alphabet', 'σσ')]),
 OrderedDict([('Moroccan Alphabet', 'sh'),
              ('Arabic Alphabet', 'ش'),
              ('English Alphabet', 'sh'),
              ('Greek Alphabet', 'σ')]),
 OrderedDict([('Moroccan Alphabet', 't'),
              ('Arabic Alphabet', 'ت'),
              ('English Alphabet', 't'),
              ('Greek Alphabet', 'τ')]),
 OrderedDict([('Moroccan Alphabet', 't'),
              ('Arabic Alphabet', 'ط'),
              ('English Alphabet', 't'),
              ('Greek Alphabet', 'τ')]),
 OrderedDict([('Moroccan Alphabet', 't'),
              ('Arabic Alphabet', 'ة'),
              ('English Alphabet', 't'),
              ('Greek Alphabet', 'τ')]),
 OrderedDict([('Moroccan Alphabet', 't'),
              ('Arabic Alphabet', 'ث'),
              ('English Alphabet', 't'),
              ('Greek Alphabet', 'θ')]),
 OrderedDict([('Moroccan Alphabet', 'u'),
              ('Arabic Alphabet', 'و'),
              ('English Alphabet', 'u'),
              ('Greek Alphabet', 'oυ')]),
 OrderedDict([('Moroccan Alphabet', 'v'),
              ('Arabic Alphabet', 'ڤ'),
              ('English Alphabet', 'v'),
              ('Greek Alphabet', 'β')]),
 OrderedDict([('Moroccan Alphabet', 'w'),
              ('Arabic Alphabet', 'و'),
              ('English Alphabet', 'w'),
              ('Greek Alphabet', 'oυ')]),
 OrderedDict([('Moroccan Alphabet', 'x'),
              ('Arabic Alphabet', 'كز'),
              ('English Alphabet', 'x'),
              ('Greek Alphabet', 'ξ')]),
 OrderedDict([('Moroccan Alphabet', 'x'),
              ('Arabic Alphabet', 'كس'),
              ('English Alphabet', 'x'),
              ('Greek Alphabet', 'ξ')]),
 OrderedDict([('Moroccan Alphabet', 'yi'),
              ('Arabic Alphabet', 'ي'),
              ('English Alphabet', 'yi'),
              ('Greek Alphabet', 'υι')]),
 OrderedDict([('Moroccan Alphabet', 'z'),
              ('Arabic Alphabet', 'ز'),
              ('English Alphabet', 'z'),
              ('Greek Alphabet', 'ζ')]),
 OrderedDict([('Moroccan Alphabet', '3'),
              ('Arabic Alphabet', 'ع'),
              ('English Alphabet', "'"),
              ('Greek Alphabet', "'")]),
 OrderedDict([('Moroccan Alphabet', '2'),
              ('Arabic Alphabet', 'ء'),
              ('English Alphabet', "'"),
              ('Greek Alphabet', "'")]),
 OrderedDict([('Moroccan Alphabet', '5'),
              ('Arabic Alphabet', 'خ'),
              ('English Alphabet', 'kh'),
              ('Greek Alphabet', 'χ')]),
 OrderedDict([('Moroccan Alphabet', '7'),
              ('Arabic Alphabet', 'ح'),
              ('English Alphabet', 'h'),
              ('Greek Alphabet', 'χ')]),
 OrderedDict([('Moroccan Alphabet', '9'),
              ('Arabic Alphabet', 'ق'),
              ('English Alphabet', 'q'),
              ('Greek Alphabet', 'κ')])]