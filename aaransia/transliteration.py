import re

import unidecode
import pandas as pd
import numpy as np

from aaransia.defaults import *
from aaransia.utils import *
from aaransia.exceptions import *

# Importing the alphabet
alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET)

# Return available alphabets code
def get_alphabets_codes():
    return list(ALPHABETS)

# Transliteration of a Moroccan letter to an Arabian letter
def _moroccan_letter_to_moroccan_arabic_letter(letter, position, word): 
    if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')) and position == 0: return 'ا'
    elif (letter in ('o', 'e')) and position > 0: return ''
    else: return alphabet.loc[alphabet[MOROCCAN_ALPHABET] == letter][ARABIAN_ALPHABET].values[0]

# Transliteration of an Arabic letter to an Moroccan letter
def _moroccan_arabic_letter_to_moroccan_letter(letter, position, word): 
    return alphabet.loc[alphabet[ARABIAN_ALPHABET] == normalize_arabic(de_noise(letter))][MOROCCAN_ALPHABET].values[0]

# Transliterate letter
def _transliterate_letter(letter, source_language, target_language):
    try:
        return alphabet.loc[alphabet[ALPHABETS[source_language]] == letter][ALPHABETS[target_language]].values[0]
    except IndexError:
        raise SourceLanguageException

# Transliteration of Moroccan to Moroccan Arabic
def transliterate_moroccan(text):
    moroccan_arabic_transliteration = list()
    for word in text.split():
        if word.isdigit(): moroccan_arabic_transliteration.append(word)
        else:
            arabian_word, word, word_iterator = [], unidecode.unidecode(word.lower()), iter(range(len(word)))
            for i in word_iterator:
                if i < len(word) - 1:
                    if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                        arabian_word.append(_moroccan_letter_to_moroccan_arabic_letter(word[i:i+2], i, word))
                        next(word_iterator)
                    elif word[i] == word[i+1]:
                        arabian_word.append(_moroccan_letter_to_moroccan_arabic_letter(word[i], i, word))
                        next(word_iterator)
                    else: arabian_word.append(_moroccan_letter_to_moroccan_arabic_letter(word[i], i, word))
                else: arabian_word.append(_moroccan_letter_to_moroccan_arabic_letter(word[i], i, word))
            moroccan_arabic_transliteration.append(u''.join(arabian_word).replace(u'\u200e', ''))
    moroccan_arabic_transliteration = u' '.join(moroccan_arabic_transliteration)
    return moroccan_arabic_transliteration

# Transliteration of Moroccan Arabic to Moroccan
def transliterate_moroccan_arabic(text):
    text, moroccan_transliteration = normalize_arabic(de_noise(text)), list()
    str_iterator = iter(text.split())
    for word in str_iterator:
        if word.isdigit(): moroccan_transliteration.append(word)
        else: 
            moroccan_word, word_iterator = [], iter(range(len(word))) 
            for i in word_iterator:
                if i < len(word) - 1:
                    if word[i:i+2] in DOUBLE_MOROCCAN_ARABIC_LETTERS:
                        moroccan_word.append(_moroccan_arabic_letter_to_moroccan_letter(word[i:i+2], i, word))
                        next(word_iterator)
                    else: moroccan_word.append(_moroccan_arabic_letter_to_moroccan_letter(word[i], i, word))
                else: moroccan_word.append(_moroccan_arabic_letter_to_moroccan_letter(word[i], i, word))
            moroccan_transliteration.append(''.join(moroccan_word))
    moroccan_transliteration = ' '.join(moroccan_transliteration)
    return moroccan_transliteration

# Transliteration
def transliterate(text, source_language, target_language):
    try:
        return ''.join(list(map(lambda l: _transliterate_letter(l, source_language, target_language), text)))
    except SourceLanguageException:
        raise SourceLanguageException(f'{SOURCE_LANGUAGE_EXCEPTION} {source_language}')