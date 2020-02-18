from collections import defaultdict

# Project directories
BASE_DIR = './aaransia'
DATA_DIR = '/data'
LOG_DIR = '/log'
TEST_DIR = '/test'

# Data sets
ALPHABET = '/alphabet.csv'
DICTIONARY = '/dictionary.csv'

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


# Double Moroccan Letters
DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss']

# Double Moroccan Arabic Letters
DOUBLE_MOROCCAN_ARABIC_LETTERS = ['كز','كس']

# Alphabets
MOROCCAN_ALPHABET = 'Moroccan Alphabet'
ARABIAN_ALPHABET = 'Arabian Alphabet'
LATIN_ALPHABET = 'Latin Alphabet'
ABJADI_ALPHABET = 'Abjadi Alphabet'
GREEK_ALPHABET = 'Greek Alphabet'