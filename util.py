from aaransia.utils import * 
from aaransia.transliteration import * 

construct_moroccan_to_moroccan_arabic_alphabet()
construct_moroccan_arabic_to_moroccan_alphabet()
construct_moroccan_to_latin_alphabet()
construct_moroccan_arabic_to_latin_alphabet()

s_1 = "ktb bl3rbya hnaya"
s_2 = "كتب بلعربيا هنايا"

print(transliterate_moroccan(s_1))
print(transliterate_moroccan_arabic(s_2))
print(transliterate_moroccan_to_latin(s_1))
print(transliterate_moroccan_arabic_to_latin(s_2))