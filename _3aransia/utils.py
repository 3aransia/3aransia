import pandas as pd
from _3aransia.constants import *

# Build test alphabet file
def build_test_alphabet_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET)
    alphabet_test = alphabet.rename(columns={
                          'Moroccan Alphabet':'Test Case',
                          'Arabian Alphabet':'Expected Result'})
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_ALPHABET, index=False)

# Build Test words File
def build_test_words_file():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_SAMPLE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic','French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
                          'Moroccan':'Test Case',
                          'Moroccan Arabic':'Expected Result'})
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_WORDS, index=False)