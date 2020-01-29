from _3aransia.translator import *

# Function to translate Moroccan input to Arabic
def translate_input(s):
    print(' '.join([word['arabian_word'] for word in moroccan_to_arabic(s)]))

# Function to run tests
# run_tests()

translate_input(input('Enter input to translate: '))