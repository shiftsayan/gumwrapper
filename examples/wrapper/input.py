"""
python input.py
python input.py --first_name "Alice" --last_name "Doe"
python input.py --first_name "Alice" --age 25
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument(
    "age",
    int,
    "input",
    message="Age",
    placeholder="25",
)
@argument(
    "last_name",
    str,
    "input",
    message="Last",
    placeholder="Enter your last name",
    default="N/A",
)
@argument(
    "first_name", str, "input", message="First", placeholder="Enter your first name"
)
def example(first_name: str, last_name: str, age: int):
    print(f"[first_name] {value_and_type(first_name)}")
    print(f"[last_name] {value_and_type(last_name)}")
    print(f"[age] {value_and_type(age)}")


if __name__ == "__main__":
    example()
