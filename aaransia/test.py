"""This script is dedicated to test the 3aransia transliteration function"""

import unittest
import logging

import pandas as pd

from aaransia.transliteration import transliterate
from aaransia.exceptions import SourceLanguageError
from aaransia.defaults import (BASE_DIR, LOG_DIR, TEST_DIR, DATA_DIR, MOROCCAN_ALPHABET,
                               ARABIAN_ALPHABET, EXPECTED_RESULT, TEST_MOROCCAN_ALPHABET,
                               DICTIONARY_FILE, TEST_MOROCCAN_WORDS, TEST_STATS_LOGGER_NAME,
                               TEST_MOROCCAN_ALPHABET_LOGGER_NAME, TEST_MOROCCAN_WORDS_LOGGER_NAME,
                               TEST_STATS_LOG_FILE, TEST_MOROCCAN_ALPHABET_LOG_FILE,
                               MOROCCAN_ALPHABET_CODE, ARABIAN_ALPHABET_CODE, TEST_CASE,
                               ALPHABET_FILE)

def build_moroccan_alphabet_test_file():
    """This function is dedicated to build the moroccan alphabet test file"""
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET_FILE)
    alphabet_test = alphabet.rename(columns={
        MOROCCAN_ALPHABET:TEST_CASE,
        ARABIAN_ALPHABET:EXPECTED_RESULT})
    alphabet_test = alphabet_test[[TEST_CASE, EXPECTED_RESULT]]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET, index=False)

def build_moroccan_words_test_file():
    """This function is dedicated to build the moroccan words test file"""
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_FILE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic', 'French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
        'Moroccan':TEST_CASE,
        'Moroccan Arabic':EXPECTED_RESULT})
    moroccan_words_test = moroccan_words_test[[TEST_CASE, EXPECTED_RESULT]]
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS, index=False)

# Refresh test files based on the csv data
build_moroccan_alphabet_test_file()
build_moroccan_words_test_file()

# Logging config
logging.root.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
TEST_STATS_LOGGER = logging.getLogger(TEST_STATS_LOGGER_NAME)

TEST_MOROCCAN_ALPHABET_LOGGER = logging.getLogger(TEST_MOROCCAN_ALPHABET_LOGGER_NAME)
TEST_MOROCCAN_WORDS_LOGGER = logging.getLogger(TEST_MOROCCAN_WORDS_LOGGER_NAME)

# Test sets
TEST_ALPHABET = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET)
TEST_WORDS = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS)

# Test statistics logger
STATS_LOGGER_FILE_HANDLER = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_STATS_LOG_FILE, 'a')
STATS_LOGGER_FILE_HANDLER.setFormatter(FORMATTER)
STATS_LOGGER_FILE_HANDLER.setLevel(logging.INFO)
TEST_STATS_LOGGER.addHandler(STATS_LOGGER_FILE_HANDLER)
TEST_STATS_LOGGER.info('\n')

class TestSequenceFunctions(unittest.TestCase):
    """This class is meant for test purposes"""

    def test_moroccan_alphabet_transliteration(self):
        """This script is dedicated to test the moroccan alphabet transliteration

        @self -- the instance of the testing class"""
        alphabet_logger_file_handler = logging.FileHandler(BASE_DIR + LOG_DIR +
                                                           TEST_MOROCCAN_ALPHABET_LOG_FILE, 'w')
        alphabet_logger_file_handler.setFormatter(FORMATTER)
        alphabet_logger_file_handler.setLevel(logging.INFO)
        TEST_MOROCCAN_ALPHABET_LOGGER.addHandler(alphabet_logger_file_handler)
        TEST_MOROCCAN_ALPHABET_LOGGER.info('Transliteration of [item to test] '
                                           '([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for _, row in TEST_ALPHABET.iterrows():
            try:
                expected_result = row["Expected Result"]
                moroccan_transliteration = transliterate(row["Test Case"],
                                                         MOROCCAN_ALPHABET_CODE,
                                                         ARABIAN_ALPHABET_CODE)
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except SourceLanguageError as source_language_error:
                TEST_MOROCCAN_ALPHABET_LOGGER.error('Transliteration of %s, %s',
                                                    row["Test Case"], source_language_error)
            except AssertionError as assertion_error:
                TEST_MOROCCAN_ALPHABET_LOGGER.error('Transliteration of %s, %s',
                                                    row["Test Case"], assertion_error)
                count_errors += 1
        info_percentage = round(count_infos/len(TEST_ALPHABET)*100, 2)
        error_percentage = round(count_errors/len(TEST_ALPHABET)*100, 2)
        TEST_MOROCCAN_ALPHABET_LOGGER.info(f'Total INFO logs {count_infos} ({info_percentage}%), '
                                           f'Total ERROR logs {count_errors} ({error_percentage}%)')
        TEST_STATS_LOGGER.info(f'{TEST_MOROCCAN_ALPHABET_LOGGER_NAME} - '
                               f'Total INFO logs {count_infos} ({info_percentage}%), '
                               f'Total ERROR logs {count_errors} ({error_percentage}%)')

def run_tests():
    """This function is meant to run all the tests"""
    unittest.main()
