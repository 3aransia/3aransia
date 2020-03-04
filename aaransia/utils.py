"""Script containing util functions for 3aransia"""

import re

def de_noise(text):
    """Returns a de-noised arabic text

    Keyword arguments:
    @text -- the text to de-noise
    """
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text

def normalize_arabic(text):
    """Returns a normalized arabic text

    Keyword arguments:
    @text -- the text to normalize
    """
    text = re.sub("[إأٱآا]", "ا", text)
    text = re.sub("ى", "ا", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    return text
