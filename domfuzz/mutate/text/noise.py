#!/usr/bin/env python
# -*- coding: utf-8 -*-

def append(text):
    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(text + chr(i))

    return result

def bitflip(text):
    """Generate all permutations of one bit flipped character."""
    result = set()
    for i in range(0, len(text)):
        for bit in [ 1, 2, 4, 8, 16, 64, 128 ]:
            flipped = ord(text[i]) ^ bit
            if flipped < 32 or flipped > 127:
                continue
            result.add(text[:i] + chr(flipped) + text[i+1:])
    return result

def omission(text):
    """Generate all permutations of one missing character."""
    result = set()

    for i in range(0, len(text)):
        result.add(text[:i] + text[i+1:])

    return result

def prepend(text):
    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(chr(i) + text)

    return result

def repetition(text):
    """Generate all permutations of a repeated character."""
    result = set()

    for i in range(0, len(text)):
        result.add(text[:i] + text[i] + text[i:])

    return result

def transposition(text):
    """Generate all permutations of swapped characters."""
    result = set()

    for i in range(0, len(text) - 1):
        result.add(text[:i] + text[i+1] + text[i] + text[i+2:])
 
    return result

def complete(text):
    result = set()
    result.update(append(text))
    result.update(bitflip(text))
    result.update(omission(text))
    result.update(prepend(text))
    result.update(repetition(text))
    result.update(transposition(text))

    return result
