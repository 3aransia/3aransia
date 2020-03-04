"""This script is dedicated to test the 3aransia transliteration function"""

import unittest
import logging

import pandas as pd

from aaransia.transliteration import transliterate
from aaransia.exceptions import SourceLanguageError
from aaransia.text_samples import TEXT_SAMPLES
from aaransia.defaults import (
    BASE_DIR, LOG_DIR, TEST_DIR, DATA_DIR, TEST_STATS_LOGGER_NAME, TEST_TRANSLITERATION_LOGGER_NAME,
    TEST_STATS_LOG_FILE, MOROCCAN_ALPHABET_CODE, TEST_TRANSLITERATION_LOG_FILE, ALPHABET_CODE_LIST
)

# Logging config
logging.root.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
TEST_STATS_LOGGER = logging.getLogger(TEST_STATS_LOGGER_NAME)
TEST_TRANSLITERATION_LOGGER = logging.getLogger(TEST_TRANSLITERATION_LOGGER_NAME)

# Test statistics logger
STATS_LOGGER_FILE_HANDLER = logging.FileHandler(BASE_DIR + LOG_DIR + TEST_STATS_LOG_FILE, 'w')
STATS_LOGGER_FILE_HANDLER.setFormatter(FORMATTER)
STATS_LOGGER_FILE_HANDLER.setLevel(logging.INFO)

TEST_STATS_LOGGER.addHandler(STATS_LOGGER_FILE_HANDLER)

class TestTransliteration(unittest.TestCase):
    """This class is meant for test purposes"""

    def test_transliteration(self):
        """This script is dedicated to test the moroccan alphabet transliteration

        @self -- the instance of the testing class"""
        transliteration_logger_file_handler = logging.FileHandler(BASE_DIR + LOG_DIR +
                                                           TEST_TRANSLITERATION_LOG_FILE, 'w')
        transliteration_logger_file_handler.setFormatter(FORMATTER)
        transliteration_logger_file_handler.setLevel(logging.INFO)
        TEST_TRANSLITERATION_LOGGER.addHandler(transliteration_logger_file_handler)

        count_infos, count_errors = 0, 0
        for i in range(len(TEXT_SAMPLES)):
            for word in TEXT_SAMPLES[i].split():
                try:
                    for target_language in ALPHABET_CODE_LIST:
                        TEST_TRANSLITERATION_LOGGER.info(f'Transliteration of {word} '
                                                         f'({ALPHABET_CODE_LIST[i]} ==> {target_language}), '
                                                         f'{transliterate(word, ALPHABET_CODE_LIST[i], target_language)}')
                        count_infos += 1
                except SourceLanguageError as source_language_error:
                    TEST_TRANSLITERATION_LOGGER.error(f'Transliteration of {word}, '
                                                    f'{source_language_error}')
                    count_errors += 1

            info_percentage = round(count_infos/len(TEXT_SAMPLES[i].split())*100, 2)
            error_percentage = round(count_errors/len(TEXT_SAMPLES[i].split())*100, 2)

            TEST_TRANSLITERATION_LOGGER.info(f'Total INFO logs {count_infos} ({info_percentage}%), '
                                            f'Total ERROR logs {count_errors} ({error_percentage}%)')

            TEST_STATS_LOGGER.info(f'{TEST_TRANSLITERATION_LOGGER_NAME} - {ALPHABET_CODE_LIST[i].capitalize()} '
                                f'Transliteration - '
                                f'Total INFO logs {count_infos} ({info_percentage}%), '
                                f'Total ERROR logs {count_errors} ({error_percentage}%)')

def run_tests():
    """This function is meant to run all the tests"""
    unittest.main()
