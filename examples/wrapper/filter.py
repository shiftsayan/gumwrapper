"""
python filter.py
python filter.py --items "apple,banana"
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument(
    "items",
    list,
    "filter",
    choices=["apple", "banana", "cherry", "date", "elderberry", "fig"],
    limit=3,
)
def example(items: list[str]):
    print(f"[items] {value_and_type(items)}")


if __name__ == "__main__":
    example()
