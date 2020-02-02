import unidecode

import pandas as pd
import numpy as np

from _3aransia.constants import *

alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)

# Translate a Moroccan letter to an Arabian letter
def morrocan_letter_to_arabian(letter, position): 
    if letter == 'e' and position > 0: return ''
    else: return alphabet.loc[alphabet['MoroccanAlphabet'] == letter.lower()]['ArabianAlphabet'].values[0]

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    arabian_translation = list()
    for word in _str.split():
        moroccan_translation_object, arabian_word, word, word_iterator = dict(), [], unidecode.unidecode(word.lower()), iter(range(len(word)))
        for i in word_iterator:
            if i < len(word) - 1:
                if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                    arabian_word.append(morrocan_letter_to_arabian(word[i:i+2], i))
                    next(word_iterator)
                elif word[i] == word[i+1]:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], i))
                    next(word_iterator)
                else: arabian_word.append(morrocan_letter_to_arabian(word[i], i))
            else: arabian_word.append(morrocan_letter_to_arabian(word[i], i))
        moroccan_translation_object = {'moroccan_word' : word, 'arabian_word' : u''.join(arabian_word).replace(u'\u200e', '')}
        arabian_translation.append(moroccan_translation_object)
    return arabian_translation