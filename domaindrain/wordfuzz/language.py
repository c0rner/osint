"""Language/script-based text mutation functions."""
from . import arg

# Homoglyph tables, keyed by script name.  Each mapping value is always a
# list of replacement glyphs so callers can iterate uniformly.
_HOMOGLYPHS: dict[str, dict[str, list[str]]] = {
    'alnum': {
        '0': ['o'],
        '1': ['i', 'l'],
        '5': ['s'],
        'i': ['1', 'l'],
        'l': ['1', 'i'],
        'o': ['0'],
        's': ['5'],
    },
    'armenian': {
        '1': ['\u053c'],  # 'Լ'
        'l': ['\u053c'],  # 'Լ'
        't': ['\u0567'],  # 'է'
    },
    'cyrillic': {
        'a': ['\u0430'],  # 'а'
        'e': ['\u0435'],  # 'е'
        'o': ['\u043e'],  # 'о'
        'p': ['\u0440'],  # 'р'
        'c': ['\u0441'],  # 'с'
        'y': ['\u0443'],  # 'у'
        'x': ['\u0445'],  # 'х'
        's': ['\u0455'],  # 'ѕ'
        'i': ['\u0456'],  # 'і'
        'j': ['\u0458'],  # 'ј'
    },
    'greek': {
        'i': ['\u03af', '\u03b9'],  # 'ί', 'ι'
        'l': ['\u03b9'],            # 'ι'
        'v': ['\u03bd'],            # 'ν'
        'o': ['\u03bf'],            # 'ο'
        'u': ['\u03c5'],            # 'υ'
        'q': ['\u03e5'],            # 'ϥ'
        'c': ['\u03f2'],            # 'ϲ'
        'j': ['\u03f3'],            # 'ϳ'
    },
    'latin': {
        '\u00e4': ['\u00e2', '\u00e3', '\u0101', '\u0103', '\u01df', '\u0201', '\u0203'],  # ä → â ã ā ă ǟ ȁ ȃ
        '\u00e5': ['\u00e0', '\u00e1', '\u0103', '\u01e1', '\u01fb', '\u0227'],            # å → à á ǡ ǻ ȧ
        '\u00f6': ['\u00f0', '\u00f4', '\u00f5', '\u014d', '\u014f', '\u0151', '\u020d', '\u020f'],  # ö → ð ô õ ō ŏ ő ȍ ȏ
        '\u00f8': ['\u01ff'],                                                              # ø → ǿ
        'i': ['\u00ec', '\u00ed', '\u00ee', '\u00ef', '\u0129', '\u013a'],  # ì í î ï ĩ ĺ
        'a': ['\u0105', '\u0227'],                      # ą ȧ
        'c': ['\u0109', '\u010b'],                      # ĉ ċ
        'd': ['\u010f', '\u0111'],                      # ď đ
        'e': ['\u0117', '\u0119'],                      # ė ę
        'g': ['\u011d', '\u0121', '\u0123'],            # ĝ ġ ģ
        'j': ['\u0135', '\u013c'],                      # ĵ ļ
        'k': ['\u0137'],                                # ķ
        'l': ['\u013a', '\u013c', '\u013e', '\u0142'],  # ĺ ļ ľ ł
        'n': ['\u0146'],                                # ņ
        'r': ['\u0155', '\u0157'],                      # ŕ ŗ
        's': ['\u015d', '\u015f'],                      # ŝ ş
        't': ['\u0163', '\u0165', '\u0167'],            # ţ ť ŧ
        'z': ['\u017a', '\u017c', '\u017e'],            # ź ż ž
        'o': ['\u00f8', '\u01a1'],                      # ø ơ
        'u': ['\u01b0'],                                # ư
        'q': ['\u01eb'],                                # ǫ
        'ae': ['\u00e6', '\u01fd'],                     # æ ǽ
        'nj': ['\u014b'],                               # ŋ
        'oe': ['\u0153'],                               # œ
        'hu': ['\u0195'],                               # ƕ
        'ur': ['\u01b0'],                               # ư
    },
}


@arg.add(desc="Replace a character with a homoglyph")
def homograph(text: str, script: list[str] | None = None) -> set[str]:
    """
    Generates all permutations of a single replaced character of *text*
    depending on the script(s) selected.

    Please note that in modern browsers two different scripts cannot be
    mixed or punycode is shown (e.g. Latin + Armenian produces punycode).

    See the Google Chrome IDN policy for details:
    https://www.chromium.org/developers/design-documents/idn-in-google-chrome
    """
    if script is None:
        script = ['latin']

    result: set[str] = set()

    for i, ch in enumerate(text):
        for name in script:
            for glyph in _HOMOGLYPHS[name].get(ch, []):
                result.add(text[:i] + glyph + text[i + 1:])

    # TODO Support combinations (example hi -> 'ŀi')
    for i in range(len(text) - 1):
        bigram = text[i:i + 2]
        for name in script:
            for glyph in _HOMOGLYPHS[name].get(bigram, []):
                result.add(text[:i] + glyph + text[i + 2:])

    return result


@arg.add(desc="Inserted hyphen")
def hyphenation(text: str) -> set[str]:
    """Generate all permutations of an inserted hyphen in *text*."""
    return {text[:i] + '-' + text[i:] for i in range(1, len(text))}


@arg.add(desc="Swap a vowel")
def vowelswap(text: str) -> set[str]:
    """Generate all permutations of a swapped vowel in *text*."""
    vowels = 'aeiou'
    result: set[str] = set()
    for i, ch in enumerate(text):
        if ch not in vowels:
            continue
        for vowel in vowels:
            result.add(text[:i] + vowel + text[i + 1:])
    return result
