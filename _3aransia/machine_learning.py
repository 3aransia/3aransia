import sys

import pandas as pd
import numpy as np
import nltk

from _3aransia.constants import *

# Function to run the machine leatning algorithm
def run_machine_learning():
    moroccan_words = pd.read_csv(BASE_DIR + DATA_DIR + OPEN_DICTIONARY_SAMPLE)  
    print(moroccan_words)


