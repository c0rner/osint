#!/usr/bin/env python3
"""Domain name fuzzer.

Generates lookalike domain candidates from a given label and validates
each candidate against RFC 1123 hostname rules via IDNA encoding.
"""
import argparse
import re
import sys

import wordfuzz.arg  # importing the package populates wordfuzz.arg.methods

# RFC 1123 hostname label: starts and ends with alphanumeric, hyphens allowed
# in the middle, max 63 characters.  Underscores are intentionally excluded.
_LABEL_RE = re.compile(r'^[a-zA-Z0-9](?:[-a-zA-Z0-9]{0,61}[a-zA-Z0-9])?$')


def has_valid_labels(domain: str) -> bool:
    """Return True if every label in *domain* is a valid RFC 1123 hostname label."""
    for label in domain.split('.'):
        try:
            encoded = label.encode('idna').decode('ascii')
        except (UnicodeError, UnicodeDecodeError):
            return False
        if not _LABEL_RE.match(encoded):
            return False
    return True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Domain label fuzzer')
    parser.add_argument('label', type=str)
    group = parser.add_argument_group('Options', 'Fuzzing methods')
    for name, func in wordfuzz.arg.methods.items():
        help_text = (func.help or '').capitalize()
        group.add_argument(f'--{name}', dest='functions', action='append_const',
                           const=name, help=help_text)
    return parser


def process(text: str, functions: list[str]) -> dict[str, set[str]]:
    """Run each requested mutator on *text* and return a mapping of name → results."""
    return {
        name: wordfuzz.arg.methods[name](text)
        for name in functions
        if name in wordfuzz.arg.methods
    }


def main() -> None:
    parser = build_parser()
    args = vars(parser.parse_args())
    if not args.get('functions'):
        parser.print_help()
        sys.exit(1)

    for name, words in process(args['label'], args['functions']).items():
        for word in sorted(words):
            if not has_valid_labels(word):
                continue
            try:
                idna = word.encode('idna').decode('ascii')
            except UnicodeError:
                continue
            print(f'{name},{idna},{word}')


if __name__ == '__main__':
    main()
