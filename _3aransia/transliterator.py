import unidecode
import re

import pandas as pd
import numpy as np

from _3aransia.constants import *
from _3aransia.utils import *

alphabet = pd.read_csv(BASE_DIR + DATA_DIR + ALPHABET)

# Transliterate a Moroccan letter to an Arabian letter
def morrocan_letter_to_arabian(letter, position, word): 
    if ((letter in 'o'  and len(word) > 1) or letter in ('a', 'ou')) and position == 0: return 'أ'
    elif letter in ('i', 'e') and position == 0: return 'إ'
    elif letter == 'e' and position > 0: return ''
    else: return alphabet.loc[alphabet['Moroccan Alphabet'] == letter.lower()]['Arabian Alphabet'].values[0]

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    arabian_translation_object, arabian_translation = list(), list()
    for word in _str.split():
        if word.isdigit(): arabian_translation.append(word)
        else:
            moroccan_translation_object, arabian_word, word, word_iterator = dict(), [], unidecode.unidecode(word.lower()), iter(range(len(word)))
            for i in word_iterator:
                if i < len(word) - 1:
                    if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                        arabian_word.append(morrocan_letter_to_arabian(word[i:i+2], i, word))
                        next(word_iterator)
                    elif word[i] == word[i+1]:
                        arabian_word.append(morrocan_letter_to_arabian(word[i], i, word))
                        next(word_iterator)
                    else: arabian_word.append(morrocan_letter_to_arabian(word[i], i, word))
                else: arabian_word.append(morrocan_letter_to_arabian(word[i], i, word))
            arabian_word = u''.join(arabian_word).replace(u'\u200e', '')
            moroccan_translation_object = {'moroccan_word' : word, 'arabian_word' : arabian_word}
            arabian_translation.append(arabian_word)
            arabian_translation_object.append(moroccan_translation_object)
    arabian_translation = u' '.join(arabian_translation)
    arabian_translation_object.append({'moroccan_sentence': _str, 'arabian_translation': arabian_translation})
    return arabian_translation_object

# Transliterate a Arabic letter to an Moroccan letter
def arabian_letter_to_moroccan(letter, position, word): 
    return alphabet.loc[alphabet['Arabian Alphabet'] == letter]['Moroccan Alphabet'].values[0]

# Transliteration from arabic to moroccan
def arabic_to_moroccan(_str):
    _str = normalizeArabic(deNoise(_str))
    moroccan_translation_object, moroccan_translation = list(), list()
    str_iterator = iter(_str.split())
    for word in str_iterator:
        if word.isdigit(): 
            moroccan_translation.append(word)
        else: 
            arabian_translation_object, moroccan_word, word_iterator = dict(), [], iter(range(len(word)))
            for i in word_iterator:
                moroccan_word.append(arabian_letter_to_moroccan(word[i], i, word))
            arabian_translation_object = {'arabian_word' : word, 'moroccan_word' : ''.join(moroccan_word)}
            moroccan_translation_object.append(arabian_translation_object)
            moroccan_translation.append(''.join(moroccan_word))
    moroccan_translation = ' '.join(moroccan_translation)
    moroccan_translation_object.append({'moroccan_sentence': _str, 'moroccan_translation': moroccan_translation})
    return moroccan_translation_object