#!/usr/bin/env python

import argparse
import json
import re
import wordfuzz

""" Domain name fuzzer
"""


# This regexp pattern is based on what is in the validators library
# by Konsta Vesterinen (https://github.com/kvesteri/validators)
label_re = re.compile(
    r'^([a-zA-Z0-9][-_a-zA-Z0-9.]{0,61}[a-zA-Z0-9])+$'
    )
tld_re = re.compile(
    r'^([a-zA-Z]{2,13}|(xn--[a-zA-Z0-9]{2,30}))$'  # TLD
    )

def is_valid_label(label):
    return label_re.match(label)

def gen_help(ap, name, description, functions):
    group = parser.add_argument_group(name, description)
    for func in functions:
        helpstring = functions[func].__doc__.splitlines()[0]
        group.add_argument('--{}'.format(func), dest='functions', action='append_const', const=func, help=helpstring.lower())

def process(text, mutators, functions):
    result = {}
    for func in functions:
        if func not in mutators:
            continue
        result[func] = mutators[func](text)
    return result

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


parser = argparse.ArgumentParser(description='Domain label fuzzer')
parser.add_argument('label', type=str)
gen_help(parser, 'Options', 'Word fuzzers', wordfuzz.fuzzer.engines)
#gen_help(parser, 'Keyboard', 'Mutators based on keyboard layout', wordfuzz.keyboard.cmd.fuzzers)
#gen_help(parser, 'Noise', 'Mutators based on noise', wordfuzz.noise.cmd.fuzzers)
#gen_help(parser, 'Language', 'Mutators based on language constructs', wordfuzz.language.cmd.fuzzers)

args = vars(parser.parse_args())
if args['label'] is None:
    parser.print_help()
    exit()

fuzzed_output = process(args['label'].decode('utf8'), wordfuzz.fuzzer.engines, args['functions'])

result = {}
for fuzzer in fuzzed_output:
    result[fuzzer] = {}
    for word in fuzzed_output[fuzzer]:
        if not is_valid_label(word.encode("idna")):
            continue
        result[fuzzer][word] = {}
        result[fuzzer][word]['idna'] = word.encode("idna")
        result[fuzzer][word]['python'] = word.encode("unicode_escape")
        print("{},{},{}".format(fuzzer, word.encode("idna"), word.encode("utf8")))

#print("# Generated {} valid domain name variations ({} were discarded)".format(len(result),len(invalid_domains)))
#print("JSON: {}".format(json.dumps(domains, indent=2, default=set_default, ensure_ascii=False).encode('utf8')))
#print("JSON: {}".format(json.dumps(result, indent=2, ensure_ascii=False).encode('utf8')))
