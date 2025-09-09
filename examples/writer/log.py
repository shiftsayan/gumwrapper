"""
python examples/writer/log.py
"""

from gumwrapper import GumWriter


def example():
    messages = ["Starting app", "Warning: low memory", "Process complete"]
    GumWriter.log(messages, level="info", formatter="text")


if __name__ == "__main__":
    example()