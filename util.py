from pprint import PrettyPrinter

from aaransia.utils import * 
from aaransia.transliteration import * 
from aaransia.exceptions import * 

pp = PrettyPrinter(indent = 4)

pp.pprint(get_alphabets_codes())

pp.pprint(get_alphabets())

pp.pprint(construct_alphabet())

s_ar = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate(s_ar, source_language='ar', target_language='ma'))

s_ma = "ktb bl3rbya hnaya ch7al ma bghiti"
s_ar = "كتب بلعربيا هنايا شحال ما بغيتي"
s_la = "ktb bl'rbya hnaya chhal ma bghiti"
s_ab = "ktb bl'rbya hnaya chḥal ma bghiti"
s_gr = "κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι"

strings = [s_ma, s_ar, s_la, s_ab, s_gr]

for s in strings:
    for source_language in get_alphabets_codes():
        for target_language in get_alphabets_codes():
            try:
                print(f'{s}\n{source_language} ==> {target_language}\n{transliterate(s, source_language, target_language)}\n')
            except SourceLanguageException as sle:
                print(sle)