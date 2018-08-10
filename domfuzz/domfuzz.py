#!/usr/bin/env python

import argparse
import re
from mutate import text as mutext

""" This regexp pattern is based on what is in the validators library
    by Konsta Vesterinen (https://github.com/kvesteri/validators) """
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
        group.add_argument('--{}'.format(func), dest='functions', action='append_const', const=func, help=functions[func].__doc__)

def process(text, mutators, functions):
    result = set()
    for func in functions:
        if func not in mutators:
            continue
        result.update(mutators[func](text))
    return result

parser = argparse.ArgumentParser(description='Generate valid permutations of a domain name')
parser.add_argument('domain', type=str)
parser.add_argument('-a', '--all', action='store_true', help='Run all mutator functions')
gen_help(parser, 'Keyboard', 'Mutators based on keyboard layout', mutext.keyboard.functions)
gen_help(parser, 'Noise', 'Mutators based on noise', mutext.noise.functions)
gen_help(parser, 'Language', 'Mutators based on language constructs', mutext.language.functions)

mutators = {}
mutators.update(mutext.keyboard.functions)
mutators.update(mutext.language.functions)
mutators.update(mutext.noise.functions)

args = vars(parser.parse_args())
if args['domain'] is None:
    parser.print_help()
    exit()
if args['all']:
    args['functions'] = []

result = process(args['domain'], mutators, args['functions'])

invalid_domains = invalidated(result)
result.difference_update(invalid_domains)
print("Generated {} valid domain name variations".format(len(result),len(invalid_domains)))

for domain in sorted(result):
    print("{}".format(domain.encode("idna")))
