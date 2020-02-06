from collections import defaultdict

# Project directories
BASE_DIR = './aaransia'
DATA_DIR = '/data'
LOG_DIR = '/log'
TEST_DIR = '/test'

# Data sets
CONTROLLED_DICTIONARY = '/controlled_dictionary.csv'
DICTIONARY = '/dictionary.csv'
DICTIONARY_SAMPLE = '/dictionary_sample.csv'
TRANING_DATA = '/training_data.csv'
ALPHABET = '/alphabet.csv'

# Test files
TEST_CASES = '/test_cases.csv'
TEST_ALPHABET_MA_AR = '/test_alphabet_ma_ar.csv'
TEST_WORDS_MA_AR = '/test_words_ma_ar.csv'

TEST_ALPHABET_AR_MA = '/test_alphabet_ar_ma.csv'
TEST_WORDS_AR_MA = '/test_words_ar_ma.csv'

# Test logs files
TEST_CASE_LOG_FILE = '/test_case.log'

ALPHABET_MA_AR_TEST_LOG_FILE = '/test_alphabet_ma_ar.log'
WORD_MA_AR_TEST_LOG_FILE = '/test_word_ma_ar.log'
SENTENCE_MA_AR_TEST_LOG_FILE = '/test_sentence_ma_ar.log'

ALPHABET_AR_MA_TEST_LOG_FILE = '/test_alphabet_ar_ma.log'
WORD_AR_MA_TEST_LOG_FILE = '/test_word_ar_ma.log'
SENTENCE_AR_MA_TEST_LOG_FILE = '/test_sentence_ar_ma.log'

ARABIC_TRANSLATION_TEST_LOG_FILE = '/test_arabic_translation.log'
FRENCH_TRANSLATION_TEST_LOG_FILE = '/test_french_translation.log'
ENGLISH_TRANSLATION_TEST_LOG_FILE = '/test_english_translation.log'

TEST_STATS_LOG_FILE = '/test_stats.log'

# Double moroccan letters
DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee']

# Alphabets
moroccan_alphabet = {   
                ' ': [' '],
                '!': ['!'],
                ',': ['،'],
                '.': ['.'],
                '2': ['ء'],
                '3': ['ع'],
                '5': ['خ'],
                '7': ['ح'],
                '9': ['ق'],
                '?': ['؟'],
                'a': ['ا', 'أ'],
                'b': ['ب'],
                'c': ['ك'],
                'ch': ['ش'],
                'd': ['د', 'ذ', 'ض', 'ظ'],
                'e': [' ', 'إ'],
                'ee': ['ي'],
                'f': ['ف'],
                'g': ['ڭ'],
                'gh': ['غ'],
                'h': ['ه'],
                'i': ['ي', 'إ'],
                'j': ['ج'],
                'k': ['ك'],
                'kh': ['خ'],
                'l': ['ل'],
                'la': ['لا'],
                'm': ['م'],
                'n': ['ن'],
                'o': ['و', 'أ'],
                'ou': ['و'],
                'p': ['پ'],
                'q': ['ق'],
                'r': ['ر'],
                's': ['س', 'ص'],
                'sh': ['ش'],
                't': ['ت', 'ة', 'ط', 'ث'],
                'u': ['و'],
                'v': ['ڤ'],
                'w': ['و'],
                'x': ['كس', 'كز'],
                'y': ['ي'],
                'yi': ['ي'],
                'z': ['ز']}

moroccan_arabic_alphabet = {   
                ' ': [' ', 'e'],
                '!': ['!'],
                '.': ['.'],
                'Test Case': ['Expected Result'],
                '،': [','],
                '؟': ['?'],
                'ء': ['2'],
                'أ': ['o', 'a'],
                'إ': ['e', 'i'],
                'ا': ['a'],
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
                'ص': ['s'],
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
                'و': ['o', 'w', 'ou', 'u'],
                'ي': ['i', 'y', 'yi', 'ee'],
                'پ': ['p'],
                'ڤ': ['v'],
                'ڭ': ['g']}