#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import cmd

@cmd.add
def homograph(text):
    """Replace a character with a homoglyph

    Generates all permutations of a single replaced characer of `word`
    depending on the alphabet(s) selected.  

    Please note that in modern browsers Latin, Cyrillic or Greek characters
    cannot be mixed with each other or punycode is shown.

    There is more information in the Google Chrome IDN policy:
    https://www.chromium.org/developers/design-documents/idn-in-google-chrome

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()
    homoglyphs = {
            'alnum': { '0': 'o', '1': ['i', 'l'], '5': 's', 'i': ['1', 'l'], 'l': ['1', 'i'], 'o': '0', 's': '5' },
            'armenian': { '1': u'Լ', 'l': u'Լ' },
            'cyrillic': { 'a': u'а', 'c': u'с', 'e': u'е', 'o': u'о', 'p': u'р', 'x': u'х', 'y': u'у' },
            'greek': { '0': u'Ο', '1': u'Ι', 'c': u'ϲ', 'i': u'Ι', 'l': u'Ι', 'o': u'ο', 'p': u'ρ', 'u': u'υ', 'v': u'ν' }
            }

    # TODO Include all permutations (multiple replacements)
    for i in range(0, len(text)):
        for name,glyphs in homoglyphs.iteritems():
            if text[i] not in glyphs:
                continue
            for glyph in glyphs[text[i]]:
                # DEBUG print("Name: {}, Glyph '{}' -> '{}'".format(name, text[i], glyph.encode('utf-8')))
                result.add(text[:i] + glyph + text[i+1:])
    return result

@cmd.add
def hyphenation(text):
    """Inserted hyphen

    Generate all permutations of a inserted hyphen in `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()

    for i in range(1, len(text)):
        result.add(text[:i] + '-' + text[i:])

    return result

@cmd.add
def vowelswap(text):
    """Swap a vowel

    Generate all permutations of a swapped vowel in `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()
    vowels = 'aeiou'
    for i in range(0, len(text)):
        for vowel in vowels:
            if text[i] not in vowels:
                continue
            result.add(text[:i] + vowel + text[i+1:])
    return result
