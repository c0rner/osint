"""Noise-based text mutation functions."""
import string

from . import arg


@arg.add(desc="Append a-z to word")
def append(word: str) -> set[str]:
    """Generates all permutations of character a-z appended to *word*."""
    return {word + c for c in string.ascii_lowercase}


@arg.add(desc="Bitflip a character in word")
def bitflip(word: str) -> set[str]:
    """Generates all permutations of a single bitflipped character of *word*."""
    result = set()
    for i, ch in enumerate(word):
        for bit in (1, 2, 4, 8, 16, 64, 128):
            flipped = ord(ch) ^ bit
            if 32 <= flipped <= 127:
                result.add(word[:i] + chr(flipped) + word[i + 1:])
    return result


@arg.add(desc="Omit a single character in word")
def omission(word: str) -> set[str]:
    """Generates all permutations of a single omitted character in *word*."""
    return {word[:i] + word[i + 1:] for i in range(len(word))}


@arg.add(desc="Prepend a-z to word")
def prepend(word: str) -> set[str]:
    """Generates all permutations of character a-z prepended to *word*."""
    return {c + word for c in string.ascii_lowercase}


@arg.add(desc="Repeat a character in word")
def repetition(word: str) -> set[str]:
    """Generates all permutations of a repeated character in *word*."""
    return {word[:i] + word[i] + word[i:] for i in range(len(word))}


@arg.add(desc="Transpose (swap) two characters in word")
def transposition(word: str) -> set[str]:
    """Generates all permutations of two transposed characters in *word*."""
    return {word[:i] + word[i + 1] + word[i] + word[i + 2:] for i in range(len(word) - 1)}
