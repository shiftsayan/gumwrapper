#!/usr/bin/env python3
"""Simple test for CLI functionality."""

from gumwrapper import argument

@argument("name", str, prompt_method="input", message="What's your name? ")
@argument("age", int, prompt_method="input", message="How old are you? ")
def greet(name: str, age: int):
    print(f"Hello {name}, you are {age} years old!")

if __name__ == "__main__":
    greet()