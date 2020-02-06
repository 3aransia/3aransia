import sys
import operator

import pandas as pd
import numpy as np
import nltk

from aaransia.constants import *
from aaransia.utils import *

traning_data = pd.read_csv(BASE_DIR + DATA_DIR + TRANING_DATA)

# Model to guess the moroccan L/D

## Tokenization
moroccan_words_tokens_x = {word : i for (i, word) in enumerate(traning_data["Moroccan"])}
moroccan_words_tokens_y = {word : i for (i, word) in enumerate(traning_data["Moroccan Arabic"])}

# # Padding 
# measurer = np.vectorize(len)
# max_length_x = measurer(moroccan_words_tokens_x.values.astype(str)).max(axis=0)



# Function to run the machine leatning algorithms
def run_machine_learning():
    # print(get_tokens("oustouraliya almaniya", moroccan_tokens))
    print(max(moroccan_words_tokens_x.items(), key=lambda x:len(x)))
    print(max(moroccan_words_tokens_y.items(), key=lambda y:len(y)))
