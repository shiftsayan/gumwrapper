import inspect
from typing import get_args

from gumwrapper.wrapper import GumType, GumWrapper


def test_gum_type():
    """Test that GumType only contains input methods."""
    gum_types = get_args(GumType)
    expected_input_methods = ["choose", "confirm", "input", "write", "filter", "file"]
    assert sorted(gum_types) == sorted(expected_input_methods)


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
    """Test that GumType only includes input methods, not output methods."""
    gum_types = get_args(GumType)
    input_methods = ["choose", "confirm", "input", "write", "filter", "file"]
    output_methods = ["spin", "format", "join", "pager", "style", "table", "log"]

    # All input methods should be in GumType
    for input_method in input_methods:
        assert input_method in gum_types, f"Input method {input_method} not found in GumType"
    
    # No output methods should be in GumType
    for output_method in output_methods:
        assert output_method not in gum_types, f"Output method {output_method} should not be in GumType"
