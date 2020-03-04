# Contributing to 3aransia

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