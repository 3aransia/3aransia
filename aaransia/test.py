"""This script is dedicated to test the 3aransia transliteration function"""

import unittest
import logging

import pandas as pd

from aaransia.transliteration import transliterate
from aaransia.defaults import ( BASE_DIR, MOROCCAN_ALPHABET, TEST_CASE, 
                                ARABIAN_ALPHABET, EXPECTED_RESULT, TEST_DIR,
                            TEST_MOROCCAN_ALPHABET, DICTIONARY_FILE, TEST_MOROCCAN_WORDS,
                            TEST_STATS_LOGGER, TEST_MOROCCAN_ALPHABET_LOGGER, 
                            TEST_MOROCCAN_WORDS_LOGGER, LOG_DIR, TEST_STATS_LOG_FILE,
                            TEST_MOROCCAN_ALPHABET_LOG_FILE, MOROCCAN_ALPHABET_CODE,
                            ARABIAN_ALPHABET_CODE
                            )
from aaransia.utils import *
from aaransia.exceptions import SourceLanguageError

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

# Refresh test files based on the csv data
build_moroccan_alphabet_test_file()
build_moroccan_words_test_file()

# Logging config
logging.root.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
test_stats_logger = logging.getLogger(TEST_STATS_LOGGER)

test_moroccan_alphabet_logger = logging.getLogger(TEST_MOROCCAN_ALPHABET_LOGGER)
test_moroccan_words_logger = logging.getLogger(TEST_MOROCCAN_WORDS_LOGGER)

# Test sets
alphabet_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_ALPHABET)
words_moroccan_to_moroccan_arabic = pd.read_csv(BASE_DIR + TEST_DIR + TEST_MOROCCAN_WORDS)

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
    def test_moroccan_alphabet_transliteration(self):
        fh = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_MOROCCAN_ALPHABET_LOG_FILE, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)
        test_moroccan_alphabet_logger.addHandler(fh)
        test_moroccan_alphabet_logger.info(f'Transliteration of [item to test] ([expected result], [generated result result])')

        count_infos, count_errors = 0, 0

        for index, row in alphabet_moroccan_to_moroccan_arabic.iterrows():
            try:
                expected_result, moroccan_transliteration = row["Expected Result"], transliterate(row["Test Case"], MOROCCAN_ALPHABET_CODE, ARABIAN_ALPHABET_CODE)
                self.assertEqual(expected_result, moroccan_transliteration)
                count_infos += 1
            except (IndexError, KeyError, TypeError, TypeError, AssertionError, SourceLanguageError) as e:
                test_moroccan_alphabet_logger.error(f'Transliteration of {row["Test Case"]}, {e}')
                count_errors += 1
        test_moroccan_alphabet_logger.info(f'Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')
        test_stats_logger.info(f'{TEST_MOROCCAN_ALPHABET_LOGGER} - Total INFO logs {count_infos} ({round(count_infos/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%), Total ERROR logs {count_errors} ({round(count_errors/len(alphabet_moroccan_to_moroccan_arabic)*100, 2)}%)')

def run_tests():
    unittest.main()
