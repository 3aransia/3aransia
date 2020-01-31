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
simple_alphabet_logger = logging.getLogger('simple_alphabet_logger')
alphabet_logger = logging.getLogger('alphabet_logger')
word_logger = logging.getLogger('word_logger')
sentence_logger = logging.getLogger('sentence_logger')
arabic_translation_logger = logging.getLogger('arabic_translation_logger')
french_translation_logger = logging.getLogger('french_translation_logger')
english_translation_logger = logging.getLogger('english_translation_logger')

# Data sets
simple_alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_SIMPLE_ALPHABET)
alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
words = pd.read_csv(BASE_DIR + DATA_DIR + OPEN_DICTIONARY_SAMPLE)

# Test simple alphabet
def test_simple_alphabet_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SIMPLE_ALPHABET_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    simple_alphabet_logger.addHandler(fh)
    simple_alphabet_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in simple_alphabet.iterrows():
        arabian_letter, moroccan_translation = row["ArabianAlphabet"], moroccan_to_arabic(row["MoroccanAlphabet"])
        try:
            if arabian_letter == ' ':
                simple_alphabet_logger.error('Translating   ( , [])')
                count_errors += 1
            elif arabian_letter == moroccan_translation[0]["arabian_word"]:
                simple_alphabet_logger.info(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
                count_infos += 1
            else:
                simple_alphabet_logger.warning(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
                count_warnings += 1
        except IndexError:
            simple_alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, IndexError')
            count_errors += 1
        except KeyError:
            simple_alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, KeyError')
            count_errors += 1
        except TypeError:
            simple_alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, TypeError')
            count_errors += 1
    simple_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(simple_alphabet)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(simple_alphabet)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(simple_alphabet)*100, 2)}%)')


# Test alphabet
def test_alphabet_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ALPHABET_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    alphabet_logger.addHandler(fh)
    alphabet_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in alphabet.iterrows():
        arabian_letter, moroccan_translation = row["ArabianAlphabet"], moroccan_to_arabic(row["MoroccanAlphabet"])
        try:
            if arabian_letter == ' ':
                alphabet_logger.error('Translating   ( , [])')
                count_errors += 1
            elif arabian_letter == moroccan_translation[0]["arabian_word"]:
                alphabet_logger.info(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
                count_infos += 1
            else:
                alphabet_logger.warning(f'Translating {row["MoroccanAlphabet"]} ({arabian_letter}, {moroccan_translation[0]["arabian_word"]})')
                count_warnings += 1
        except IndexError:
            alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, IndexError')
            count_errors += 1
        except KeyError:
            alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, KeyError')
            count_errors += 1
        except TypeError:
            alphabet_logger.error(f'Translating {row["MoroccanAlphabet"]}, TypeError')
            count_errors += 1

    alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(alphabet)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet)*100, 2)}%)')

# Test words
def test_word_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    word_logger.addHandler(fh)
    word_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in words.iterrows():
        arabian_word, moroccan_translation = row["Moroccan Arabic"], moroccan_to_arabic(row["Moroccan"])
        try:
            if arabian_word == moroccan_translation[0]["arabian_word"]:
                word_logger.info(f'Translating {row["Moroccan"]} ({arabian_word}, {moroccan_translation[0]["arabian_word"]})')
                count_infos += 1
            else:
                word_logger.warning(f'Translating {row["Moroccan"]} ({arabian_word}, {moroccan_translation[0]["arabian_word"]})')
                count_warnings += 1
        except IndexError:
            word_logger.error(f'Translating {row["Moroccan"]}, IndexError')
            count_errors += 1
        except KeyError:
            word_logger.error(f'Translating {row["Moroccan"]}, KeyError')
            count_errors += 1
        except TypeError:
            word_logger.error(f'Translating {row["Moroccan"]}, TypeError')
            count_errors += 1
    word_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(words)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(words)*100, 2)}%)')

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
    # Test simple alphabet
    test_simple_alphabet_translation()

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


