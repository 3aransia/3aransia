# 3aransia

Transliteration of languages and dialects

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg)

## Contribution

For contribution you can refer to [CONTRIBUTING.md](CONTRIBUTING.md)

## Prerequisites

- [`Python 3`](https://www.python.org/downloads/)
  
## Installation

```pip install aaransia```

## Usage

### Get all alphabets codes

```python
from aaransia import get_alphabets_codes

print(get_alphabets_codes())
```

```
>>> ['ar', 'af', 'al', 'az', 'ba', 'bo', 'ca', 'co', 'cr', 'cz', 'da', 'du', 'en', 'ep', 'et', 'fp', 'fi', 'fr', 'fs', 'ga', 'ge', 'ha', 'hw', 'hu', 'ic', 'ig', 'in', 'ir', 'it', 'ki', 'ku', 'la', 'lt', 'li', 'lu', 'ma', 'mg', 'ml', 'mt', 'mo', 'no', 'po', 'pr', 'ro', 'sa', 'gr', 'se', 'sh', 'sv', 'sl', 'so', 'es', 'su', 'sw', 'tk', 'tu', 'uz', 'vi', 'we', 'xh', 'yo', 'zu', 'pa', 'pe', 'si', 'ur', 'uy']
```

### Get all alphabets

```python
from aaransia import get_alphabets

print(get_alphabets())
```

```
{
>>>    'af': 'Afrikaans Alphabet',
>>>    'al': 'Albanian Alphabet',
>>>    'ar': 'Arabic Alphabet',
>>>    'az': 'Azerbaijani Alphabet',
>>>    'ba': 'Basque Alphabet',
>>>    'bo': 'Bosnian Alphabet',
>>>    'ca': 'Catalan Alphabet',
>>>    'co': 'Corsican Alphabet',
>>>    'cr': 'Creole Alphabet',
>>>    'cz': 'Czech Alphabet',
>>>    'da': 'Danish Alphabet',
>>>    'du': 'Dutch Alphabet',
>>>    'en': 'English Alphabet',
>>>    'ep': 'Esperanto Alphabet',
>>>    'es': 'Spanish Alphabet',
>>>    'et': 'Estonian Alphabet',
>>>    'fi': 'Finnish Alphabet',
>>>    'fp': 'Filipino Alphabet',
>>>    'fr': 'French Alphabet',
>>>    'fs': 'Frisian Alphabet',
>>>    'ga': 'Gaelic Alphabet',
>>>    'ge': 'German Alphabet',
>>>    'gr': 'Greek Alphabet',
>>>    'ha': 'Hausa Alphabet',
>>>    'hu': 'Hungarian Alphabet',
>>>    'hw': 'Hawaiian Alphabet',
>>>    'ic': 'Icelandic Alphabet',
>>>    'ig': 'Igbo Alphabet',
>>>    'in': 'Indonesian Alphabet',
>>>    'ir': 'Irish Alphabet',
>>>    'it': 'Italian Alphabet',
>>>    'ki': 'Kinyarwanda Alphabet',
>>>    'ku': 'Kurdish Alphabet',
>>>    'la': 'Latin Alphabet',
>>>    'li': 'Lithuanian Alphabet',
>>>    'lt': 'Latvian Alphabet',
>>>    'lu': 'Luxembourgish Alphabet',
>>>    'ma': 'Moroccan Alphabet',
>>>    'mg': 'Malagasy Alphabet',
>>>    'ml': 'Malay Alphabet',
>>>    'mo': 'Maori Alphabet',
>>>    'mt': 'Maltese Alphabet',
>>>    'no': 'Norwegian Alphabet',
>>>    'pa': 'Pashto Alphabet',
>>>    'pe': 'Persian Alphabet',
>>>    'po': 'Polish Alphabet',
>>>    'pr': 'Portuguese Alphabet',
>>>    'ro': 'Romanian Alphabet',
>>>    'sa': 'Samoan Alphabet',
>>>    'se': 'Sesotho Alphabet',
>>>    'sh': 'Shona Alphabet',
>>>    'si': 'Sindhi Alphabet',
>>>    'sl': 'Slovenian Alphabet',
>>>    'so': 'Somali Alphabet',
>>>    'su': 'Sundanese Alphabet',
>>>    'sv': 'Slovak Alphabet',
>>>    'sw': 'Swedish Alphabet',
>>>    'tk': 'Turkish Alphabet',
>>>    'tu': 'Turkmen Alphabet',
>>>    'ur': 'Urdu Alphabet',
>>>    'uy': 'Uyghur Alphabet',
>>>    'uz': 'Uzbek Alphabet',
>>>    'vi': 'Vietnamese Alphabet',
>>>    'we': 'Welsh Alphabet',
>>>    'xh': 'Xhosa Alphabet',
>>>    'yo': 'Yoruba Alphabet',
>>>    'zu': 'Zulu Alphabet'
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
2. Generate the whole alphabet with the ```construct_alphabet``` function from [utils.py](aaransia/utils.py)
3. Update the [defaults.py](aaransia/defaults.py)
   1. Add the alphabet code
   2. Add the alphabet name
   3. Add both of them to the alphabet dictionary
   4. Add the double letters if they are
   5. Add the updated alphabet got from ```construct_alphabet``` earlier (use ```PrettyPrinter``` and ```pylint``` to format it, you can refer to main.py line 15)
4. Test a text with the language just added against all other languages in [test.py](aaransia/test.py)
   1. Add a language text to test in [text_samples](aaransia/text_samples.py)
   2. Add test handling for the new language
   3. Test it by using the command ```python -m unittest discover -s aaransia```
   4. Fix the bugs
5. Validate it semantically and phonetically
6. Make a pull request

## Other related projects

- [3aransia.api](https://3aransia.github.io/3aransia.api) The api of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
