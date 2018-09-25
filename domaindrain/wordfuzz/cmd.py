#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import argparse
    import noise
    import keyboard
    import language

    parser = argparse.ArgumentParser(description='Generate text permutations')
    parser.add_argument('text', type=str)
    parser.add_argument('-k', '--kbd', action='store_true', help='Keyboard mutations')
    parser.add_argument('-n', '--noise', action='store_true', help='Noise mutations')
    parser.add_argument('-l', '--lang', action='store_true', help='Language mutations')
    args = vars(parser.parse_args())

    result = set()
    word = args['text']
    if args['kbd']:
        result.update(keyboard.complete(word))
    if args['lang']:
        result.update(language.complete(word))
    if args['noise']:
        result.update(noise.complete(word))

    for r in result:
        print(r.encode('utf-8'))

if __name__ == '__main__':
    main()
