"""This file contains all poject defaults and constants"""

# Project directories
BASE_DIR = './aaransia'
DATA_DIR = '/data'
LOG_DIR = '/log'
TEST_DIR = '/test'

# Data sets
ALPHABET_FILE = '/alphabet.csv'
DICTIONARY_FILE = '/dictionary.csv'

# Test files
TEST_CASES = '/test_cases.csv'

TEST_MOROCCAN_ALPHABET = '/test_moroccan_alphabet.csv'
TEST_MOROCCAN_WORDS = '/test_moroccan_words.csv'

TEST_MOROCCAN_ARABIC_ALPHABET = '/test_moroccan_arabic_alphabet.csv'
TEST_MOROCCAN_ARABIC_WORDS = '/test_moroccan_arabic_words.csv'

TEST_MOROCCAN_TO_LATIN_ALPHABET = '/test_moroccan_to_latin_alphabet.csv'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET = '/test_moroccan_arabic_to_latin_alphabet.csv'

# Test logs files
TEST_CASE_LOG_FILE = '/test_case.log'

TEST_MOROCCAN_ALPHABET_LOG_FILE = '/test_moroccan_alphabet.log'
TEST_MOROCCAN_WORDS_LOG_FILE = '/test_moroccan_words.log'

TEST_MOROCCAN_ARABIC_ALPHABET_LOG_FILE = '/test_moroccan_arabic_alphabet.log'
TEST_MOROCCAN_ARABIC_WORDS_LOG_FILE = '/test_moroccan_arabic_words.log'

TEST_MOROCCAN_TO_LATIN_ALPHABET_LOG_FILE = '/test_moroccan_to_latin_alphabet.log'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOG_FILE = '/test_moroccan_arabic_to_latin_alphabet.log'

TEST_STATS_LOG_FILE = '/test_stats.log'

# Loggers
TEST_STATS_LOGGER = 'test_stats_logger'
TEST_CASE_LOGGER = 'test_case_logger'

TEST_MOROCCAN_ALPHABET_LOGGER = 'test_moroccan_alphabet_logger'
TEST_MOROCCAN_WORDS_LOGGER = 'test_moroccan_words_logger'

TEST_MOROCCAN_ARABIC_ALPHABET_LOGGER = 'test_moroccan_arabic_alphabet_logger'
TEST_MOROCCAN_ARABIC_WORDS_LOGGER = 'test_moroccan_arabic_words_logger'

TEST_MOROCCAN_TO_LATIN_ALPHABET_LOGGER = 'test_moroccan_to_latin_alphabet_logger'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOGGER = 'test_moroccan_arabic_to_latin_alphabet_logger'

# Test strings
TEST_CASE = 'Test Case'
EXPECTED_RESULT = 'Expected Result'

# Alphabet codes
MOROCCAN_ALPHABET_CODE = 'ma'
ARABIAN_ALPHABET_CODE = 'ar'
LATIN_ALPHABET_CODE = 'la'
ABJADI_ALPHABET_CODE = 'ab'
GREEK_ALPHABET_CODE = 'gr'

# Alphabets
MOROCCAN_ALPHABET = 'Moroccan Alphabet'
ARABIAN_ALPHABET = 'Arabian Alphabet'
LATIN_ALPHABET = 'Latin Alphabet'
ABJADI_ALPHABET = 'Abjadi Alphabet'
GREEK_ALPHABET = 'Greek Alphabet'

# Language list
ALPHABETS = {
    MOROCCAN_ALPHABET_CODE: MOROCCAN_ALPHABET,
    ARABIAN_ALPHABET_CODE : ARABIAN_ALPHABET,
    LATIN_ALPHABET_CODE   : LATIN_ALPHABET,
    ABJADI_ALPHABET_CODE  : ABJADI_ALPHABET,
    GREEK_ALPHABET_CODE   : GREEK_ALPHABET
}

# Double Letters
DOUBLE_LETTERS = {
    MOROCCAN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ARABIAN_ALPHABET_CODE: ['كز', 'كس'],
    LATIN_ALPHABET_CODE: ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss'],
    ABJADI_ALPHABET_CODE: ['sh', 'gh', 'ee', 'kh', 'la', 'th', 'ch'],
    GREEK_ALPHABET_CODE: ['μπ', 'λα', 'oυ']
}

DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss']

# Double Moroccan Arabic Letters
DOUBLE_MOROCCAN_ARABIC_LETTERS = ['كز', 'كس']

# Exceptions
SOURCE_LANGUAGE_EXCEPTION = "Source language doesn't match the input text"
