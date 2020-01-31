from _3aransia.translator import *
from _3aransia.test import *

# Function to translate Moroccan input to Arabic
def translate_input(s):
    print(' '.join([word['arabian_word'] for word in moroccan_to_arabic(s)]))

translate_input(input('Enter input to translate: '))