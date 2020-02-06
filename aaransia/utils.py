import re

import pandas as pd

from aaransia.constants import *

# Build test moroccan alphabet file
def build_test_alphabet_ma_ar_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET)
    alphabet_test = alphabet.rename(columns={
                          'Moroccan Alphabet':'Test Case',
                          'Arabian Alphabet':'Expected Result'})
    alphabet_test = alphabet_test[['Test Case', 'Expected Result']]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_ALPHABET_MA_AR, index=False)

# Build Test moroccan words File
def build_test_words_ma_ar_file():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_SAMPLE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic','French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
                          'Moroccan':'Test Case',
                          'Moroccan Arabic':'Expected Result'})
    moroccan_words_test = moroccan_words_test[['Test Case', 'Expected Result']]
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_WORDS_MA_AR, index=False)

# Build test arabian alphabet file
def build_test_alphabet_ar_ma_file():
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET)
    alphabet_test = alphabet.rename(columns={
                          'Arabian Alphabet':'Test Case',
                          'Moroccan Alphabet':'Expected Result'})
    alphabet_test = alphabet_test[['Test Case', 'Expected Result']]
    alphabet_test.to_csv(BASE_DIR + TEST_DIR + TEST_ALPHABET_AR_MA, index=False)

# Build Test arabian words File
def build_test_words_ar_ma_file():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + DICTIONARY_SAMPLE)
    moroccan_words_test = moroccan_words.drop(columns=['Arabic','French', 'English'])
    moroccan_words_test = moroccan_words_test.rename(columns={
                          'Moroccan Arabic':'Test Case',
                          'Moroccan':'Expected Result'})
    moroccan_words_test = moroccan_words_test[['Test Case', 'Expected Result']]
    moroccan_words_test.to_csv(BASE_DIR + TEST_DIR + TEST_WORDS_AR_MA, index=False)

# Remove noise from arabic text
def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text

# Normalize arabic
def normalizeArabic(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    return(text)
