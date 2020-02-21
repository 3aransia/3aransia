"""This script make transliterations for the available languages"""

from aaransia.defaults import (
    ALPHABETS, ARABIAN_ALPHABET_CODE, SOURCE_LANGUAGE_EXCEPTION, DOUBLE_LETTERS
)
from aaransia.utils import construct_alphabet
from aaransia.exceptions import SourceLanguageException

# Load alphabet
alphabet = construct_alphabet()

# Return available alphabets code
def get_alphabets_codes():
    """Returns a list of alphabet codes"""
    return list(ALPHABETS)

# Return available alphabets
def get_alphabets():
    """Returns a dictionary of alphabets with keys as alphabet codes
    and values as plain alphabet names
    """
    return ALPHABETS

# Transliterate letter
def _transliterate_letter(letter, source, target):
    """Retuns the letter transliteration of the input letter accordingly
    to the source language and the target language

    Keyword arguments:
    letter -- the letter to transliterate
    source -- the source language from the available languages
    target -- the target language from the available languages
    """
    try:
        for _letter in alphabet:
            if _letter[ALPHABETS[source]] == letter:
                return _letter[ALPHABETS[target]]
        return None
    except IndexError:
        raise SourceLanguageException

# Transliterate word
def _transliterate_word(word, source, target):
    """Retuns the word transliteration of the input word accordingly
    to the source language and the target language

    Keyword arguments:
    word -- the word to transliterate
    source -- the source language from the available languages
    target -- the target language from the available languages
    """
    try:
        if word.isdigit():
            return word
        if source != ARABIAN_ALPHABET_CODE:
            word = word.lower()
        result, word_iterator = [], iter(range(len(word)))
        for i in word_iterator:
            if i < len(word) - 1:
                if word[i:i+2] in DOUBLE_LETTERS[source]:
                    result.append(_transliterate_letter(word[i:i+2], source, target))
                    next(word_iterator)
                elif word[i] == word[i+1] and source == ARABIAN_ALPHABET_CODE:
                    result.append(_transliterate_letter(word[i], source, target))
                    next(word_iterator)
                else:
                    result.append(_transliterate_letter(word[i], source, target))
            else:
                result.append(_transliterate_letter(word[i], source, target))
        return u''.join(result).replace(u'\u200e', '')
    except TypeError:
        raise SourceLanguageException

# Transliteration
def transliterate(text, source, target):
    """Retuns the text transliteration of the input text accordingly
    to the source language and the target language

    Keyword arguments:
    text -- the text to transliterate
    source -- the source language from the available languages
    target -- the target language from the available languages
    """
    try:
        return ' '.join(list(map(lambda w: _transliterate_word(w, source, target),
                                 text.split())))
    except (TypeError, SourceLanguageException):
        raise SourceLanguageException(f'{SOURCE_LANGUAGE_EXCEPTION}: {source}')
