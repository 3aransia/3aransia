"""This script is for demonstration purposes"""

from pprint import PrettyPrinter

from aaransia.utils import construct_alphabet
from aaransia.transliteration import get_alphabets, get_alphabets_codes, transliterate
from aaransia.exceptions import SourceLanguageError

PRETTY_PRINTER = PrettyPrinter(indent=1)

PRETTY_PRINTER.pprint(get_alphabets_codes())

PRETTY_PRINTER.pprint(get_alphabets())

PRETTY_PRINTER.pprint(construct_alphabet())

ARABIC_SENTENCE = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate(ARABIC_SENTENCE, source='ar', target='ma'))

MOROCCAN_ARABIC_SENTENCE = "ktb بلعربيا hnaya شحال ما بغيتي"

print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma', universal=True))

MOROCCAN_SENTENCE = "ktb bl3rbya hnaya ch7al ma bghiti"
ARABIC_SENTENCE = "كتب بلعربيا هنايا شحال ما بغيتي"
ENGLISH_SENTENCE = "ktb bl'rbya hnaya chhal ma bghiti"
GREEK_SENTENCE = "κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι"

SENTENCES = [MOROCCAN_SENTENCE, ARABIC_SENTENCE, ENGLISH_SENTENCE, GREEK_SENTENCE]

ALPHABETS = get_alphabets_codes()

for i in range(len(SENTENCES)):
    try:
        for target_language in ALPHABETS:
            print(f'{SENTENCES[i]}\n'
                  f'{ALPHABETS[i]} ==> {target_language}\n'
                  f'{transliterate(SENTENCES[i], ALPHABETS[i], target_language)}\n')
    except SourceLanguageError as sle:
        print(SENTENCES[i], sle)
