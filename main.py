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

MOROCCAN_SENTENCE = "ktb bl3rbya hnaya ch7al ma bghiti"
ARABIC_SENTENCE = "كتب بلعربيا هنايا شحال ما بغيتي"
LATIN_SENTENCE = "ktb bl'rbya hnaya chhal ma bghiti"
ABJADI_SENTENCE = "ktb bl'rbya hnaya chḥal ma bghiti"
GREEK_SENTENCE = "κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι"

SENTENCES = [MOROCCAN_SENTENCE, ARABIC_SENTENCE, LATIN_SENTENCE, ABJADI_SENTENCE, GREEK_SENTENCE]

for sentence in SENTENCES:
    for source_language in get_alphabets_codes():
        try:
            for target_language in get_alphabets_codes():
                print(f'{sentence}\n'
                      f'{source_language} ==> {target_language}\n'
                      f'{transliterate(sentence, source_language, target_language)}\n')
        except SourceLanguageError as sle:
            print(sentence, sle)

MOROCCAN_SPECIAL_SENTENCE = "ktb bl3rbya, hnaya ch7al ma bghiti !&"

print(transliterate(MOROCCAN_SPECIAL_SENTENCE, source='ma', target='la'))