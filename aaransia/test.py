import unittest
import logging

from aaransia.transliteration import *
from aaransia.defaults import *
from aaransia.utils import *

# Building test files

# Build moroccan alphabet test file
def build_moroccan_alphabet_test_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET_FILE)
    alphabet_test = alphabet.rename(columns={
                          MOROCCAN_ALPHABET:TEST_CASE,
                          ARABIAN_ALPHABET:EXPECTED_RESULT})
    alphabet_test = alphabet_test[[TEST_CASE, EXPECTED_RESULT]]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET, index=False)

# Build moroccan words test File
def build_moroccan_words_test_file():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_FILE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic','French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
                          'Moroccan':TEST_CASE,
                          'Moroccan Arabic':EXPECTED_RESULT})
    moroccan_words_test = moroccan_words_test[[TEST_CASE, EXPECTED_RESULT]]
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS, index=False)

# Build arabian alphabet test file
def build_moroccan_arabic_alphabet_test_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET_FILE)
    alphabet_test = alphabet.rename(columns={
                          ARABIAN_ALPHABET:TEST_CASE,
                          MOROCCAN_ALPHABET:EXPECTED_RESULT})
    alphabet_test = alphabet_test[[TEST_CASE, EXPECTED_RESULT]]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_ALPHABET, index=False)

# Build arabian words test file
def build_moroccan_arabic_words_test_file():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_FILE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic','French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
                          'Moroccan Arabic':TEST_CASE,
                          'Moroccan':EXPECTED_RESULT})
    moroccan_words_test = moroccan_words_test[[TEST_CASE, EXPECTED_RESULT]]
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_WORDS, index=False)

# Build moroccan to latin alphabet test file
def build_moroccan_to_latin_alphabet_test_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET_FILE)
    alphabet_test = alphabet.rename(columns={
                          MOROCCAN_ALPHABET:TEST_CASE,
                          LATIN_ALPHABET:EXPECTED_RESULT})
    alphabet_test = alphabet_test[[TEST_CASE, EXPECTED_RESULT]]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_TO_LATIN_ALPHABET, index=False)

# Build moroccan arabic to latin alphabet test file
def build_moroccan_arabic_to_latin_alphabet_test_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET_FILE)
    alphabet_test = alphabet.rename(columns={
                          ARABIAN_ALPHABET:TEST_CASE,
                          LATIN_ALPHABET:EXPECTED_RESULT})
    alphabet_test = alphabet_test[[TEST_CASE, EXPECTED_RESULT]]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET, index=False)

# Refresh test files based on the csv data
build_moroccan_alphabet_test_file()
build_moroccan_words_test_file()

build_moroccan_arabic_alphabet_test_file()
build_moroccan_arabic_words_test_file()

build_moroccan_to_latin_alphabet_test_file()
build_moroccan_arabic_to_latin_alphabet_test_file()

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

test_moroccan_to_latin_alphabet_logger = logging.getLogger(TEST_MOROCCAN_TO_LATIN_ALPHABET_LOGGER)
test_moroccan_arabic_to_latin_alphabet_logger = logging.getLogger(TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOGGER)

# Test sets
test_cases = pd.read_csv(BASE_DIR + TEST_DIR + TEST_CASES)

alphabet_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET)
words_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS)

alphabet_moroccan_arabic_to_moroccan = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_ALPHABET)
words_moroccan_arabic_to_moroccan = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_WORDS)

alphabet_moroccan_to_latin = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_TO_LATIN_ALPHABET)
alphabet_moroccan_arabic_to_latin = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET)

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
        test_case_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in test_cases.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_case_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_case_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')
        test_stats_logger.info(f'test_case_logger - Total INFO logs {count_infos} ({round(count_infos/len(test_cases)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(test_cases)*100, 2)}%)')


    # Test moroccan alphabet
    def test_moroccan_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_alphabet_logger.addHandler(fh)
        test_moroccan_alphabet_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_to_moroccan_arabic.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_alphabet_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_ALPHABET_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')

    # Test moroccan words
    def test_moroccan_words_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_WORDS_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_words_logger.addHandler(fh)
        test_moroccan_words_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in words_moroccan_to_moroccan_arabic.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_words_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_words_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_to_moroccan_arabic)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_WORDS_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_to_moroccan_arabic)*100, 2)}%)')

    # Test arabian moroccan alphabet
    def test_moroccan_arabic_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ARABIC_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_arabic_alphabet_logger.addHandler(fh)
        test_moroccan_arabic_alphabet_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_arabic_to_moroccan.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_arabic_alphabet_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_arabic_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_ARABIC_ALPHABET_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_moroccan)*100, 2)}%)')

    # Test arabian moroccan words
    def test_moroccan_arabic_words_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ARABIC_WORDS_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_arabic_words_logger.addHandler(fh)
        test_moroccan_arabic_words_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in words_moroccan_arabic_to_moroccan.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic_arabic(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_arabic_words_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_arabic_words_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_arabic_to_moroccan)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_ARABIC_WORDS_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(words_moroccan_arabic_to_moroccan)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(words_moroccan_arabic_to_moroccan)*100, 2)}%)')

    # Test moroccan to latin alphabet
    def test_moroccan_to_latin_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_TO_LATIN_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_to_latin_alphabet_logger.addHandler(fh)
        test_moroccan_to_latin_alphabet_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_to_latin.iterrows():
            expected_result, moroccan_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic_to_latin(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_to_latin_alphabet_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_to_latin_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_latin)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_latin)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_TO_LATIN_ALPHABET_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_latin)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_latin)*100, 2)}%)')

    # Test moroccan arabic to latin alphabet
    def test_moroccan_arabic_to_latin_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_arabic_to_latin_alphabet_logger.addHandler(fh)
        test_moroccan_arabic_to_latin_alphabet_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_arabic_to_latin.iterrows():
            expected_result, moroccan_arabic_transliteration = row["Expected Result"], _transliterate_moroccan_to_moroccan_arabic_arabic_to_latin(row["Test Case"])
            try:
                self.assertEqual(expected_result, moroccan_arabic_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError) as e:
                test_moroccan_arabic_to_latin_alphabet_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_arabic_to_latin_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_latin)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_latin)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_arabic_to_latin)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_arabic_to_latin)*100, 2)}%)')

def run_tests():
    unittest.main()