#!/usr/bin/env python3

from gumwrapper import argument
from gumwrapper.decorator import GUM_DATA_KEY

@argument("test", bool, "confirm", message="Test message")
def test_func(test: bool):
    print(f"Test: {test}")

print(f"Function: {test_func}")
print(f"Has {GUM_DATA_KEY}: {hasattr(test_func, GUM_DATA_KEY)}")

if hasattr(test_func, GUM_DATA_KEY):
    data = getattr(test_func, GUM_DATA_KEY)
    print(f"GUM_DATA length: {len(data)}")
    for i, arg in enumerate(data):
        print(f"  {i}: {arg.argument_name} ({arg.gum_wrapper_type})")
else:
    print("No GUM_DATA_KEY found!")

# Try to call it
print("Calling test_func()...")
test_func()