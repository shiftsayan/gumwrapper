"""
python file.py
python file.py --filename "confirm.py"
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument("filename", str, "file", path=".")
def example(filename: str):
    print(f"[filename] {value_and_type(filename)}")


if __name__ == "__main__":
    example()
