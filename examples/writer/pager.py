"""
python examples/writer/pager.py
"""

from gumwrapper import GumWriter


def example():
    content = """This is a long text that will be displayed in a pager.

You can scroll through this content using the pager interface.

Line 1
Line 2
Line 3
...and so on."""
    GumWriter.pager(content=content, show_line_numbers=True)


if __name__ == "__main__":
    example()
