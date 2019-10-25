import sys

import pandas as pd
import numpy as np
import nltk

from constants import *

# Translate a Moroccan letter to an Arabian letter
def morrocan_letter_to_arabian_letter(letter, position, word_length): 
    alphabet = pd.read_csv('data/' + MOROCCAN_ALPHABET)
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

# Translate Moroccan to Arabic
def moroccan_to_arabic(_str):
    alphabet = pd.read_csv('data/' + MOROCCAN_ALPHABET)
    arabian_translation = []
    for word in _str.split():
        arabian_word = []
        word_iterator = iter(range(len(word.lower())))
        for i in word_iterator:
            if word[i] in ['c'] and i+1 != len(word) and word[i+1] == 'h':
                arabian_word.append(morrocan_letter_to_arabian_letter('ch', i , len(word)))
                next(word_iterator)
            elif word[i] in ['k'] and i+1 != len(word) and word[i+1] == 'h':
                arabian_word.append(morrocan_letter_to_arabian_letter('kh', i, len(word)))
                next(word_iterator)
            elif word[i] in ['s'] and i+1 != len(word) and word[i+1] == 'h':
                arabian_word.append(morrocan_letter_to_arabian_letter('sh', i, len(word)))
                next(word_iterator)
            else:
                if i != len(word) - 1 and i+1 == len(word) - 1 and word[i+1] == 'e' and (word[i-1] in ['d', 'a', 'o', 'w', 'r', 'z', 'u']):
                    arabian_word.append(morrocan_letter_to_arabian_letter(word[i], -1, len(word)))
                elif i != len(word) - 1 and i+1 == len(word) - 1 and word[i+1] == 'e':
                    arabian_word.append(morrocan_letter_to_arabian_letter(word[i], len(word), len(word)))
                elif i > 0 and (word[i-1] in ['d', 'a', 'o', 'w', 'r', 'z', 'u']):
                    arabian_word.append(morrocan_letter_to_arabian_letter(word[i], 0, len(word)))
                else:
                    arabian_word.append(morrocan_letter_to_arabian_letter(word[i], i, len(word)))
        arabian_translation.append((word, (u''.join(arabian_word).replace(u'\u200e', ''))))
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
#     print(word_to_substitute('7alwa'))
#     print(word_to_substitute('9o9o'))
#     print(validate_dictionary('data/' + OPEN_DICTIONARY))
#     print(word_distance("7alwa", "halwa"))
#     print(word_distance("Halwa", "halwa"))
    moroccan_words = pd.read_csv('data/' + OPEN_DICTIONARY)
#     print(generate_close_words(2, ' '.join(moroccan_words["LDM"])))
    print(moroccan_to_arabic(' '.join(moroccan_words["LDM"])))


run_tests()