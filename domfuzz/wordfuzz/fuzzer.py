# -*- coding: utf-8 -*-

engines = {}

def add(func, group=None):
    global fuzzers
    if func.__doc__ is not None:
        func.help = func.__doc__.splitlines()[0]

    func.group = group
    engines[func.__name__] = func
    return func
