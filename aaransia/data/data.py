"""This script is for managing the 3aransia's data"""

import csv
from pprint import PrettyPrinter

import pandas as pd

csv_file = pd.read_csv('alphabet.csv')

csv_file.to_csv('alphabet.csv', index=False)


def construct_alphabet():
    """Returns the constructed alphabet from the csv file in data
    """
    with open('alphabet.csv', 'r') as file_handler:
        dict_reader, alphabet = csv.DictReader(file_handler, delimiter=','), list()
        for row in dict_reader:
            alphabet.append(row)
    with open('../alphabet.py', 'w') as file_handler:
        file_handler.write(f'''
"""Script containing the alphabet """

from collections import OrderedDict

ALPHABET = {alphabet}
        
''')

construct_alphabet()
