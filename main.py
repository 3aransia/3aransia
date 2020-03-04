"""This script is for demonstration purposes"""

from pprint import PrettyPrinter

from aaransia.transliteration import get_alphabets, get_alphabets_codes, transliterate
from aaransia.exceptions import SourceLanguageError

PRETTY_PRINTER = PrettyPrinter(indent=1)

print(get_alphabets_codes())

print(len(get_alphabets_codes()))

PRETTY_PRINTER.pprint(get_alphabets())

ARABIC_SENTENCE = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate(ARABIC_SENTENCE, source='ar', target='ma'))

MOROCCAN_ARABIC_SENTENCE = "ktb بلعربيا hnaya شحال ما بغيتي"

try:
    print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma'))
except SourceLanguageError as source_language_error:
    print(source_language_error)

print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma', universal=True))
print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ma', target='ar', universal=True))
