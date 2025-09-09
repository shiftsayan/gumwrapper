"""
python examples/writer/style.py
"""

from gumwrapper import GumWriter


def example():
    text = "Hello World"
    styled = GumWriter.style(text, foreground="blue", border="rounded", padding="1", bold=True)
    print(styled)


if __name__ == "__main__":
    example()