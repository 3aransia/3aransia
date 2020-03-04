# 3aransia

Transliteration of languages and dialects

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Contribution

For contribution you can refer to [CONTRIBUTING.md](CONTRIBUTING.md)

## Features

- Fast and reliable - it uses default variables to access data
- Bulk transliteration
- API available
- Multilanguage transliteration available
- 70 languages and dialects supportted

## Languages and dialects supported

```
1. Afrikaans	    2. Algerian	        3. Arabic	
4. Azerbaijani	    5. Bosnian	        6. Catalan	
7. Corsican	    8. Czech	        9. Welsh	
10. Danish	    11. German	        12. Greek	
13. English	    14. Esperanto       15. Spanish	
16. Estonian	    17. Basque	        18. Persian	
19. Finnish	    20. French	        21. Frisian	
22. Irish	    23. Gaelic	        24. Galician	
25. Hausa	    26. Croatian	27. Creole	
28. Hungarian	    29. Hawaiian	30. Indonesian	
31. Igbo	    32. Icelandic	33. Italian	
34. Kinyarwanda	    35. Kurdish	        36. Latin	
37. Libyan	    38. Lithuanian	39. Luxembourgish	
40. Latvian	    41. Moroccan	42. Malagasy	
43. Maori	    44. Malay	        45. Maltese	
46. Dutch	    47. Norwegian	48. Polish	
49. Portuguese	    50. Romanian	51. Samoan	
52. Shona	    53. Slovak	        54. Slovenian	
55. Somali	    56. Albanian	57. Sesotho	
58. Sundanese	    59. Swedish	        60. Swahili	
61. Filipino	    62. Tunisian	63. Turkish	
64. Turkmen	    65. Urdu	        66. Uzbek	
67. Vietnamese	    68. Xhosa	        69. Yoruba	
70. Zulu
```
  
## Installation

```pip install aaransia```

## Usage

### Get all alphabets codes

```python
from aaransia import get_alphabets_codes

print(len(get_alphabets_codes()))
print(get_alphabets_codes())
```

```
>>> 70
>>> ['ar', 'af', 'sq', 'al', 'az', 'eu', 'bo', 'ca', 'co', 'hr', 'cs', 'da',
 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fs', 'gl', 'de', 'ht', 'ha', 'hw',
 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ki', 'ku', 'la', 'lv', 'li', 'lt', 'lu',
 'ma', 'mg', 'ms', 'mt', 'mo', 'no', 'pl', 'pt', 'ro', 'sa', 'gc', 'el',
 'ss', 'sh', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tn', 'tr', 'tu',
 'uz', 'vi', 'cy', 'xh', 'yo', 'zu', 'fa', 'ur']
```

### Get all alphabets

```python
from aaransia import get_alphabets

print(get_alphabets())
```

