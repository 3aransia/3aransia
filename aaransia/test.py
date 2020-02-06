import logging
import logging.handlers
import os

from aaransia.transliterator import *
from aaransia.constants import *
from aaransia.machine_learning import *
from aaransia.utils import *

# Refresh test files
build_test_alphabet_ma_ar_file()
build_test_words_ma_ar_file()

build_test_alphabet_ar_ma_file()
build_test_words_ar_ma_file()

# Logging config
logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
test_stats_logger = logging.getLogger('test_stats_logger')
test_case_logger = logging.getLogger('test_case_logger')

alphabet_ma_ar_logger = logging.getLogger('alphabet_ma_ar_logger')
word_ma_ar_logger = logging.getLogger('word_ma_ar_logger')

alphabet_ar_ma_logger = logging.getLogger('alphabet_ar_ma_logger')
word_ar_ma_logger = logging.getLogger('word_ar_ma_logger')

sentence_logger = logging.getLogger('sentence_logger')
arabic_translation_logger = logging.getLogger('arabic_translation_logger')
french_translation_logger = logging.getLogger('french_translation_logger')
english_translation_logger = logging.getLogger('english_translation_logger')

# Test sets
test_cases = pd.read_csv(BASE_DIR + TEST_DIR + TEST_CASES)

alphabet_ma_ar = pd.read_csv(BASE_DIR + TEST_DIR + TEST_ALPHABET_MA_AR)
words_ma_ar = pd.read_csv(BASE_DIR + TEST_DIR + TEST_WORDS_MA_AR)

alphabet_ar_ma = pd.read_csv(BASE_DIR + TEST_DIR + TEST_ALPHABET_AR_MA)
words_ar_ma = pd.read_csv(BASE_DIR + TEST_DIR + TEST_WORDS_AR_MA)

# Test statistics logger
fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_STATS_LOG_FILE, 'a')
fh.setFormatter(formatter)
fh.setLevel(logging.INFO)
test_stats_logger.addHandler(fh)
test_stats_logger.info(f'\n')

# Test case 
def test_case():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_CASE_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    test_case_logger.addHandler(fh)
    test_case_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in test_cases.iterrows():
        expected_result, moroccan_translation = row["Expected Result"], moroccan_to_arabic(row["Test Case"])
        try:
            if expected_result == moroccan_translation:
                test_case_logger.info(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_infos += 1
            else:
                test_case_logger.warning(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_warnings += 1
        except (IndexError, KeyError, TypeError) as e:
            test_case_logger.error(f'Translating {row["Test Case"]}, {e}')
            count_errors += 1
    test_case_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(test_cases)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')
    test_stats_logger.info(f'test_case_logger - Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(test_cases)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')


# Test moroccan alphabet
def test_alphabet_ma_ar_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ALPHABET_MA_AR_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    alphabet_ma_ar_logger.addHandler(fh)
    alphabet_ma_ar_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in alphabet_ma_ar.iterrows():
        expected_result, moroccan_translation = row["Expected Result"], moroccan_to_arabic(row["Test Case"])
        try:
            if expected_result == moroccan_translation:
                alphabet_ma_ar_logger.info(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_infos += 1
            else:
                alphabet_ma_ar_logger.warning(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_warnings += 1
        except (IndexError, KeyError, TypeError) as e:
            alphabet_ma_ar_logger.error(f'Translating {row["Test Case"]}, {e}')
            count_errors += 1
    alphabet_ma_ar_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_ma_ar)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(alphabet_ma_ar)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_ma_ar)*100, 2)}%)')
    test_stats_logger.info(f'alphabet_ma_ar_logger - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_ma_ar)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(alphabet_ma_ar)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_ma_ar)*100, 2)}%)')

