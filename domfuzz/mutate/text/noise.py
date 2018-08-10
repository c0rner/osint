#!/usr/bin/env python
# -*- coding: utf-8 -*-

def append(text):
    """append a character"""
    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(text + chr(i))

    return result

def bitflip(text):
    """one bit flipped character"""
    result = set()
    for i in range(0, len(text)):
        for bit in [ 1, 2, 4, 8, 16, 64, 128 ]:
            flipped = ord(text[i]) ^ bit
            if flipped < 32 or flipped > 127:
                continue
            result.add(text[:i] + chr(flipped) + text[i+1:])
    return result

def omission(text):
    """omit a character"""
    result = set()

    for i in range(0, len(text)):
        result.add(text[:i] + text[i+1:])

    return result

def prepend(text):
    """prepend a character"""
    result = set()

    for i in range(ord('a'), ord('z') + 1):
        result.add(chr(i) + text)

    return result

def repetition(text):
    """repeat a character once"""
    result = set()

    for i in range(0, len(text)):
        result.add(text[:i] + text[i] + text[i:])

    return result

def transposition(text):
    """transpose (swap) two characters"""
    result = set()

    for i in range(0, len(text) - 1):
        result.add(text[:i] + text[i+1] + text[i] + text[i+2:])
 
    return result

functions = {"append": append, "bitflip": bitflip, "omission": omission, "prepend": prepend, "repetition": repetition, "transposition": transposition }
