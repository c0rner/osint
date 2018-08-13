#!/usr/bin/env python

import argparse
import re
import wordfuzz

""" Domain name fuzzer
"""


# This regexp pattern is based on what is in the validators library
# by Konsta Vesterinen (https://github.com/kvesteri/validators)
domain_re = re.compile(
    r'^([a-zA-Z0-9][-_a-zA-Z0-9.]{0,61}[a-zA-Z0-9])+$'  # domain pt.3
    )
tld_re = re.compile(
    r'^([a-zA-Z]{2,13}|(xn--[a-zA-Z0-9]{2,30}))$'  # TLD
    )

def invalidated(items):
    discard = set()
    for domain in items:
        try:
            if not domain_re.match(domain.encode("idna")):
                discard.add(domain)
        except:
            discard.add(domain)
    return discard

def gen_help(ap, name, description, functions):
    group = parser.add_argument_group(name, description)
    for func in functions:
        helpstring = functions[func].__doc__.splitlines()[0]
        group.add_argument('--{}'.format(func), dest='functions', action='append_const', const=func, help=helpstring.lower())

def process(text, mutators, functions):
    result = set()
    for func in functions:
        if func not in mutators:
            continue
        result.update(mutators[func](text))
    return result

parser = argparse.ArgumentParser(description='Domain name fuzzer')
parser.add_argument('domain', type=str)
parser.add_argument('tld', type=str, nargs='?')
parser.add_argument('-a', '--all', action='store_true', help='Run all mutator functions')
gen_help(parser, 'Keyboard', 'Mutators based on keyboard layout', wordfuzz.keyboard.cmd.fuzzers)
#gen_help(parser, 'Noise', 'Mutators based on noise', wordfuzz.noise.cmd.fuzzers)
#gen_help(parser, 'Language', 'Mutators based on language constructs', wordfuzz.language.cmd.fuzzers)

args = vars(parser.parse_args())
if args['domain'] is None:
    parser.print_help()
    exit()
if args['tld']:
    tld = args['tld']
if args['all']:
    args['functions'] = []

result = process(args['domain'], wordfuzz.cmd.fuzzers, args['functions'])

invalid_domains = invalidated(result)
result.difference_update(invalid_domains)
print("Generated {} valid domain name variations".format(len(result),len(invalid_domains)))

for domain in sorted(result):
    print("{}{}".format(domain.encode("idna"), tld))
