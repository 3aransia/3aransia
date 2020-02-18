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
moroccan_alphabet = {   ' ': [' '],
                '!': ['!'],
                ',': ['،'],
                '.': ['.'],
                '2': ['ء'],
                '3': ['ع'],
                '5': ['خ'],
                '7': ['ح'],
                '9': ['ق'],
                '?': ['؟'],
                'a': ['ا'],
                'b': ['ب'],
                'c': ['ك'],
                'ch': ['ش'],
                'd': ['د', 'ذ', 'ض', 'ظ'],
                'e': [' ', 'ا'],
                'ee': ['ي'],
                'f': ['ف'],
                'g': ['ڭ'],
                'gh': ['غ'],
                'h': ['ه'],
                'i': ['ي', 'ا'],
                'j': ['ج'],
                'k': ['ك'],
                'kh': ['خ'],
                'l': ['ل'],
                'la': ['لا'],
                'm': ['م'],
                'n': ['ن'],
                'o': ['و', 'ا'],
                'ou': ['و'],
                'p': ['پ'],
                'q': ['ق'],
                'r': ['ر'],
                's': ['س', 'ص'],
                'sh': ['ش'],
                'ss': ['ص'],
                't': ['ت', 'ط', 'ة', 'ث'],
                'u': ['و'],
                'v': ['ڤ'],
                'w': ['و'],
                'x': ['كز', 'كس'],
                'y': ['ي'],
                'yi': ['ي'],
                'z': ['ز']}

moroccan_arabic_alphabet = {   ' ': [' ', 'e'],
                '!': ['!'],
                '.': ['.'],
                '،': [','],
                '؟': ['?'],
                'ء': ['2'],
                'ا': ['a', 'e', 'i', 'o'],
                'ب': ['b'],
                'ة': ['t'],
                'ت': ['t'],
                'ث': ['t'],
                'ج': ['j'],
                'ح': ['7'],
                'خ': ['5', 'kh'],
                'د': ['d'],
                'ذ': ['d'],
                'ر': ['r'],
                'ز': ['z'],
                'س': ['s'],
                'ش': ['ch', 'sh'],
                'ص': ['s', 'ss'],
                'ض': ['d'],
                'ط': ['t'],
                'ظ': ['d'],
                'ع': ['3'],
                'غ': ['gh'],
                'ف': ['f'],
                'ق': ['9', 'q'],
                'ك': ['k', 'c'],
                'كز': ['x'],
                'كس': ['x'],
                'ل': ['l'],
                'لا': ['la'],
                'م': ['m'],
                'ن': ['n'],
                'ه': ['h'],
                'و': ['o', 'ou', 'u', 'w'],
                'ي': ['y', 'i', 'ee', 'yi'],
                'پ': ['p'],
                'ڤ': ['v'],
                'ڭ': ['g']}

moroccan_to_latin_alphabet = {   ' ': [' '],
                '!': ['!'],
                ',': [','],
                '.': ['.'],
                '2': ['e'],
                '3': ["'"],
                '5': ['kh'],
                '7': ['h'],
                '9': ['q'],
                '?': ['?'],
                'a': ['a'],
                'b': ['b'],
                'c': ['c'],
                'ch': ['ch'],
                'd': ['d', 'd', 'd', 'd'],
                'e': ['e', 'e'],
                'ee': ['ee'],
                'f': ['f'],
                'g': ['g'],
                'gh': ['gh'],
                'h': ['h'],
                'i': ['i', 'i'],
                'j': ['j'],
                'k': ['k'],
                'kh': ['kh'],
                'l': ['l'],
                'la': ['la'],
                'm': ['m'],
                'n': ['n'],
                'o': ['o', 'o'],
                'ou': ['ou'],
                'p': ['b'],
                'q': ['q'],
                'r': ['r'],
                's': ['s', 's'],
                'sh': ['sh'],
                'ss': ['ss'],
                't': ['t', 't', 't', 't'],
                'u': ['u'],
                'v': ['v'],
                'w': ['w'],
                'x': ['x', 'x'],
                'y': ['y'],
                'yi': ['yi'],
                'z': ['z']}

moroccan_arabic_to_latin_alphabet = {   ' ': [' ', 'e'],
                '!': ['!'],
                '.': ['.'],
                '،': [','],
                '؟': ['?'],
                'ء': ['e'],
                'ا': ['a', 'e', 'i', 'o'],
                'ب': ['b'],
                'ة': ['t'],
                'ت': ['t'],
                'ث': ['t'],
                'ج': ['j'],
                'ح': ['h'],
                'خ': ['kh', 'kh'],
                'د': ['d'],
                'ذ': ['d'],
                'ر': ['r'],
                'ز': ['z'],
                'س': ['s'],
                'ش': ['ch', 'sh'],
                'ص': ['s', 'ss'],
                'ض': ['d'],
                'ط': ['t'],
                'ظ': ['d'],
                'ع': ["'"],
                'غ': ['gh'],
                'ف': ['f'],
                'ق': ['q', 'q'],
                'ك': ['k', 'c'],
                'كز': ['x'],
                'كس': ['x'],
                'ل': ['l'],
                'لا': ['la'],
                'م': ['m'],
                'ن': ['n'],
                'ه': ['h'],
                'و': ['o', 'ou', 'u', 'w'],
                'ي': ['y', 'i', 'ee', 'yi'],
                'پ': ['b'],
                'ڤ': ['v'],
                'ڭ': ['g']}