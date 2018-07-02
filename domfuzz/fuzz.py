#!/usr/bin/env python
# -*- coding: utf-8 -*-

class KeyboardFuzzer():
    layout = {
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

    def __addition(self, text):
        """Generate all permutations of one extra key stroke (fat fingers)."""
        result = set()

        text = text.lower()
        for layout in self.fuzz_layouts:
            for i in range(0, len(text)):
                if text[i] not in self.layout[layout]:
                    continue
                for c in self.layout[layout][text[i]]:
                    result.add(text[:i] + c + text[i:])
                    result.add(text[:i+1] + c + text[i+1:])

        return result

    def __replacement(self, text):
        """Generate all permutations of one misplaced key stroke."""
        result = set()

        for layout in self.fuzz_layouts:
            for i in range(0, len(text)):
                if text[i] not in self.layout[layout]:
                    continue
                for c in self.layout[layout][text[i]]:
                    # TODO Consider duplicate characters (tt, ll, ss, ...)
                    result.add(text[:i] + c + text[i+1:])

        return result

    def fuzz(self, text):
        """Return all keyboard fuzzing permutations of 'text'"""
        # TODO Should spacebar be included?
        result = set()
        text = text.lower()
        result.update(self.__addition(text))
        result.update(self.__replacement(text))

        return list(result)

    def __init__(self, layouts=None, fullstop=False):
        self.fullstop = fullstop # FIXME Implement exclusion of fullstop "."
        if not layouts:
            layouts=self.layouts()
        self.fuzz_layouts = set(layouts).intersection(self.layouts())


    def layouts(self):
        return self.layout.keys()


class LangFuzzer():
    def __homograph(self, text):
        result = set()
        homoglyphs = {
                'alnum': { '0': 'o', '1': 'l', '5': 's', 'i': ['1', 'l'], 'l': ['1', 'i'], 'o': '0', 's': '5' },
                'armenian': { '1': u'Լ', 'l': u'Լ' },
                'cyrillic': { 'a': u'а', 'c': u'с', 'e': u'е', 'o': u'о', 'p': u'р', 'x': u'х', 'y': u'у' },
                'greek': { '0': u'Ο', '1': u'Ι', 'c': u'ϲ', 'i': u'Ι', 'l': u'Ι', 'o': u'ο', 'p': u'ρ', 'u': u'υ', 'v': u'ν' }
                }

        # TODO Include all permutations (multiple replacements)
        for i in range(0, len(text)):
            for name,glyphs in homoglyphs.iteritems():
                if text[i] not in glyphs:
                    continue
                for glyph in glyphs[text[i]]:
                    # DEBUG print("Name: {}, Glyph '{}' -> '{}'".format(name, text[i], glyph.encode('utf-8')))
                    result.add(text[:i] + glyph + text[i+1:])
        return result

    def __hyphenation(self, text):
        result = set()

        for i in range(1, len(text)):
            result.add(text[:i] + '-' + text[i:])

        return result

    def __vowelswap(self, text):
        result = set()
        vowels = 'aeiou'
        for i in range(0, len(text)):
            for vowel in vowels:
                if text[i] not in vowels:
                    continue
                result.add(text[:i] + vowel + text[i+1:])
        return result

    def fuzz(self, text):
        result = set()
        result.update(self.__homograph(text))
        result.update(self.__hyphenation(text))
        result.update(self.__vowelswap(text))

        return list(result)


class NoiseFuzzer():
    def __append(self, text):
        result = set()

        for i in range(ord('a'), ord('z') + 1):
            result.add(text + chr(i))

        return result

    def __bitflip(self, text):
        """Generate all permutations of one bit flipped character."""
        result = set()
        for i in range(0, len(text)):
            for bit in [ 1, 2, 4, 8, 16, 64, 128 ]:
                flipped = ord(text[i]) ^ bit
                if flipped < 32 or flipped > 127:
                    continue
                result.add(text[:i] + chr(flipped) + text[i+1:])
        return result

    def __omission(self, text):
        """Generate all permutations of one missing character."""
        result = set()

        for i in range(0, len(text)):
            result.add(text[:i] + text[i+1:])

        return result

    def __repetition(self, text):
        """Generate all permutations of a repeated character."""
        result = set()

        for i in range(0, len(text)):
            result.add(text[:i] + text[i] + text[i:])

        return result

    def fuzz(self, text):
        result = set()
        result.update(self.__append(text))
        result.update(self.__bitflip(text))
        result.update(self.__omission(text))
        result.update(self.__repetition(text))

        return list(result)

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate text permutations')
    parser.add_argument('text', type=str)
    args = vars(parser.parse_args())

    kbd = KeyboardFuzzer(['qwerty', 'qwertz', 'azerty'])
    lang = LangFuzzer()
    noise = NoiseFuzzer()

    result = set()
    word = args['text']
    result.update(kbd.fuzz(word))
    result.update(lang.fuzz(word))
    result.update(noise.fuzz(word))

    for r in result:
        print("{}\t{}".format(r.encode('utf-8'), r.encode('idna')))


if __name__ == '__main__':
    main()
