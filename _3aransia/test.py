import logging

from _3aransia.translator import *
from _3aransia.constants import *
from _3aransia.machine_learning import *

logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)

# Test single letters
def test_single_letter_translation():
    logger = logging.getLogger('Single letter logger')
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SINGLE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    logging.info(f'Translating a ({alphabet.loc[alphabet["MoroccanAlphabet"] == "a"]["ArabianAlphabet"].values[0]}, { moroccan_to_arabic("a")[0]["arabian_word"]})')

# Test double letters
def test_double_letter_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + DOUBLE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test duplicate letters
def test_duplicate_letter_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + DUPLICATE_LETTER_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test words
def test_word_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test sentences
def test_sentence_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SENTENCE_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test Arabic translation
def test_arabic_translation_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ARABIC_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test French translation
def test_french_translation_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + FRENCH_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

# Test English translation
def test_english_translation_translation():
    logger = logging.getLogger()
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ENGLISH_TRANSLATION_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)

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


