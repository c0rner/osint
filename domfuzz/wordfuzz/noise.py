#!/usr/bin/env python
# -*- coding: utf-8 -*-

import arg

@arg.add(desc="Append a-z to word")
def append(word):
    """
    Generates all permutations of character a-z appended to `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """

    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(word + chr(i))

    return result

@arg.add(desc="Bitflip a character in word")
def bitflip(word):
    """
    Generates all permutations of a single bitflipped characer of `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()
    for i in range(0, len(word)):
        for bit in [ 1, 2, 4, 8, 16, 64, 128 ]:
            flipped = ord(word[i]) ^ bit
            if flipped < 32 or flipped > 127:
                continue
            result.add(word[:i] + chr(flipped) + word[i+1:])
    return result

@arg.add(desc="Omit a single character in word")
def omission(word):
    """
    Generates all permutaions of a single imotted character in `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()

    for i in range(0, len(word)):
        result.add(word[:i] + word[i+1:])

    return result

@arg.add(desc="Prepend a-z to word")
def prepend(word):
    """
    Generates all permutations of character a-z prepended to `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(chr(i) + word)

    return result

@arg.add(desc="Repeat a character in word")
def repetition(word):
    """
    Generates all permutations of a repeated character in `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()

    for i in range(0, len(word)):
        result.add(word[:i] + word[i] + word[i:])

    return result

@arg.add(desc="Transpose (swap) two characters in word")
def transposition(word):
    """
    Generates all permutations of two transposed characters in `word`.

    Args:
        word: A single word

    Returns:
        A set of all possible permutations
    """
    result = set()

    for i in range(0, len(word) - 1):
        result.add(word[:i] + word[i+1] + word[i] + word[i+2:])
 
    return result
