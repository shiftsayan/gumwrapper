import shutil


def _check_gum_availability():
    """Check if gum CLI is available and raise ValueError if not."""
    if not shutil.which("gum"):
        raise ValueError(
            "gum CLI is not installed or not available in PATH. "
            "Please install gum from https://github.com/charmbracelet/gum"
        )


# Check gum availability on import
_check_gum_availability()

from gumwrapper.decorator import argument
from gumwrapper.utilities import (
    box,
    code,
    error,
    fmt,
    format_text,
    info,
    loading,
    markdown,
    pager,
    spin,
    style,
    success,
    warning,
)
from gumwrapper.wrapper import GumPrompt
from gumwrapper.writer import GumWriter

__all__ = [
    "GumPrompt",
    "GumWriter",
    "argument",
    # Utility functions
    "format_text",
    "spin",
    "style",
    "pager",
    # Convenience functions
    "fmt",
    "loading",
    "box",
    "success",
    "error",
    "warning",
    "info",
    "code",
    "markdown",
]
