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
alphabet_logger = logging.getLogger('alphabet_logger')
word_logger = logging.getLogger('word_logger')
sentence_logger = logging.getLogger('sentence_logger')
arabic_translation_logger = logging.getLogger('arabic_translation_logger')
french_translation_logger = logging.getLogger('french_translation_logger')
english_translation_logger = logging.getLogger('english_translation_logger')

# Data sets
alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
words = pd.read_csv(BASE_DIR + DATA_DIR + OPEN_DICTIONARY_SAMPLE)

# Test alphabet
def test_alphabet_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ALPHABET_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    alphabet_logger.addHandler(fh)
    alphabet_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    for index, row in alphabet.iterrows():
        arabian_letter, moroccan_translation = row["ArabianAlphabet"], moroccan_to_arabic(row["MoroccanAlphabet"])
        try:
            if arabian_letter == ' ':
                alphabet_logger.error('Translating   ( , [])')
            elif arabian_letter == moroccan_translation[0]["arabian_word"]:
                alphabet_logger.info(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
            else:
                alphabet_logger.warning(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
        except:
            alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')

# Test words
def test_word_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    word_logger.addHandler(fh)
    word_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    for index, row in words.iterrows():
        arabian_word, moroccan_translation = row["Moroccan Arabic"], moroccan_to_arabic(row["Moroccan"])
        try:
            if arabian_word == moroccan_translation[0]["arabian_word"]:
                word_logger.info(f'Translating {row["Moroccan"]} ({arabian_word}, {moroccan_translation[0]["arabian_word"]})')
            else:
                word_logger.warning(f'Translating {row["Moroccan"]} ({arabian_word}, {moroccan_translation[0]["arabian_word"]})')
        except:
            word_logger.error(f'Translating {row["Moroccan"]} ({arabian_word}, {moroccan_translation[0]["arabian_word"]})')


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

    # Test alphabet
    test_alphabet_translation()
    
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


