from aaransia.transliterator import *
from aaransia.utils import *
from aaransia.analyzer import *
from aaransia.test import *

# Function to transliterate Moroccan input to Moroccan Arabic
def transliterate_moroccan(s):
    print(moroccan_to_arabic(s))

# Function to translate Moroccan Arabic input to Moroccan
def transliterate_moroccan_arabic(s):
    print(arabic_to_moroccan(s))

if __name__ == "__main__":
    text, results = str(input("Text: ")).split(), list()
    for word in text:
        for analysis in ai.analyse_arabic(word):
            if analysis and analysis not in results:
                results.append(analysis)
    if len(results) == 0:
        results = ai.information(text)
    print(results)
