from aaransia.transliterator import *
from aaransia.utils import *
from aaransia.test import *

# Function to transliterate Moroccan input to Moroccan Arabic
def transliterate_moroccan(s):
    print(moroccan_to_arabic(s))

# Function to translate Moroccan Arabic input to Moroccan
def transliterate_moroccan_arabic(s):
    print(moroccan_arabic_to_moroccan(s))

if __name__ == "__main__":
    choice = ''
    while choice != '0': 
        choice = input("Please choose tranliteration:\n1. Moroccan to Moroccan Arabic\n2. Moroccan Arabic to Moroccan\n0. Quit\n")
        if choice == '1': transliterate_moroccan(input("Enter input to translate to Moroccan Arabic: "))
        elif choice == '2': transliterate_moroccan_arabic(input("Enter input to translate to Moroccan: "))
        elif choice == '0': print('Thank you for using 3aransia')
        else: 
            print('Incorrect entry, please try again')
