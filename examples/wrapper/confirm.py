"""
python confirm.py
python confirm.py --delete
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument("delete", bool, "confirm", message="Delete all files?")
def example(delete: bool):
    print(f"[delete] {value_and_type(delete)}")


if __name__ == "__main__":
    example()
