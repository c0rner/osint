#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import argparse
    import noise
    import keyboard
    import language

    parser = argparse.ArgumentParser(description='Generate text permutations')
    parser.add_argument('text', type=str)
    args = vars(parser.parse_args())

    result = set()
    word = args['text']
    result.update(keyboard.complete(word))
    result.update(language.complete(word))
    result.update(noise.complete(word))

    for r in result:
        print(r.encode('utf-8'))

if __name__ == '__main__':
    main()
