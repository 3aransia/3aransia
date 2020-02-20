from aaransia.utils import * 
from aaransia.transliteration import * 
from aaransia.exceptions import * 

print(get_alphabets_codes())

s_ma = "ktb bl3rbya hnaya ch7al ma bghiti"
s_ar = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate_moroccan(s_ma))
print(transliterate_moroccan_arabic(s_ar))

s_ar = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate(s_ar, 'ar', 'ma'))

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
                continue