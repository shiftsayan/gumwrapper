"""
python choose.py
python choose.py --color green
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument("color1", str, "choose", choices=["red", "green", "blue"])
@argument("color2", str, "choose", choices=["red", "green", "blue"])
@argument("color3", str, "choose", choices=["red", "green", "blue"])
def example(color1: str, color2: str, color3: str):
    print(f"[color1] {value_and_type(color1)}")
    print(f"[color2] {value_and_type(color2)}")
    print(f"[color3] {value_and_type(color3)}")


if __name__ == "__main__":
    example()
