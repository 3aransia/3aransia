import logging
import logging.handlers
import os

from _3aransia.translator import *
from _3aransia.constants import *
from _3aransia.machine_learning import *

# Logging config
logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
single_letter_logger = logging.getLogger('single_letter_logger')
double_letter_logger = logging.getLogger('double_letter_logger')
duplicate_letter_logger = logging.getLogger('duplicate_letter_logger')
word_logger = logging.getLogger('word_logger')
sentence_logger = logging.getLogger('sentence_logger')
arabic_translation_logger = logging.getLogger('arabic_translation_logger')
french_translation_logger = logging.getLogger('french_translation_logger')
english_translation_logger = logging.getLogger('english_translation_logger')

# Alphabet
alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)

# Test single letters
def test_single_letter_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SINGLE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    single_letter_logger.addHandler(fh)

    if str(alphabet.loc[alphabet["MoroccanAlphabet"] == "a"]["ArabianAlphabet"].values[0]) == str(moroccan_to_arabic("a")[0]["arabian_word"]):
        single_letter_logger.info(f'Translating a ({alphabet.loc[alphabet["MoroccanAlphabet"] == "a"]["ArabianAlphabet"].values[0]}, { moroccan_to_arabic("a")[0]["arabian_word"]})')
    else:
        single_letter_logger.warning(f'Translating a ({alphabet.loc[alphabet["MoroccanAlphabet"] == "a"]["ArabianAlphabet"].values[0]}, { moroccan_to_arabic("a")[0]["arabian_word"]})')

        
# Test double letters
def test_double_letter_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + DOUBLE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    double_letter_logger.addHandler(fh)

# Test duplicate letters
def test_duplicate_letter_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + DUPLICATE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    duplicate_letter_logger.addHandler(fh)


# Test words
def test_word_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    word_logger.addHandler(fh)

# Test sentences
def test_sentence_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SENTENCE_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    sentence_logger.addHandler(fh)

# Test Arabic translation
def test_arabic_translation_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ARABIC_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    arabic_translation_logger.addHandler(fh)

# Test French translation
def test_french_translation_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + FRENCH_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    french_translation_logger.addHandler(fh)

# Test English translation
def test_english_translation_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ENGLISH_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    english_translation_logger.addHandler(fh)

# Test function
def run_tests():
    # 3aransia test framework

    # Reported annomalies written in issues
    # Fixing bugs incrementally and agilly 
    # Use exceptions to handle errors

    # lexical Translation tests

    # Test single letters
    test_single_letter_translation()
    
    # Test double letters
    test_double_letter_translation()
    
    # Test duplicate letters
    test_duplicate_letter_translation()
    
    # Test words
    test_word_translation()
    
    # Test sentenses
    test_sentence_translation()

    # Test Arabic translation of words
    test_arabic_translation_translation()
    
    # Test French translation of words
    test_french_translation_translation()

    # Test English translation of words
    test_english_translation_translation() 


