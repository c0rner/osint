"""Standalone CLI entry point for wordfuzz."""
import argparse

from . import arg
from . import noise      # noqa: F401 – registers noise methods
from . import keyboard   # noqa: F401 – registers keyboard methods
from . import language   # noqa: F401 – registers language methods

# Map CLI group flags to the registered method names they cover.
_GROUPS: dict[str, list[str]] = {
    'kbd':   ['addition', 'replacement'],
    'noise': ['append', 'bitflip', 'omission', 'prepend', 'repetition', 'transposition'],
    'lang':  ['homograph', 'hyphenation', 'vowelswap'],
}


def main() -> None:
    parser = argparse.ArgumentParser(description='Generate text permutations')
    parser.add_argument('text', type=str)
    parser.add_argument('-k', '--kbd',   action='store_true', help='Keyboard mutations')
    parser.add_argument('-n', '--noise', action='store_true', help='Noise mutations')
    parser.add_argument('-l', '--lang',  action='store_true', help='Language mutations')
    args = vars(parser.parse_args())

    selected: list[str] = []
    for flag, methods in _GROUPS.items():
        if args[flag]:
            selected.extend(methods)

    if not selected:
        parser.print_help()
        return

    result: set[str] = set()
    word: str = args['text']
    for name in selected:
        if name in arg.methods:
            result.update(arg.methods[name](word))

    for r in sorted(result):
        print(r)


if __name__ == '__main__':
    main()
