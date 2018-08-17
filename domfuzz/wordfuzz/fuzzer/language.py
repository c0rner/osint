#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import cmd

@cmd.add
def homograph(text, script=['latin']):
    """Replace a character with a homoglyph

    Generates all permutations of a single replaced characer of `word`
    depending on the alphabet(s) selected.  

    Please note that in modern browsers two different scripts cannot be
    mixed or punycode is shown. (ie. Latin + Armenian produces puny code)

    There is more information in the Google Chrome IDN policy:
    https://www.chromium.org/developers/design-documents/idn-in-google-chrome

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()
    homoglyphs = {
            'alnum': {
                '0': 'o',
                '1': ['i', 'l'],
                '5': 's',
                'i': ['1', 'l'],
                'l': ['1', 'i'],
                'o': '0',
                's': '5'
                },
            'armenian': {
                '1': u'\u053c', # 'Լ'
                'l': u'\u053c', # 'Լ'
                't': u'\u0567'  # 'է'
                },
            'cyrillic': {
                'a': u'\u0430', # 'а'
                'e': u'\u0435', # 'е'
                'o': u'\u043e', # 'о'
                'p': u'\u0440', # 'р'
                'c': u'\u0441', # 'с'
                'y': u'\u0443', # 'у'
                'x': u'\u0445', # 'х'
                's': u'\u0455', # 'ѕ'
                'i': u'\u0456', # 'і'
                'j': u'\u0458'  # 'ј'
                },
            'greek': {
                'i': [u'\u03af', u'\u03b9'], # 'ί', 'ι'
                'l': u'\u03b9', # 'ι'
                'v': u'\u03bd', # 'ν'
                'o': u'\u03bf', # 'ο'
                'u': u'\u03c5', # 'υ'
                'q': u'\u03e5', # 'ϥ'
                'c': u'\u03f2', # 'ϲ'
                'j': u'\u03f3'  # 'ϳ'
                },
            'latin': {
                u'\u00e4': [u'\u00e2', u'\u00e3', u'\u0101', u'\u0103'], # 'ä', 'â', 'ã', 'ā', 'ă'
                u'\u00e5': [u'\u00e0', u'\u00e1', u'\u0103'], # 'å', 'à', 'á'
                u'\u00f6': [u'\u00f0', u'\u00f4', u'\u00f5', u'\u014d', u'\u014f', u'\u0151'], # 'ö', 'ð', 'ô', 'õ', 'ō', 'ŏ', 'ő'
                'i': [u'\u00ec', u'\u00ed', u'\u00ee', u'\u00ef', u'\u0129'], # 'ì', 'í', 'î', 'ï', 'ĩ'
                'a': u'\u0105', # 'ą'
                'c': [u'\u0109', u'\u010b'], # 'ĉ' 'ċ'
                'd': [u'\u010f',  u'\u0111'], # 'ď', 'đ'
                'e': [u'\u0117', u'\u0119'], # 'ė', 'ę'
                'g': [u'\u011d', u'\u0121', u'\u0123'], # 'ĝ', 'ġ', 'ģ'
                'j': [u'\u0135', u'\u013c'], # 'ĵ', 'ļ'
                'k': [u'\u0137'], # 'ķ'
                'l': [u'\u0137'], # 'ķ'
                'l': [u'\u013a', u'\u013c', u'\u013e', u'\u0142'], # 'ĺ', 'ļ', 'ľ', 'ł'
                'n': u'\u0146', # 'ņ'
                'r': [u'\u0155', u'\u0157'], # 'ŕ', 'ŗ'
                's': [u'\u015d', u'\u015f'], # 'ŝ', 'ş'
                't': [u'\u0163', u'\u0165', u'\u0167'], # 'ţ', 'ť', 'ŧ'
                'z': [u'\u017a', u'\u017c', u'\u017e']  # 'ź', 'ż', 'ž'
                }
            }

    # TODO Include all permutations (multiple replacements)
    # TODO Support double homoglyphs (example \u0133 'ĳ' or \u014b 'ŋ')
    # TODO Support combinations (example hi -> 'ŀi')
    for i in range(0, len(text)):
        for name in script:
            if text[i] not in homoglyphs[name]:
                continue
            for glyph in homoglyphs[name][text[i]]:
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
