"""
python choose.py
python choose.py --color green
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument("color", str, "choose", choices=["red", "green", "blue"])
def example(color: str):
    print(f"[color] {value_and_type(color)}")


if __name__ == "__main__":
    example()
