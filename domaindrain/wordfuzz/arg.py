# -*- coding: utf-8 -*-

methods = {}

def add(desc=None, group=None):
    def ret(func):
        func.help = desc
        func.group = group
        methods[func.__name__] = func
        return func
    return ret
