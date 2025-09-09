from typing import get_args

from gumwrapper.wrapper import GumPrompt, GumWrite, PromptType


def test_gum_type():
    """Test that GumType only contains input methods."""
    gum_types = get_args(PromptType)
    expected_input_methods = ["choose", "confirm", "input", "write", "filter", "file"]
    assert sorted(gum_types) == sorted(expected_input_methods)


def test_all_input_methods_exist():
    """Test that all expected input commands have corresponding GumWrapper methods."""
    expected_input_methods = [
        "choose",
        "confirm",
        "input",
        "write",
        "filter",
        "file",
    ]

    for method_name in expected_input_methods:
        assert hasattr(
            GumPrompt, method_name
        ), f"Input method {method_name} not found in GumWrapper"
        method = getattr(GumPrompt, method_name)
        assert callable(method), f"Input method {method_name} is not callable"


def test_all_output_methods_exist():
    """Test that all expected output commands have corresponding GumWriter methods."""
    expected_output_methods = [
        "spin",
        "format",
        "join",
        "pager",
        "style",
        "table",
        "log",
    ]

    for method_name in expected_output_methods:
        assert hasattr(
            GumWrite, method_name
        ), f"Output method {method_name} not found in GumWriter"
        method = getattr(GumWrite, method_name)
        assert callable(method), f"Output method {method_name} is not callable"


def test_gum_type_completeness():
    """Test that GumType only includes input methods, not output methods."""
    gum_types = get_args(PromptType)
    input_methods = ["choose", "confirm", "input", "write", "filter", "file"]
    output_methods = ["spin", "format", "join", "pager", "style", "table", "log"]

    # All input methods should be in GumType
    for input_method in input_methods:
        assert (
            input_method in gum_types
        ), f"Input method {input_method} not found in GumType"

    # No output methods should be in GumType
    for output_method in output_methods:
        assert (
            output_method not in gum_types
        ), f"Output method {output_method} should not be in GumType"
