#!/usr/bin/env python3
import argparse
from gumwrapper.decorator import GUM_DATA_KEY

from gumwrapper import argument

@argument("name", str, prompt_method="input", message="What's your name? ")
def test_func(name: str):
    print(f"Hello {name}!")

# Debug the gum arguments
gum_arguments = getattr(test_func, GUM_DATA_KEY, [])
print(f"Found {len(gum_arguments)} gum arguments:")
for arg in gum_arguments:
    print(f"  argument_name: '{arg.argument_name}'")

# Debug CLI parsing
parser = argparse.ArgumentParser(add_help=False)
for gum_argument in gum_arguments:
    parser.add_argument(f"--{gum_argument.argument_name}", type=gum_argument.argument_type)

parsed_args, _ = parser.parse_known_args(["--name", "Alice"])
cli_args = {k: v for k, v in vars(parsed_args).items() if v is not None}
print(f"CLI args: {cli_args}")

for gum_argument in gum_arguments:
    print(f"Checking if '{gum_argument.argument_name}' in {list(cli_args.keys())}")
    print(f"Result: {gum_argument.argument_name in cli_args}")