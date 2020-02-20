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
    
# Return available alphabets 
def get_alphabets():
    return ALPHABETS

# Transliteration of a Moroccan letter to an Arabian letter
def _moroccan_letter_to_moroccan_arabic_letter(letter, position, word): 
    try:
        if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')) and position == 0: return 'ا'
        elif (letter in ('o', 'e')) and position > 0: return ''
        else: return alphabet.loc[alphabet[MOROCCAN_ALPHABET] == letter][ARABIAN_ALPHABET].values[0]
    except IndexError:
        raise SourceLanguageException

# Transliterate letter
def _transliterate_letter(letter, source_language, target_language):
    try:
        return alphabet.loc[alphabet[ALPHABETS[source_language]] == letter][ALPHABETS[target_language]].values[0]
    except IndexError:
        raise SourceLanguageException

# Transliteration of Moroccan to Moroccan Arabic
def _transliterate_moroccan_to_moroccan_arabic(text):
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

# Transliteration
def transliterate(text, source_language, target_language):
    try:
        if source_language == MOROCCAN_ALPHABET_CODE and target_language == ARABIAN_ALPHABET_CODE:
            return _transliterate_moroccan_to_moroccan_arabic(text)
        else:
            return ''.join(list(map(lambda l: _transliterate_letter(l, source_language, target_language), text)))
    except SourceLanguageException:
        raise SourceLanguageException(f'{SOURCE_LANGUAGE_EXCEPTION}: {source_language}')