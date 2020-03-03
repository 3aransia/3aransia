"""Script containing util functions for 3aransia"""

import re
import csv

from aaransia.defaults import BASE_DIR, DATA_DIR, ALPHABET_FILE

# Remove noise from arabic text
def de_noise(text):
    """Returns a de-noised arabic text

    Keyword arguments:
    @text -- the text to de-noise
    """
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
    """Returns a normalized arabic text

    Keyword arguments:
    @text -- the text to normalize
    """
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ا", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    return text

# Construct alphabet dictionary
def construct_alphabet():
    """Returns the constructed alphabet from the csv file in data
    """
    with open(BASE_DIR + DATA_DIR + ALPHABET_FILE) as file_handler:
        dict_reader, alphabet = csv.DictReader(file_handler, delimiter=','), list()
        for row in dict_reader:
            alphabet.append(row)
        return alphabet
