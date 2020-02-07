"""
This loads the pickled Aramorpher object, making it available to do analysis
Run this first:
> python make_pickle.py
"""
import pickle
import os
import sys

import aaransia.aramorpher
from aaransia.constants import *

with open(BASE_DIR + DATA_DIR + ANAMORPH_DATA, "rb") as f:
    ai = pickle.load(f) 
