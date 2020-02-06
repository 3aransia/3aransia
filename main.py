from _3aransia.transliterator import *
from _3aransia.test import *
from _3aransia.utils import *

# Function to translate Moroccan input to Arabic
def translate_input(s):
    print(' '.join([word['arabian_word'] for word in moroccan_to_arabic(s)]))

translate_input(input('Enter input to translate: '))