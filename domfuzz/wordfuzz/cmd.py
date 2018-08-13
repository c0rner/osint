# -*- coding: utf-8 -*-

fuzzers = {}

def add(func, group=None):
    global fuzzers
    if func.__doc__ is not None:
        func.help = func.__doc__.splitlines()[0]

    func.group = group
    fuzzers[func.__name__] = func
    return func

class ddfuzzer(object):
    def __init__(self, help=None):
        self.help = help

    def __call__(self, func):
        func.help = self.help
        fuzzers[func.__name__] = func
        return func