# Test moroccan words
def test_word_ma_ar_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_MA_AR_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    word_ma_ar_logger.addHandler(fh)
    word_ma_ar_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in words_ma_ar.iterrows():
        expected_result, moroccan_translation = row["Expected Result"], moroccan_to_arabic(row["Test Case"])
        try:
            if expected_result == moroccan_translation:
                word_ma_ar_logger.info(f'Translating {row["Test Case"]} ({expected_result} , {moroccan_translation})')
                count_infos += 1
            else:
                word_ma_ar_logger.warning(f'Translating {row["Test Case"]} ({expected_result} , {moroccan_translation})')
                count_warnings += 1
        except (IndexError, KeyError, TypeError) as e:
            alphabet_ma_ar_logger.error(f'Translating {row["Test Case"]}, {e}')
            count_errors += 1
    word_ma_ar_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_ma_ar)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(words_ma_ar)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_ma_ar)*100, 2)}%)')
    test_stats_logger.info(f'word_ma_ar_logger - Total INFO logs {count_infos} ({round(count_infos/len(words_ma_ar)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(words_ma_ar)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_ma_ar)*100, 2)}%)')

# Test arabian moroccan alphabet
def test_alphabet_ar_ma_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + ALPHABET_AR_MA_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    alphabet_ar_ma_logger.addHandler(fh)
    alphabet_ar_ma_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in alphabet_ar_ma.iterrows():
        expected_result, moroccan_translation = row["Expected Result"], arabic_moroccan_to_moroccan(row["Test Case"])
        try:
            if expected_result == moroccan_translation:
                alphabet_ar_ma_logger.info(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_infos += 1
            else:
                alphabet_ar_ma_logger.warning(f'Translating {row["Test Case"]} ({expected_result}, {moroccan_translation})')
                count_warnings += 1
        except (IndexError, KeyError, TypeError) as e:
            alphabet_ar_ma_logger.error(f'Translating {row["Test Case"]}, {e}')
            count_errors += 1
    alphabet_ar_ma_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_ar_ma)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(alphabet_ar_ma)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_ar_ma)*100, 2)}%)')
    test_stats_logger.info(f'alphabet_ar_ma_logger - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_ar_ma)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(alphabet_ar_ma)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet)*100, 2)}%)')

# Test arabian moroccan words
def test_word_ar_ma_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + WORD_AR_MA_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    word_ar_ma_logger.addHandler(fh)
    word_ar_ma_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

    count_infos, count_warnings, count_errors = 0, 0, 0

    for index, row in words_ar_ma.iterrows():
        expected_result, moroccan_translation = row["Expected Result"], arabic_moroccan_to_moroccan(row["Test Case"])
        try:
            if expected_result.lower() == moroccan_translation:
                word_ar_ma_logger.info(f'Translating {row["Test Case"]} ({expected_result} , {moroccan_translation})')
                count_infos += 1
            else:
                word_ar_ma_logger.warning(f'Translating {row["Test Case"]} ({expected_result} , {moroccan_translation})')
                count_warnings += 1
        except (IndexError, KeyError, TypeError) as e:
            alphabet_ar_ma_logger.error(f'Translating {row["Test Case"]}, {e}')
            count_errors += 1
    word_ar_ma_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_ar_ma)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(words_ar_ma)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_ar_ma)*100, 2)}%)')
    test_stats_logger.info(f'word_ar_ma_logger - Total INFO logs {count_infos} ({round(count_infos/len(words_ar_ma)*100, 2)}%), Total WARNING logs {count_warnings} ({round(count_warnings/len(words_ar_ma)*100, )}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_ar_ma)*100, 2)}%)')

# Test moroccan sentences
def test_sentence_ma_ar_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SENTENCE_MA_AR_TEST_LOG_FILE, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(logging.INFO)
    sentence_logger.addHandler(fh)

# Test arabian moroccan sentences
def test_sentence_ar_ma_translation():
    fh = logging.FileHandler(BASE_DIR + LOG_DIR + SENTENCE_AR_MA_TEST_LOG_FILE, 'w')
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
    # Test case
    test_case()

    # Test morrocan alphabet to arabic
    test_alphabet_ma_ar_translation()
    
    # Test moroccan words to arabic
    test_word_ma_ar_translation()
    
    # Test moroccan sentenses to arabic
    test_sentence_ma_ar_translation()

    # Test arabic alphabet to moroccan
    test_alphabet_ar_ma_translation()
    
    # Test arabic words to moroccan
    test_word_ar_ma_translation()
    
    # Test arabic sentenses to moroccan
    test_sentence_ar_ma_translation()

    # Test Arabic translation of words
    test_arabic_translation_translation()
    
    # Test French translation of words
    test_french_translation_translation()

    # Test English translation of words
    test_english_translation_translation() 

    



