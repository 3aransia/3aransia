import pandas as pd
import nltk

# Converte a letter to its substitute
def letter_to_substitute(l):
    if l == '7': return 'h'
    elif l == '9': return 'q'
    else : return l

# Converte a word to its substitute
def word_to_substitute(word):
    return ''.join(list(map(lambda x:letter_to_substitute(x), word)))

# Validate Latin/Digit Moroccan to Arabic dictionary
def validate_dictionary(dictionary):
    data = pd.read_csv(dictionary)
    return data
    #TODO

# Function to compute the distance between two words
def word_distance(word_1, word_2):
    return nltk.edit_distance(word_1, word_2)

# Temporary function to test
def run_tests():
    print(word_to_substitute('7alwa'))
    print(word_to_substitute('9o9o'))
    print(validate_dictionary('data/dictionary.csv'))
    print(word_distance("7alwa", "halwa"))
    print(word_distance("Halwa", "halwa"))

run_tests()