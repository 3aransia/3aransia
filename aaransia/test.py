"""This script is dedicated to test the 3aransia transliteration function"""

import unittest
import logging

from aaransia.transliteration import transliterate
from aaransia.exceptions import SourceLanguageError
from aaransia.text_samples import TEXT_SAMPLES
from aaransia.defaults import (
    BASE_DIR, LOG_DIR, TEST_LOGGER_NAME, TEST_TRANSLITERATION_LOG_FILE, ALPHABETS,
    LEN_LANGUAGES
)

# Logging config
logging.root.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Loggers
TEST_LOGGER = logging.getLogger(TEST_LOGGER_NAME)

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

        for text_sample in TEXT_SAMPLES:
            count_infos, count_errors = 0, 0
            for word in text_sample['text'].split():
                try:
                    for target_language in list(ALPHABETS):
                        transliteration = transliterate(word,
                                                        text_sample['language'],
                                                        target_language)
                        count_infos += 1
                except SourceLanguageError as source_language_error:
                    TEST_LOGGER.error(f'{text_sample["language"].capitalize()} - '
                                      f'Transliteration of {word}, '
                                      f'{source_language_error}')
                    count_errors += 1

            info_percentage = round(count_infos/len(text_sample['text'].split())*100/LEN_LANGUAGES, 2)
            error_percentage = round(count_errors/len(text_sample['text'].split())*100, 2)

            TEST_LOGGER.info(f'{text_sample["language"].capitalize()} - '
                             f'Total INFO logs {count_infos/LEN_LANGUAGES} '
                             f'({info_percentage}%), \n\t'
                             f'Total ERROR logs {count_errors} '
                             f'({error_percentage}%)')

def run_tests():
    """This function is meant to run all the tests"""
    unittest.main()
