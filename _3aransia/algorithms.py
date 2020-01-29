import sys

import pandas as pd
import numpy as np
import nltk

from _3aransia.constants import *

# Translate a Moroccan letter to an Arabian letter
def morrocan_letter_to_arabian(letter, position, word_length): 
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    try:
        if position == 0:
            values = alphabet.loc[alphabet['MoroccanAlphabet'] == letter]['BeginningofWord']
            return values.values[0]
        elif position == word_length:
            values = alphabet.loc[alphabet['MoroccanAlphabet'] == letter]['EndofWord']
            return values.values[0]
        elif position == -1:
            values = alphabet.loc[alphabet['MoroccanAlphabet'] == letter]['ArabianAlphabet']
            return values.values[0]
        elif position > 0:
            values = alphabet.loc[alphabet['MoroccanAlphabet'] == letter]['MiddleofWord']
            return values.values[0]
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)

# Translate Moroccan double letter to Arabian letter
def moroccan_double_letter_to_arabian(double_letter, position, word):
    for i in range(len(word)):
        if double_letter == 'la':
            return morrocan_letter_to_arabian('la', i , len(word))
        elif double_letter == 'ch':
            return morrocan_letter_to_arabian('ch', i , len(word))
        elif double_letter == 'kh':
            return morrocan_letter_to_arabian('kh', i, len(word))
        elif double_letter == 'sh':
            return morrocan_letter_to_arabian('sh', i, len(word))
        elif double_letter == 'gh':
            return morrocan_letter_to_arabian('gh', i, len(word))
        elif double_letter == 'ou':
            return morrocan_letter_to_arabian('ou', i, len(word))

# Translate duplicate Moroccan letter to Arabian letter
def moroccan_duplicate_letter_to_arabian(duplicate_letter, position, word):
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    for i in range(len(word)):
         if duplicate_letter in DUPLICATE_MOROCCAN_LETTERS:
            return morrocan_letter_to_arabian(duplicate_letter, i , len(word))

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    arabian_translation = list()
    for word in _str.split():
        moroccan_translation_object, arabian_word, word, word_iterator = dict(), [], word.lower(), iter(range(len(word)))
        for i in word_iterator:
            if i == 0:
                if word[:2] in DOUBLE_MOROCCAN_LETTERS:
                    arabian_word.append(moroccan_double_letter_to_arabian(word[0:2], 0, word))
                    next(word_iterator)
                elif word[:2] in DUPLICATE_MOROCCAN_LETTERS:
                    arabian_word.append(moroccan_duplicate_letter_to_arabian(word[0:2], 0, word))
                    next(word_iterator)
                else:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], 0, len(word)))
            
            elif i == len(word)-1:
                arabian_word.append(morrocan_letter_to_arabian(word[i], -1, len(word)))
            
            elif i > 0 and (word[i-1] in MOROCCAN_ENDING_LETTERS):
                if (i+2 <= len(word)-1 and word[i+2] == 'e') or i == len(word)-2:
                    if i+1 < len(word)-1 and (word[i:i+2] in DOUBLE_MOROCCAN_LETTERS):
                        arabian_word.append(moroccan_double_letter_to_arabian(word[i:i+2], -1, word))
                        next(word_iterator)
                    elif i+1 < len(word)-1 and (word[i:i+2] in DUPLICATE_MOROCCAN_LETTERS):
                        arabian_word.append(moroccan_duplicate_letter_to_arabian(word[i:i+2], -1, word))
                        next(word_iterator)
                    else:
                        arabian_word.append(morrocan_letter_to_arabian(word[i], -1, len(word)))
                elif (i+1 <= len(word)-1 and word[i+1] == 'e') or i == len(word)-1:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], -1, len(word)))
                else:
                    if i+1 < len(word)-1 and (word[i:i+2] in DOUBLE_MOROCCAN_LETTERS):
                        arabian_word.append(moroccan_double_letter_to_arabian(word[i:i+2], 0, word))
                        next(word_iterator)
                    elif i+1 < len(word)-1 and (word[i:i+2] in DUPLICATE_MOROCCAN_LETTERS):
                        arabian_word.append(moroccan_duplicate_letter_to_arabian(word[i:i+2], 0, word))
                        next(word_iterator)
                    else:
                        arabian_word.append(morrocan_letter_to_arabian(word[i], 0, len(word)))
            
            elif i < len(word)-2 and i+2 == len(word)-1 and word[i+2] == 'e':
                if i+1 < len(word)-1 and (word[i:i+2] in DOUBLE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_double_letter_to_arabian(word[i:i+2], i, word))
                    next(word_iterator)
                elif i+1 < len(word)-1 and (word[i:i+2] in DUPLICATE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_duplicate_letter_to_arabian(word[i:i+2], i, word))
                    next(word_iterator)
                else:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], i, len(word)))
            
            elif i < len(word)-1 and i+1 == len(word)-1 and word[i+1] == 'e':
                arabian_word.append(morrocan_letter_to_arabian(word[i], len(word), len(word)))
            
            elif i > 1 and (word[i-2] in MOROCCAN_ENDING_LETTERS) and word[i-1] == 'e':
                if i+1 < len(word)-1 and (word[i:i+2] in DOUBLE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_double_letter_to_arabian(word[i:i+2], -1, word))
                    next(word_iterator)
                elif i+1 < len(word)-1 and (word[i:i+2] in DUPLICATE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_duplicate_letter_to_arabian(word[i:i+2], -1, word))
                    next(word_iterator)
                else:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], -1, len(word)))
            
            else:
                if i+1 < len(word)-1 and (word[i:i+2] in DOUBLE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_double_letter_to_arabian(word[i:i+2], i, word))
                    next(word_iterator)
                elif i+1 < len(word)-1 and (word[i:i+2] in DUPLICATE_MOROCCAN_LETTERS):
                    arabian_word.append(moroccan_duplicate_letter_to_arabian(word[i:i+2], i, word))
                    next(word_iterator)
                else:
                    arabian_word.append(morrocan_letter_to_arabian(word[i], i, len(word)))
        try:
            moroccan_translation_object = {'moroccan_word' : word, 'arabian_word' : (u''.join(arabian_word).replace(u'\u200e', ''))}
            arabian_translation.append(moroccan_translation_object)
        except TypeError as e:
            print(e, word)
    return arabian_translation

