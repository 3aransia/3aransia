import pandas as pd

from _3aransia.constants import *

# Word counter
def word_count(_str):
    return {word: _str.count(word) for word in _str.split()}

# Get duplicated
def generate_duplicates(_str):
    return dict(filter(lambda x:x[1] > 1, word_count(_str).items()))

# Function to compute the distance between two words
def word_distance(word_1, word_2):
    return nltk.edit_distance(word_1, word_2)

# Generate lexically close words
def generate_close_words(threshold, _str):
    words = set()
    for w in _str.split():
        for y in _str.split():
            if w != y and word_distance(w,y) < threshold: 
                words.add((w,y, word_distance(w,y)))
    return sorted(words, key=lambda x:len(x[0]))

# Function to build training data
def build_training_data():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + OPEN_DICTIONARY_SAMPLE)
    moroccan_alphabet = pd.read_csv(BASE_DIR + DATA_DIR + MOROCCAN_ALPHABET)
    moroccan_words_min = moroccan_words.drop(columns=['Arabic', 'French', 'Latin/Digit Arabic'])
    data = []
    for i, letter in moroccan_alphabet.iterrows():
        data.append([letter[0], letter[1]])
        data.append([letter[0], letter[2]])
        data.append([letter[0], letter[3]])
        data.append([letter[0], letter[4]])
    moroccan_alphabet_min = pd.DataFrame(data, columns = ['Moroccan', 'Moroccan Arabic'])
    training_data_set = pd.concat([moroccan_alphabet_min, moroccan_words_min], axis=0)
    print(training_data_set.to_csv(index=False))
