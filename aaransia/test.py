import unittest
import logging

from aaransia.transliteration import *
from aaransia.constants import *
from aaransia.utils import *

# Refresh test files based on the csv data
build_moroccan_alphabet_test_file()
build_moroccan_words_test_file()

build_moroccan_arabic_alphabet_test_file()
build_moroccan_arabic_words_test_file()

# Logging config
logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
test_stats_logger = logging.getLogger(TEST_STATS_LOGGER)
test_case_logger = logging.getLogger(TEST_CASE_LOGGER)

test_moroccan_alphabet_logger = logging.getLogger(TEST_MOROCCAN_ALPHABET_LOGGER)
test_moroccan_words_logger = logging.getLogger(TEST_MOROCCAN_WORDS_LOGGER)

test_moroccan_arabic_alphabet_logger = logging.getLogger(TEST_MOROCCAN_ARABIC_ALPHABET_LOGGER)
test_moroccan_arabic_words_logger = logging.getLogger(TEST_MOROCCAN_ARABIC_WORDS_LOGGER)

# Test sets
test_cases = pd.read_csv(BASE_DIR + TEST_DIR + TEST_CASES)

alphabet_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET)
words_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS)

alphabet_moroccan_arabic_to_moroccan = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_ALPHABET)
words_moroccan_arabic_to_moroccan = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_WORDS)

# Test statistics logger
fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_STATS_LOG_FILE, 'a')
fh.setFormatter(formatter)
fh.setLevel(logging.INFO)
test_stats_logger.addHandler(fh)
test_stats_logger.info(f'\n')

class TestSequenceFunctions(unittest.TestCase):
    def SetUp(self):
        pass

    # Test case 
    def test_case(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_CASE_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_case_logger.addHandler(fh)
        test_case_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in test_cases.iterrows():
            expected_result, moroccan_translation = row["Expected Result"], transliterate_moroccan(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_translation)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_case_logger.error(f'Translating {row["Test Case"]}, {e}')
                count_errors += 1
        test_case_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')
        test_stats_logger.info(f'test_case_logger - Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')


    # Test moroccan alphabet
    def test_moroccan_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_alphabet_logger.addHandler(fh)
        test_moroccan_alphabet_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_to_moroccan_arabic.iterrows():
            expected_result, moroccan_translation = row["Expected Result"], transliterate_moroccan(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_translation)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_alphabet_logger.error(f'Translating {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')
        test_stats_logger.info(f'test_moroccan_alphabet_logger - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')

    # Test moroccan words
    def test_moroccan_words_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_WORDS_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_words_logger.addHandler(fh)
        test_moroccan_words_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in words_moroccan_to_moroccan_arabic.iterrows():
            expected_result, moroccan_translation = row["Expected Result"], transliterate_moroccan(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_translation)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_words_logger.error(f'Translating {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_words_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_to_moroccan_arabic)*100, 2)}%)')
        test_stats_logger.info(f'test_moroccan_words_logger - Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_to_moroccan_arabic)*100, 2)}%)')

    # Test arabian moroccan alphabet
    def test_moroccan_arabic_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ARABIC_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_arabic_alphabet_logger.addHandler(fh)
        test_moroccan_arabic_alphabet_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_arabic_to_moroccan.iterrows():
            expected_result, moroccan_translation = row["Expected Result"], transliterate_moroccan_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_translation)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_arabic_alphabet_logger.error(f'Translating {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_arabic_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%)')
        test_stats_logger.info(f'test_moroccan_arabic_alphabet_logger - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%)')

    # Test arabian moroccan words
    def test_moroccan_arabic_words_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ARABIC_WORDS_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_arabic_words_logger.addHandler(fh)
        test_moroccan_arabic_words_logger.info(f'Translating [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in words_moroccan_arabic_to_moroccan.iterrows():
            expected_result, moroccan_translation = row["Expected Result"], transliterate_moroccan_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_translation)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_arabic_words_logger.error(f'Translating {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_arabic_words_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_arabic_to_moroccan)*100, 2)}%)')
        test_stats_logger.info(f'test_moroccan_arabic_words_logger - Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_arabic_to_moroccan)*100, 2)}%)')

def run_tests():
    unittest.main()