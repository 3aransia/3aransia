# Contributing to 3aransia

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

## Fixing bugs and adding features

- ```pylint``` code before doing a PR
- Contribution can also be made through adding issues