```
>>> {
>>>     'af': 'Afrikaans Alphabet',
>>>     'al': 'Algerian Alphabet',
>>>     'ar': 'Arabic Alphabet',
>>>     'az': 'Azerbaijani Alphabet',
>>>     'bo': 'Bosnian Alphabet',
>>>     'ca': 'Catalan Alphabet',
>>>     'co': 'Corsican Alphabet',
>>>     'cs': 'Czech Alphabet',
>>>     'cy': 'Welsh Alphabet',
>>>     'da': 'Danish Alphabet',
>>>     'de': 'German Alphabet',
>>>     'el': 'Greek Alphabet',
>>>     'en': 'English Alphabet',
>>>     'eo': 'Esperanto Alphabet',
>>>     'es': 'Spanish Alphabet',
>>>     'et': 'Estonian Alphabet',
>>>     'eu': 'Basque Alphabet',
>>>     'fa': 'Persian Alphabet',
>>>     'fi': 'Finnish Alphabet',
>>>     'fr': 'French Alphabet',
>>>     'fs': 'Frisian Alphabet',
>>>     'ga': 'Irish Alphabet',
>>>     'gc': 'Gaelic Alphabet',
>>>     'gl': 'Galician Alphabet',
>>>     'ha': 'Hausa Alphabet',
>>>     'hr': 'Croatian Alphabet',
>>>     'ht': 'Creole Alphabet',
>>>     'hu': 'Hungarian Alphabet',
>>>     'hw': 'Hawaiian Alphabet',
>>>     'id': 'Indonesian Alphabet',
>>>     'ig': 'Igbo Alphabet',
>>>     'is': 'Icelandic Alphabet',
>>>     'it': 'Italian Alphabet',
>>>     'ki': 'Kinyarwanda Alphabet',
>>>     'ku': 'Kurdish Alphabet',
>>>     'la': 'Latin Alphabet',
>>>     'li': 'Libyan Alphabet',
>>>     'lt': 'Lithuanian Alphabet',
>>>     'lu': 'Luxembourgish Alphabet',
>>>     'lv': 'Latvian Alphabet',
>>>     'ma': 'Moroccan Alphabet',
>>>     'mg': 'Malagasy Alphabet',
>>>     'mo': 'Maori Alphabet',
>>>     'ms': 'Malay Alphabet',
>>>     'mt': 'Maltese Alphabet',
>>>     'nl': 'Dutch Alphabet',
>>>     'no': 'Norwegian Alphabet',
>>>     'pl': 'Polish Alphabet',
>>>     'pt': 'Portuguese Alphabet',
>>>     'ro': 'Romanian Alphabet',
>>>     'sa': 'Samoan Alphabet',
>>>     'sh': 'Shona Alphabet',
>>>     'sk': 'Slovak Alphabet',
>>>     'sl': 'Slovenian Alphabet',
>>>     'so': 'Somali Alphabet',
>>>     'sq': 'Albanian Alphabet',
>>>     'ss': 'Sesotho Alphabet',
>>>     'su': 'Sundanese Alphabet',
>>>     'sv': 'Swedish Alphabet',
>>>     'sw': 'Swahili Alphabet',
>>>     'tl': 'Filipino Alphabet',
>>>     'tn': 'Tunisian Alphabet',
>>>     'tr': 'Turkish Alphabet',
>>>     'tu': 'Turkmen Alphabet',
>>>     'ur': 'Urdu Alphabet',
>>>     'uz': 'Uzbek Alphabet',
>>>     'vi': 'Vietnamese Alphabet',
>>>     'xh': 'Xhosa Alphabet',
>>>     'yo': 'Yoruba Alphabet',
>>>     'zu': 'Zulu Alphabet'
>>> }
```

### Transliterate from a language or dialect to another

```python
ARABIC_SENTENCE = "كتب بلعربيا هنايا شحال ما بغيتي"

print(transliterate(ARABIC_SENTENCE, source='ar', target='ma'))
```

```
>>> ktb bl3rbya hnaya ch7al ma bghiti
```

### Transliterate cross languages and dialects to another, using the universal parameter
```python
from aaransia import SourceLanguageError

MOROCCAN_ARABIC_SENTENCE = "ktb بلعربيا hnaya شحال ما بغيتي"

try:
    print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma'))
except SourceLanguageError as source_language_error:
    print(source_language_error)

print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma', universal=True))
print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ma', target='ar', universal=True))
```

```
>>> Source alphabet language doesn't match the input text: ar
>>> ktb bl3rbya hnaya chhal ma bghyty
>>> كتب بلعربيا هنايا شحال ما بغيتي
```

## Adding a language or a dialect

1. Add it to the [alphabet](aaransia/data/alphabet.csv) CSV file
2. Generate the whole alphabet with the ```construct_alphabet``` function from [data.py](aaransia/data/data.py)
3. Update the [defaults.py](aaransia/defaults.py) (the order the to be respected)
   1. Add the alphabet code
   2. Add the alphabet name
   3. Add both of them to the alphabet dictionary
   4. Add the double letters if there are any
4. Test a text with the language just added against all other languages in [test.py](aaransia/test.py)
   1. Add a language text to test in [text_samples](aaransia/text_samples.py) (the order is to be respected)
   2. Add test handling for the new language
   3. Test it by using the command ```python -m unittest discover -s aaransia``` from the [3aransia](./) repository
   4. Fix the bugs
5. Validate it semantically and phonetically
6. Make a pull request
7. Wait for the PR confirmation and add your name to the collaborators

## Fixing bugs and adding features

- ```pylint``` code before doing a PR
- Contribution can also be made through adding issues

## Other related projects

- [3aransia.api](https://3aransia.github.io/3aransia.api) The api of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
