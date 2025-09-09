#!/usr/bin/env python3

from gumwrapper.decorator import argument, GUM_DATA_KEY

print("Testing decorator...")

@argument("test", str)
def test_func():
    pass

print(f"Function: {test_func}")
print(f"Has attribute: {hasattr(test_func, GUM_DATA_KEY)}")
print(f"Attribute value: {getattr(test_func, GUM_DATA_KEY, 'NOT_FOUND')}")