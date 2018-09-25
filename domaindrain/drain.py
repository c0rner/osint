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
    r'^([a-zA-Z0-9][-_a-zA-Z0-9]{0,61})$'
    )
tld_re = re.compile(
    r'^([a-zA-Z]{2,13}|(xn--[a-zA-Z0-9]{2,30}))$'  # TLD
    )

def have_valid_labels(label):
    for l in label.split('.'):
        if not label_re.match(l.encode('idna')):
            return False
    return True

def gen_help(ap, name, description, functions):
    group = parser.add_argument_group(name, description)
    for func in functions:
        helpstring = functions[func].help
        group.add_argument('--{}'.format(func), dest='functions', action='append_const', const=func, help=helpstring.capitalize())

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
gen_help(parser, 'Options', 'Fuzzing methods', wordfuzz.arg.methods)

args = vars(parser.parse_args())
if args['label'] is None or args['functions'] is None:
    parser.print_help()
    exit()

fuzzed_output = process(args['label'].decode('utf8'), wordfuzz.arg.methods, args['functions'])

result = {}
for fuzzer in fuzzed_output:
    result[fuzzer] = {}
    for word in fuzzed_output[fuzzer]:
        if not have_valid_labels(word):
            continue
        result[fuzzer][word] = {}
        result[fuzzer][word]['idna'] = word.encode("idna")
        result[fuzzer][word]['python'] = word.encode("unicode_escape")
        print("{},{},{}".format(fuzzer, word.encode("idna"), word.encode("utf8")))
