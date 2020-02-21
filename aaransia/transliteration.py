"""This script make transliterations for the available languages"""

import unidecode

from aaransia.defaults import (
    ALPHABET, ALPHABETS, MOROCCAN_ALPHABET, ARABIAN_ALPHABET, DOUBLE_MOROCCAN_LETTERS,
    MOROCCAN_ALPHABET_CODE, ARABIAN_ALPHABET_CODE, SOURCE_LANGUAGE_EXCEPTION
)

from aaransia.exceptions import SourceLanguageException

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

# Transliteration of a Moroccan letter to an Arabian letter
def ma_to_ar_letter(letter, position, word):
    """Retuns the letter transliteration in arabic of the input moroccan letter
    accordingly to its position and the word it is inside

    Keyword arguments:
    letter -- the letter to transliterate
    position -- the position of the letter in the word
    word -- the word the letter is in
    """
    try:
        if ((letter in 'o' and len(word) > 1) or letter in ('a', 'i', 'e')) and position == 0:
            return 'ا'
        if (letter in ('o', 'e')) and position > 0:
            return ''
        for _letter in ALPHABET:
            if _letter[MOROCCAN_ALPHABET] == letter:
                return _letter[ARABIAN_ALPHABET]
        return None
    except IndexError:
        raise SourceLanguageException

# Transliterate letter
def _transliterate_letter(letter, source_language, target_language):
    """Retuns the letter transliteration of the input letter accordingly
    to the source language and the target language

    Keyword arguments:
    letter -- the letter to transliterate
    source_language -- the source language from the available languages
    target_language -- the target language from the available languages
    """
    try:
        for _letter in ALPHABET:
            if _letter[ALPHABETS[source_language]] == letter:
                return _letter[ALPHABETS[target_language]]
        return None
    except IndexError:
        raise SourceLanguageException

# Transliterate moroccan word to moroccan arabic word
def ma_to_ar_word(word):
    """Retuns the word transliteration in arabic of the input moroccan word

    Keyword arguments:
    word -- the word to transliterate
    """
    if word.isdigit():
        return word
    arabian_word, word = [], unidecode.unidecode(word.lower())
    word_iterator = iter(range(len(word)))
    for i in word_iterator:
        if i < len(word) - 1:
            if word[i:i+2] in DOUBLE_MOROCCAN_LETTERS:
                arabian_word.append(ma_to_ar_letter(word[i:i+2], i, word))
                next(word_iterator)
            elif word[i] == word[i+1]:
                arabian_word.append(ma_to_ar_letter(word[i], i, word))
                next(word_iterator)
            else:
                arabian_word.append(ma_to_ar_letter(word[i], i, word))
        else:
            arabian_word.append(ma_to_ar_letter(word[i], i, word))
    return u''.join(arabian_word).replace(u'\u200e', '')

# Transliteration of Moroccan to Moroccan Arabic
def _transliterate_moroccan_to_moroccan_arabic(text):
    """Retuns the moroccan to moroccan arabic transliteration of a text

    Keyword arguments:
    text -- moroccan text entry
    """
    try:
        ar_transliteration = list()
        for word in text.split():
            ar_transliteration.append(ma_to_ar_word(word))
        ar_transliteration = u' '.join(ar_transliteration)
        return ar_transliteration
    except IndexError:
        raise SourceLanguageException

# Transliteration
def transliterate(text, source_language, target_language):
    """Retuns the text transliteration of the input text accordingly
    to the source language and the target language

    Keyword arguments:
    text -- the text to transliterate
    source_language -- the source language from the available languages
    target_language -- the target language from the available languages
    """
    try:
        if source_language == MOROCCAN_ALPHABET_CODE and target_language == ARABIAN_ALPHABET_CODE:
            return _transliterate_moroccan_to_moroccan_arabic(text)
        return ''.join(list(map(lambda l: _transliterate_letter(l, source_language,
                                                                target_language),
                                text)))
    except (TypeError, SourceLanguageException):
        raise SourceLanguageException(f'{SOURCE_LANGUAGE_EXCEPTION}: {source_language}')
