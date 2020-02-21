import re
import csv
import collections
import pickle

import pandas as pd

from aaransia.defaults import BASE_DIR, DATA_DIR, ALPHABET_FILE

# Remove noise from arabic text
def de_noise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text

# Normalize arabic
def normalize_arabic(text):
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    return(text)

# Construct alphabet dictionary
def construct_alphabet():
    with open(BASE_DIR + DATA_DIR + ALPHABET_FILE) as fh:
        rd, alphabet = csv.DictReader(fh, delimiter=','), list()
        for row in rd: alphabet.append(row)
        return alphabet