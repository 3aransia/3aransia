from aaransia.transliteration import *
from aaransia.utils import *
from aaransia.test import *

if __name__ == "__main__":
    choice = ''
    while choice != '0': 
        choice = input("Please choose tranliteration:\n1. Moroccan to Moroccan Arabic\n0. Quit\n")
        if choice == '1': print(_transliterate_moroccan_to_moroccan_arabic(input("Enter input to translate to Moroccan Arabic: \n")))
        elif choice == '0': print('Thank you for using 3aransia\n')
        else: print('Incorrect entry, please try again\n')
