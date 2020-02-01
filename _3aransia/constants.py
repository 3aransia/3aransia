BASE_DIR = './_3aransia'
DATA_DIR = '/data'
LOG_DIR = '/log'
CURRENT_DIR = '.'

CONTROLLED_DICTIONARY = '/controlled_dictionary.csv'
OPEN_DICTIONARY = '/open_dictionary.csv'
OPEN_DICTIONARY_SAMPLE = '/open_dictionary_sample.csv'
TRANING_DATA = '/training_data.csv'
MOROCCAN_ALPHABET = '/moroccan_alphabet.csv'
MOROCCAN_SIMPLE_ALPHABET = '/moroccan_simple_alphabet.csv'

ALPHABET_TEST_LOG_FILE = '/test_alphabet.log'
SIMPLE_ALPHABET_TEST_LOG_FILE = '/test_simple_alphabet.log'
WORD_TEST_LOG_FILE = '/test_word.log'
SENTENCE_TEST_LOG_FILE = '/test_sentence.log'

ARABIC_TRANSLATION_TEST_LOG_FILE = '/test_arabic_translation.log'
FRENCH_TRANSLATION_TEST_LOG_FILE = '/test_french_translation.log'
ENGLISH_TRANSLATION_TEST_LOG_FILE = '/test_english_translation.log'

UPPER_ENGLISH_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
LOWER_ENGLISH_ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

UPPER_ENGLISH_VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
UPPER_ENGLISH_CONSONS = list(set(UPPER_ENGLISH_ALPHABET) - set(UPPER_ENGLISH_VOWELS))

LOWER_ENGLISH_VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
LOWER_ENGLISH_CONSONS = list(set(LOWER_ENGLISH_ALPHABET) - set(LOWER_ENGLISH_VOWELS))

NUMBERS = '0123456789'

DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi']

DUPLICATE_MOROCCAN_LETTERS = ['aa', 'bb', 'cc','dd','ee','ff','gg','hh','ii','jj', 
    'kk', 'll', 'mm','nn','oo','pp', 'qq', '77', '22', '55', '99', '33', 'rr', 'ss', 'tt', 'uu','ww','xx', 'yy','zz']