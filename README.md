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
>>> ['ma', 'ar', 'la', 'ab', 'gr']
```

### Get all alphabets

```python
from aaransia import get_alphabets

print(get_alphabets())
```

```
>>> {   
>>>     'ab': 'Abjadi Alphabet',
>>>     'ar': 'Arabian Alphabet',
>>>     'gr': 'Greek Alphabet',
>>>     'la': 'Latin Alphabet',
>>>     'ma': 'Moroccan Alphabet'
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

### Transliterate from all languages to all languages

```python
from aaransia import transliterate, SourceLanguageError

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
```

```
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> ma
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> ar
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> la
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> ab
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti Source language doesn't match the input text: ar
>>> ktb bl3rbya hnaya ch7al ma bghiti Source language doesn't match the input text: la
>>> ktb bl3rbya hnaya ch7al ma bghiti Source language doesn't match the input text: ab
>>> ktb bl3rbya hnaya ch7al ma bghiti Source language doesn't match the input text: gr
>>> كتب بلعربيا هنايا شحال ما بغيتي Source language doesn't match the input text: ma
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> ma
>>> ktb bl3rbya hnaya ch7al ma bghyty
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> ar
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> la
>>> ktb bl'rbya hnaya chhal ma bghyty
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> ab
>>> ktb bl'rbya hnaya chḥal ma bghyty
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπρυτυ
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي Source language doesn't match the input text: la
>>> كتب بلعربيا هنايا شحال ما بغيتي Source language doesn't match the input text: ab
>>> كتب بلعربيا هنايا شحال ما بغيتي Source language doesn't match the input text: gr
>>> ktb bl'rbya hnaya chhal ma bghiti Source language doesn't match the input text: ma
>>> ktb bl'rbya hnaya chhal ma bghiti Source language doesn't match the input text: ar
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> la ==> ma
>>> ktb bl3rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> la ==> ar
>>> كتب بلعربيا هنايا شهال ما بغيتي
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> la ==> la
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> la ==> ab
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> la ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> ab ==> ma
>>> ktb bl3rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> ab ==> ar
>>> كتب بلعربيا هنايا شهال ما بغيتي
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> ab ==> la
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> ab ==> ab
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> ab ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti Source language doesn't match the input text: gr
>>> ktb bl'rbya hnaya chḥal ma bghiti Source language doesn't match the input text: ma
>>> ktb bl'rbya hnaya chḥal ma bghiti Source language doesn't match the input text: ar
>>> ktb bl'rbya hnaya chḥal ma bghiti Source language doesn't match the input text: la
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> ab ==> ma
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> 
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> ab ==> ar
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> 
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> ab ==> la
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> ab ==> ab
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chḥal ma bghiti
>>> ab ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> ktb bl'rbya hnaya chḥal ma bghiti Source language doesn't match the input text: gr
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι Source language doesn't match the input text: ma
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι Source language doesn't match the input text: ar
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι Source language doesn't match the input text: la
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι Source language doesn't match the input text: ab
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> ma
>>> ktb bl3ghbya hnaya chhhal ma bghiti
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> ar
>>> كتب بلعغبيا هنايا شههال ما بڭهيتي
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> la
>>> ktb bl'ghbya hnaya chhhal ma bghiti
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> ab
>>> ktb bl'ghbya hnaya chhhal ma bghiti
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
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
4. Test the whole alphabet in [test.py](aaransia/test.py)
5. Make a pull request

## Other related projects

- [3aransia.api](https://3aransia.github.io/3aransia.api) The api of 3aransia
- [3aransia.web](http://3aransia.com) The web application of 3aransia
