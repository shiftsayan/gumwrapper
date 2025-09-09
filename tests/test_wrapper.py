import inspect
from typing import get_args

from gumwrapper.wrapper import GumType, GumWrapper


def test_gum_type():
    """Test that all GumWrapper methods match the GumType literal."""
    input_methods = tuple(
        name
        for name, _ in inspect.getmembers(GumWrapper, predicate=inspect.isfunction)
        if not name.startswith("_")
    )
    assert sorted(input_methods) == sorted(get_args(GumType))


def test_all_methods_exist():
    """Test that all expected gum commands have corresponding wrapper methods."""
    expected_methods = [
        "choose",
        "confirm",
        "input",
        "write",
        "filter",
        "spin",
        "file",
        "format",
        "join",
        "pager",
        "style",
        "table",
        "log",
    ]

    for method_name in expected_methods:
        assert hasattr(
            GumWrapper, method_name
        ), f"Method {method_name} not found in GumWrapper"
        method = getattr(GumWrapper, method_name)
        assert callable(method), f"Method {method_name} is not callable"


def test_gum_type_completeness():
    """Test that GumType includes all expected command types."""
    gum_types = get_args(GumType)
    expected_types = [
        "choose",
        "confirm",
        "input",
        "write",
        "filter",
        "spin",
        "file",
        "format",
        "join",
        "pager",
        "style",
        "table",
        "log",
    ]

    for expected_type in expected_types:
        assert expected_type in gum_types, f"Type {expected_type} not found in GumType"
