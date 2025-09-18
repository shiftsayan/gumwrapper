"""
python examples/writer/spin.py
"""

from gumwrapper import GumWriter


def example():
    GumWriter.spin(title="Processing...", command="sleep 3", show_output=True)


if __name__ == "__main__":
    example()
