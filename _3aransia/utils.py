import pandas as pd

from _3aransia.constants import *

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