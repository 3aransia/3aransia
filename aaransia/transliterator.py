import re

import unidecode
import pandas as pd
import numpy as np

from aaransia.constants import *
from aaransia.utils import *

# Transliterate a Moroccan letter to an Arabian letter
def _morrocan_letter_to_arabian(letter, position, word): 
    if ((letter in 'o' and len(word) > 1) or letter in ('a', 'ou')) and position == 0: return 'أ'
    elif (letter in ('i', 'e')) and position == 0: return 'إ'
    elif (letter in ('o', 'e')) and position > 0: return ''
    else: return moroccan_alphabet[letter.lower()][0]

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    arabian_translation = list()
    for word in _str.split():
        if word.isdigit(): arabian_translation.append(word)
        else:
            arabian_word, word, word_iterator = [], unidecode.unidecode(word.lower()), iter(range(len(word)))
            for i in word_iterator:
                if i < len(word) - 1:
                    if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                        arabian_word.append(_morrocan_letter_to_arabian(word[i:i+2], i, word))
                        next(word_iterator)
                    elif word[i] == word[i+1]:
                        arabian_word.append(_morrocan_letter_to_arabian(word[i], i, word))
                        next(word_iterator)
                    else: arabian_word.append(_morrocan_letter_to_arabian(word[i], i, word))
                else: arabian_word.append(_morrocan_letter_to_arabian(word[i], i, word))
            arabian_translation.append(u''.join(arabian_word).replace(u'\u200e', ''))
    arabian_translation = u' '.join(arabian_translation)
    return arabian_translation

# Transliterate a Arabic letter to an Moroccan letter
def _moroccan_arabic_letter_to_moroccan(letter, position, word): 
    return moroccan_arabic_alphabet[normalize_arabic(de_noise(letter))][0]

# Transliteration from arabic to moroccan
def moroccan_arabic_to_moroccan(_str):
    _str, moroccan_translation = normalize_arabic(de_noise(_str)), list()
    str_iterator = iter(_str.split())
    for word in str_iterator:
        if word.isdigit(): 
            moroccan_translation.append(word)
        else: 
            moroccan_word, word_iterator = [], iter(range(len(word))) 
            for i in word_iterator:
                moroccan_word.append(_moroccan_arabic_letter_to_moroccan(word[i], i, word))
            moroccan_translation.append(''.join(moroccan_word))
    moroccan_translation = ' '.join(moroccan_translation)
    return moroccan_translation