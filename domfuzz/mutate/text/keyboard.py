#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO Should spacebar be included?
keyboard = {
    'qwerty': {
        '1': '2q',   '2': '3wq1',   '3': '4ew2',   '4': '5re3',   '5': '6tr4',   '6': '7yt5',   '7': '8uy6',   '8': '9iu7',   '9': '0oi8',   '0': 'po9',
        'q': '12wa', 'w': '23esaq', 'e': '34rdsw', 'r': '45tfde', 't': '56ygfr', 'y': '67uhgt', 'u': '78ijhy', 'i': '89okju', 'o': '90plki', 'p': '0lo',
        'a': 'qwsz', 's': 'wedxza', 'd': 'erfcxs', 'f': 'rtgvcd', 'g': 'tyhbvf', 'h': 'yujnbg', 'j': 'uikmnh', 'k': 'iol,mj',  'l': 'op.,k',
        'z': 'asx',  'x': 'sdcz',   'c': 'dfvx',   'v': 'fgbc',   'b': 'ghnv',   'n': 'hjmn',   'm': 'jk,n'
        },
    'qwertz': {
        '1': '2q',   '2': '3wq1',   '3': '4ew2',   '4': '5re3',   '5': '6tr4',   '6': '7zt5',   '7': '8uz6',   '8': '9iu7',   '9': '0oi8',   '0': 'po9',
        'q': '12wa', 'w': '23esaq', 'e': '34rdsw', 'r': '45tfde', 't': '56zgfr', 'z': '67uhgt', 'u': '78ijhz', 'i': '89okju', 'o': '90plki', 'p': '0lo',
        'a': 'qwsy', 's': 'wedxya', 'd': 'erfcxs', 'f': 'rtgvcd', 'g': 'tzhbvf', 'h': 'zujnbg', 'j': 'uikmnh', 'k': 'iol,mj',  'l': 'op.,k',
        'y': 'asx',  'x': 'sdcy',   'c': 'dfvx',   'v': 'fgbc',   'b': 'ghnv',   'n': 'hjmn',   'm': 'jk,n'
        },
    'azerty': {
        '1': '2a',   '2': '3za1',   '3': '4ez2',   '4': '5re3',   '5': '6tr4',   '6': '7yt5',   '7': '8uy6',   '8': '9iu7',   '9': '0oi8',   '0': 'po9',
        'a': '12qa', 'z': '23esqa', 'e': '34rdsz', 'r': '45tfde', 't': '56ygfr', 'y': '67uhgt', 'u': '78ijhy', 'i': '89okju', 'o': '90plki', 'p': '0mlo',
        'q': 'azsw', 's': 'zedxwq', 'd': 'erfcxs', 'f': 'rtgvcd', 'g': 'tyhbvf', 'h': 'yujnbg', 'j': 'uiknh',  'k': 'iol.j',  'l': 'opm.k',  'm': 'pl',
        'w': 'qsx',  'x': 'sdcw',   'c': 'dfvx',   'v': 'fgbc',   'b': 'ghnv',   'n': 'hjb'
        },
    'dvorak': {
        '1': '2',     '2': '31',     '3': '4.2',     '4': '5p.3',   '5': '6yp4',    '6': '7fy5',   '7': '8gf6',   '8': '9cg7',   '9': '0rc8',   '0': 'lr9',
        '.': '4peo3', 'p': '5yue.4', 'y': '6fiup5',  'f': '7gdiy6', 'g': '8chdf7',  'c': '9rthg8', 'r': '0lntc9', 'l': 'snr0',
        'a': 'o',     'o': '.eq',    'e': '.peujqo', 'u': 'pyikje', 'i': 'yfdxkku', 'd': 'fghbxi', 'h': 'gctmbd', 't': 'crnwmh', 'n': 'rlsvwt', 's': 'lzvn',
        'q': 'oej',   'j': 'eukq',   'k': 'uixj',    'x': 'idbk',   'b': 'dhmx',    'm': 'htwb',   'w': 'tnvm',   'v': 'nszv',   'z': 'sv'
        }
    }

def addition(text, layouts=keyboard.keys()):
    """Generate all permutations of one extra key stroke (fat fingers)."""
    result = set()

    text = text.lower()
    for layout in layouts:
        for i in range(0, len(text)):
            if text[i] not in keyboard[layout]:
                continue
            for c in keyboard[layout][text[i]]:
                result.add(text[:i] + c + text[i:])
                result.add(text[:i+1] + c + text[i+1:])

    return result

def replacement(text, layouts=keyboard.keys()):
    """Generate all permutations of one misplaced key stroke."""
    result = set()

    for layout in layouts:
        for i in range(0, len(text)):
            if text[i] not in keyboard[layout]:
                continue
            for c in keyboard[layout][text[i]]:
                # TODO Consider duplicate characters (tt, ll, ss, ...)
                result.add(text[:i] + c + text[i+1:])

    return result

def fuzz(text):
    """Return all keyboard fuzzing permutations of 'text'"""
    result = set()
    text = text.lower()
    result.update(addition(text))
    result.update(replacement(text))

    return result
