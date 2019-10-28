import sys

import pandas as pd
import numpy as np
import nltk

from constants import *

# Translate a Moroccan letter to an Arabian letter
def morrocan_letter_to_arabian(letter, position, word_length): 
    alphabet = pd.read_csv(CURRENT_DIR + DATA_DIR + MOROCCAN_ALPHABET)
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
    alphabet = pd.read_csv(CURRENT_DIR + DATA_DIR + MOROCCAN_ALPHABET)
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
    alphabet = pd.read_csv(CURRENT_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    for i in range(len(word)):
         if duplicate_letter in DUPLICATE_MOROCCAN_LETTERS:
            return morrocan_letter_to_arabian(duplicate_letter, i , len(word))

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    alphabet = pd.read_csv(CURRENT_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    arabian_translation = list()
    for word in _str.split():
        moroccan_translation_object = dict()
        arabian_word = []
        word = word.lower()
        word_iterator = iter(range(len(word)))
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

# Translate Arabic to Moroccan
# TODO

# Function to compute the distance between two words
def word_distance(word_1, word_2):
    return nltk.edit_distance(word_1, word_2)
    
# Converte a letter to its substitute
def letter_to_substitute(l):
    if l == '7': 
        return 'h'
    if l == '9': 
        return 'q'
    else : 
        return l

# Word counter
def word_count(_str):
    counts = dict()
    words = _str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

# Get duplicated
def generate_duplicates(_str):
    return dict(filter(lambda x:x[1] > 1, word_count(_str).items()))

# Generate lexically close words
def generate_close_words(threshold, _str):
    words = set()
    for w in _str.split():
        for y in _str.split():
            if w != y and word_distance(w,y) < threshold: 
                words.add((w,y, word_distance(w,y)))
    return sorted(words, key=lambda x:len(x[0]))

# Converte a word to its substitute
def word_to_substitute(word):
    return ''.join(list(map(lambda x:letter_to_substitute(x), word)))

# Validate Latin/Digit Moroccan to Arabic dictionary
def validate_dictionary(dictionary):
    data = pd.read_csv(dictionary)
    return data
    #TODO

# Temporary function to test
def run_tests():
    moroccan_words = pd.read_csv(CURRENT_DIR + DATA_DIR + OPEN_DICTIONARY)
    print(f'Number of words to translate : {len(moroccan_to_arabic(" ".join(moroccan_words["LDM"])))}')
    for word in moroccan_to_arabic(' '.join(moroccan_words["LDM"])):
        print(word)
    
# Runnin the tests
run_tests()