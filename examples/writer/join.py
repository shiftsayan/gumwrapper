"""
python examples/writer/join.py
"""

from gumwrapper import GumWriter


def example():
    items = ["item1", "item2", "item3"]
    joined = GumWriter.join(items, vertical=True, align="center")
    print(joined)


if __name__ == "__main__":
    example()
