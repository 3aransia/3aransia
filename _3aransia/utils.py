import pandas as pd
from _3aransia.constants import *

def build_dictionary():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + '/open_dictionary.csv')
    moroccan_words_min = moroccan_words.drop(columns=['Latin/Digit Arabic'])
    moroccan_words_min.to_csv(BASE_DIR + DATA_DIR + '/dictionary.csv', index=False)