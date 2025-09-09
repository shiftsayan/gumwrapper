"""
python examples/writer/table.py
"""

from gumwrapper import GumWriter


def example():
    data = "name,age\nAlice,30\nBob,25"
    result = GumWriter.table(data=data, separator=",", height=10, print_static=True)
    print(result)


if __name__ == "__main__":
    example()