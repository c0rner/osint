"""Decorator-based function registry for fuzzing methods."""
from collections.abc import Callable

methods: dict[str, Callable[..., set[str]]] = {}


def add(desc: str | None = None, group: str | None = None) -> Callable:
    """Register a fuzzing function with an optional description and group."""
    def ret(func: Callable) -> Callable:
        func.help = desc
        func.group = group
        methods[func.__name__] = func
        return func
    return ret
