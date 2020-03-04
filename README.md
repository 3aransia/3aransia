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

### Transliterate cross languages and dialects to another, using the universal parameter
```python
MOROCCAN_ARABIC_SENTENCE = "ktb بلعربيا hnaya شحال ما بغيتي"

print(transliterate(MOROCCAN_ARABIC_SENTENCE, source='ar', target='ma', universal=True))
```

```
>>> ktb bl3rbya hnaya chhal ma bghyty
```

### Transliterate from all languages to all languages

```python
from aaransia import transliterate, SourceLanguageError

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
>>> ma ==> en
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl3rbya hnaya ch7al ma bghiti
>>> ma ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> ma
>>> ktb bl3rbya hnaya chhal ma bghyty
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> ar
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> en
>>> ktb bl'rbya hnaya chhal ma bghyty
>>> 
>>> كتب بلعربيا هنايا شحال ما بغيتي
>>> ar ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπρυτυ
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> en ==> ma
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> en ==> ar
>>> كتب بل'ربيا هنايا شهال ما بغيتي
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> en ==> en
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> 
>>> ktb bl'rbya hnaya chhal ma bghiti
>>> en ==> gr
>>> κτμπ μπλ'ρμπυα χναυα σχαλ μα μπριτι
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> ma
>>> ktb bl'ghbya hnaya chhhal ma bghiti
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> ar
>>> كتب بل'غبيا هنايا شههال ما بڭهيتي
>>> 
>>> κτμπ μπλ'ρμπυα χναυα σχχαλ μα μπγχιτι
>>> gr ==> en
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
