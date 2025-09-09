"""
python examples/writer/format.py
"""

from gumwrapper import GumWriter


def example():
    code = """def hello():
    print('Hello World!')"""
    formatted = GumWriter.format(code, language="python", format_type="code")
    print(formatted)


if __name__ == "__main__":
    example()