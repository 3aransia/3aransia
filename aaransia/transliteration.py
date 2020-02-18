import re

import unidecode
import pandas as pd
import numpy as np

from aaransia.constants import *
from aaransia.utils import *

# Transliteration of a Moroccan letter to an Arabian letter
def _moroccan_letter_to_moroccan_arabic_letter(letter, position, word): 
    if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')) and position == 0: return 'ا'
    elif (letter in ('o', 'e')) and position > 0: return ''
    else: return moroccan_alphabet[letter.lower()][0]

# Transliteration of an Arabic letter to an Moroccan letter
def _moroccan_arabic_letter_to_moroccan_letter(letter, position, word): 
    return moroccan_arabic_alphabet[normalize_arabic(de_noise(letter))][0]

# Transliteration of a Moroccan letter to a Latin letter
def _moroccan_letter_to_latin_letter(letter): 
    return moroccan_to_latin_alphabet[letter.lower()][0]

# Transliteration of a Moroccan Arabic letter to a Latin letter
def _moroccan_arabic_letter_to_latin_letter(letter): 
    return moroccan_arabic_to_latin_alphabet[letter.lower()][0]

# Transliteration of Moroccan to Moroccan Arabic
def transliterate_moroccan(_str):
    moroccan_arabic_transliteration = list()
    for word in _str.split():
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
def transliterate_moroccan_arabic(_str):
    _str, moroccan_transliteration = normalize_arabic(de_noise(_str)), list()
    str_iterator = iter(_str.split())
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

# Transliteration of Moroccan to Latin
def transliterate_moroccan_to_latin(_str):
    return ''.join(list(map(_moroccan_letter_to_latin_letter, _str)))

# Transliteration of Moroccan Arabic to Latin
def transliterate_moroccan_arabic_to_latin(_str):
    return ''.join(list(map(_moroccan_arabic_letter_to_latin_letter, _str)))