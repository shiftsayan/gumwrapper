import inspect
from typing import get_args

from gumwrapper.wrapper import GumType, GumWrapper


def test_gum_type():
    input_methods = tuple(
        name
        for name, _ in inspect.getmembers(GumWrapper, predicate=inspect.isfunction)
        if not name.startswith("_")
    )
    assert sorted(input_methods) == sorted(get_args(GumType))
