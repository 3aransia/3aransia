"""This script is dedicated to test the 3aransia transliteration function"""

import unittest
import logging

from aaransia.transliteration import transliterate
from aaransia.exceptions import SourceLanguageError
from aaransia.text_samples import TEXT_SAMPLES
from aaransia.defaults import (
    BASE_DIR, LOG_DIR, TEST_STATS_LOGGER_NAME, TEST_LOGGER_NAME,
    TEST_STATS_LOG_FILE, TEST_TRANSLITERATION_LOG_FILE, ALPHABET_CODE_LIST,
    LEN_LANGUAGES
)

# Logging config
logging.root.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
TEST_STATS_LOGGER = logging.getLogger(TEST_STATS_LOGGER_NAME)
TEST_LOGGER = logging.getLogger(TEST_LOGGER_NAME)

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
        test_logget_file_handler = logging.FileHandler(BASE_DIR + LOG_DIR +
                                                       TEST_TRANSLITERATION_LOG_FILE, 'w')
        test_logget_file_handler.setFormatter(FORMATTER)
        test_logget_file_handler.setLevel(logging.INFO)
        TEST_LOGGER.addHandler(test_logget_file_handler)

        for i, text_sample in enumerate(TEXT_SAMPLES):
            count_infos, count_errors = 0, 0
            for word in text_sample.split():
                try:
                    for target_language in ALPHABET_CODE_LIST:
                        transliteration = transliterate(word,
                                                        ALPHABET_CODE_LIST[i],
                                                        target_language)
                        TEST_LOGGER.info(f'Transliteration of {word} '
                                         f'({ALPHABET_CODE_LIST[i]} '
                                         f'==> {target_language}), '
                                         f'{transliteration}')
                        count_infos += 1
                except SourceLanguageError as source_language_error:
                    TEST_LOGGER.error(f'Transliteration of {word}, '
                                      f'{source_language_error}')
                    count_errors += 1
            
            if count_errors == 0:
                for target_language in ALPHABET_CODE_LIST:
                    text = "".join([text_sample[i:i+80]+"\n\t" 
                                    for i in range(0, len(text_sample), 80)])
                    text_transliteration = transliterate(text_sample,
                                                         ALPHABET_CODE_LIST[i],
                                                         target_language)
                    text_transliteration = "".join([text_transliteration[i:i+80]+"\n\t" 
                                                           for i in range(0, len(text_transliteration), 80)])
                    TEST_LOGGER.info(f'Transliteration of '
                                    f'({ALPHABET_CODE_LIST[i]} '
                                    f'==> {target_language})\n\t'
                                    f'{text}==> '
                                    f'\n\t{text_transliteration}')

            info_percentage = round(count_infos/len(text_sample.split())*100/LEN_LANGUAGES, 2)
            error_percentage = round(count_errors/len(text_sample.split())*100, 2)

            TEST_LOGGER.info(f'Total INFO logs {count_infos/LEN_LANGUAGES} '
                             f'({info_percentage}%), \n\t'
                             f'Total ERROR logs {count_errors} '
                             f'({error_percentage}%)')

            TEST_STATS_LOGGER.info(f'{TEST_LOGGER_NAME} - {ALPHABET_CODE_LIST[i].capitalize()}\n\t'
                                   f'Transliteration - '
                                   f'Total INFO logs {count_infos/LEN_LANGUAGES} '
                                   f'({info_percentage}%), '
                                   f'Total ERROR logs {count_errors} ({error_percentage}%)')

def run_tests():
    """This function is meant to run all the tests"""
    unittest.main()
