import re

import unidecode
import pandas as pd
import numpy as np

from aaransia.constants import *
from aaransia.utils import *

# Transliterate a Moroccan letter to an Arabian letter
def _morrocan_letter_to_moroccan_arabic_letter(letter, position, word): 
    if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')) and position == 0: return 'ا'
    elif (letter in ('o', 'e')) and position > 0: return ''
    else: return moroccan_alphabet[letter.lower()][0]

# Translate Moroccan to Arabic
def transliterate_moroccan(_str):
    moroccan_arabic_translation = list()
    for word in _str.split():
        if word.isdigit(): moroccan_arabic_translation.append(word)
        else:
            arabian_word, word, word_iterator = [], unidecode.unidecode(word.lower()), iter(range(len(word)))
            for i in word_iterator:
                if i < len(word) - 1:
                    if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                        arabian_word.append(_morrocan_letter_to_moroccan_arabic_letter(word[i:i+2], i, word))
                        next(word_iterator)
                    elif word[i] == word[i+1]:
                        arabian_word.append(_morrocan_letter_to_moroccan_arabic_letter(word[i], i, word))
                        next(word_iterator)
                    else: arabian_word.append(_morrocan_letter_to_moroccan_arabic_letter(word[i], i, word))
                else: arabian_word.append(_morrocan_letter_to_moroccan_arabic_letter(word[i], i, word))
            moroccan_arabic_translation.append(u''.join(arabian_word).replace(u'\u200e', ''))
    moroccan_arabic_translation = u' '.join(moroccan_arabic_translation)
    return moroccan_arabic_translation

# Transliterate a Arabic letter to an Moroccan letter
def _moroccan_arabic_letter_to_moroccan_letter(letter, position, word): 
    return moroccan_arabic_alphabet[normalize_arabic(de_noise(letter))][0]

# Transliteration from arabic to moroccan
def transliterate_moroccan_arabic(_str):
    _str, moroccan_translation = normalize_arabic(de_noise(_str)), list()
    str_iterator = iter(_str.split())
    for word in str_iterator:
        if word.isdigit(): 
            moroccan_translation.append(word)
        else: 
            moroccan_word, word_iterator = [], iter(range(len(word))) 
            for i in word_iterator:
                moroccan_word.append(_moroccan_arabic_letter_to_moroccan_letter(word[i], i, word))
            moroccan_translation.append(''.join(moroccan_word))
    moroccan_translation = ' '.join(moroccan_translation)
    return moroccan_translation