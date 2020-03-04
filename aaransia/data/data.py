"""Script for managing the data"""

import pandas as pd

csv_file = pd.read_csv('alphabet.csv')

print(list(csv_file.columns))