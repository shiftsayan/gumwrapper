"""
Utility functions for common formatting and output operations.
These are direct wrappers around GumWriter methods for convenience.
"""

from gumwrapper.wrapper import GumWrite


def format_text(
    template: str | list[str] | None = None,
    theme: str | None = None,
    language: str | None = None,
    format_type: str = "markdown",
) -> str:
    """
    Format text using gum format command.

    Args:
        template: Text to format (markdown, code, etc.)
        theme: Color theme to use
        language: Programming language for syntax highlighting
        format_type: Type of formatting ("markdown", "code", etc.)

    Returns:
        Formatted text string
    """
    return GumWrite.format(
        template=template, theme=theme, language=language, format_type=format_type
    )


def spin(
    title: str,
    command: str = "",
    spinner: str | None = None,
    show_output: bool = False,
) -> None:
    """
    Show a spinner while running a command.

    Args:
        title: Title to display next to spinner
        command: Shell command to run
        spinner: Spinner style ("dot", "line", "arc", etc.)
        show_output: Whether to show command output
    """
    GumWrite.spin(
        title=title, command=command, spinner=spinner, show_output=show_output
    )


def style(
    text: str | list[str] | None = None,
    foreground: str | None = None,
    background: str | None = None,
    border: str | None = None,
    border_background: str | None = None,
    border_foreground: str | None = None,
    align: str | None = None,
    height: int | None = None,
    width: int | None = None,
    margin: str | None = None,
    padding: str | None = None,
    bold: bool = False,
    faint: bool = False,
    italic: bool = False,
    strikethrough: bool = False,
    underline: bool = False,
) -> str:
    """
    Style text with colors, borders, and formatting.

    Args:
        text: Text to style
        foreground: Foreground color
        background: Background color
        border: Border style ("rounded", "thick", "double", "dashed", etc.)
        border_background: Border background color
        border_foreground: Border foreground color
        align: Text alignment ("left", "center", "right")
        height: Box height in lines
        width: Box width in characters
        margin: Margin spacing
        padding: Padding spacing
        bold: Bold text
        faint: Faint text
        italic: Italic text
        strikethrough: Strikethrough text
        underline: Underlined text

    Returns:
        Styled text string
    """
    return GumWrite.style(
        text=text,
        foreground=foreground,
        background=background,
        border=border,
        border_background=border_background,
        border_foreground=border_foreground,
        align=align,
        height=height,
        width=width,
        margin=margin,
        padding=padding,
        bold=bold,
        faint=faint,
        italic=italic,
        strikethrough=strikethrough,
        underline=underline,
    )


def pager(
    content: str | None = None,
    show_line_numbers: bool = False,
    soft_wrap: bool = False,
    timeout: int | None = None,
) -> None:
    """
    Display content in a scrollable pager.

    Args:
        content: Content to display
        show_line_numbers: Show line numbers
        soft_wrap: Enable soft wrapping
        timeout: Timeout in seconds
    """
    GumWrite.pager(
        content=content,
        show_line_numbers=show_line_numbers,
        soft_wrap=soft_wrap,
        timeout=timeout,
    )


# Convenience functions with shorter names
def fmt(template: str, **kwargs) -> str:
    """Shorthand for format_text()."""
    return format_text(template, **kwargs)


def loading(title: str, command: str = "", **kwargs) -> None:
    """Shorthand for spin() - more descriptive name."""
    return spin(title, command, **kwargs)


def box(text: str, **kwargs) -> str:
    """Create a styled box around text."""
    defaults = {"border": "rounded", "padding": "1"}
    return style(text, **{**defaults, **kwargs})


def success(text: str) -> str:
    """Style text as a success message."""
    return style(text, foreground="green", bold=True)


def error(text: str) -> str:
    """Style text as an error message."""
    return style(text, foreground="red", bold=True)


def warning(text: str) -> str:
    """Style text as a warning message."""
    return style(text, foreground="yellow", bold=True)


def info(text: str) -> str:
    """Style text as an info message."""
    return style(text, foreground="blue", bold=True)


def code(text: str, language: str | None = None) -> str:
    """Format text as code with syntax highlighting."""
    return format_text(text, language=language, format_type="code")


def markdown(text: str, theme: str | None = None) -> str:
    """Format text as markdown."""
    return format_text(text, theme=theme, format_type="markdown")
