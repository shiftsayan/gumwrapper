"""
python write.py
python write.py --message "Hello World"
"""

from examples.utils import value_and_type

from gumwrapper import argument


@argument(
    "message",
    str,
    "write",
    placeholder="Enter your message...\n\nType multiple lines here.",
)
def example(message: str):
    print(f"[message] {value_and_type(message)}")


if __name__ == "__main__":
    example()
