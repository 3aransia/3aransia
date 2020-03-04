"""This script make transliterations for the available languages"""

import unicodedata

from aaransia.exceptions import SourceLanguageError
from aaransia.utils import de_noise, normalize_arabic
from aaransia.defaults import (
    ALPHABETS, ARABIC_ALPHABET_CODE, SOURCE_LANGUAGE_EXCEPTION_MESSAGE, DOUBLE_LETTERS,
    ALPHABET, MOROCCAN_ALPHABET_CODE, SPECIAL_CHARACTERS, ALPHABET_CODE_LIST
)

def get_alphabets_codes():
    """Returns a list of alphabet codes"""
    return ALPHABET_CODE_LIST

def get_alphabets():
    """Returns a dictionary of alphabets with keys as alphabet codes
    and values as plain alphabet names
    """
    return ALPHABETS

def _get_letter(letter, source, target, universal):
    """Retuns the letter transliteration of the input letter accordingly
    to the source language and the target language

    Keyword arguments:
    @letter -- the letter to transliterate
    @source -- the source language from the available languages
    @target -- the target language from the available languages
    """
    letter = de_noise(normalize_arabic(unicodedata.normalize('NFD', letter)[0]))
    if letter in SPECIAL_CHARACTERS:
        return letter
    for _letter in ALPHABET:
        if _letter[ALPHABETS[source]] == letter:
            return _letter[ALPHABETS[target]]
    if not universal:
        return None
    else:
        return letter


def _transliterate_letter(letter, source, target, position, word, universal):
    """Retuns the letter transliteration of the input letter accordingly
    to the source and the target language, the position of the letter
    and the word it is inside

    Keyword arguments:
    @letter -- the letter to transliterate
    @source -- the source language from the available languages
    @target -- the target language from the available languages
    @position -- the position of the letter
    @word -- the word from where the transliteration is make
    """
    if source == MOROCCAN_ALPHABET_CODE and target == ARABIC_ALPHABET_CODE and position == 0:
        if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')):
            return 'ا'
        return _get_letter(letter, MOROCCAN_ALPHABET_CODE, ARABIC_ALPHABET_CODE, universal)
    return _get_letter(letter, source, target, universal)

def _transliterate_word(word, source, target, universal):
    """Retuns the word transliteration of the input word accordingly
    to the source language and the target language

    Keyword arguments:
    @word -- the word to transliterate
    @source -- the source language from the available languages
    @target -- the target language from the available languages
    """
    if word.isdigit():
        return word
    if source != ARABIC_ALPHABET_CODE:
        word = word.lower()
    result, word_iterator = [], iter(range(len(word)))
    for i in word_iterator:
        if i < len(word) - 1:
            if word[i:i+2] in DOUBLE_LETTERS[source]:
                result.append(_transliterate_letter(word[i:i+2], source, target, i, word, universal))
                next(word_iterator)
            elif word[i] == word[i+1] and target == ARABIC_ALPHABET_CODE:
                result.append(_transliterate_letter(word[i], source, target, i, word, universal))
                next(word_iterator)
            else:
                result.append(_transliterate_letter(word[i], source, target, i, word, universal))
        else:
            result.append(_transliterate_letter(word[i], source, target, i, word, universal))
    return u''.join(result).replace(u'\u200e', '')

def transliterate(text, source, target, universal=False):
    """Retuns the text transliteration of the input text accordingly
    to the source language and the target language

    Keyword arguments:
    @text -- the text to transliterate
    @source -- the source language from the available languages
    @target -- the target language from the available languages
    """
    try:
        return ' '.join(list(map(lambda word: _transliterate_word(word, source, target, universal),
                                 text.split())))
    except Exception:
        raise SourceLanguageError(f'{SOURCE_LANGUAGE_EXCEPTION_MESSAGE}: {source}')