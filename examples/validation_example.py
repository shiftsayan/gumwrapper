#!/usr/bin/env python3
"""
Example demonstrating parameter validation in the new decorator system.
Shows how invalid parameters raise ValueError.
"""

from gumwrapper import argument, GumWrapper


# Valid examples
@argument("valid_choice", str, prompt_method="choose", 
          choices=["A", "B", "C"], limit=1, height=5)
def valid_choose_example(valid_choice: str):
    """Valid choose example with allowed parameters."""
    print(f"You chose: {valid_choice}")


@argument("valid_input", str, prompt_method="input",
          prompt="Enter text: ", placeholder="Type here", password=False)
def valid_input_example(valid_input: str):
    """Valid input example with allowed parameters."""
    print(f"You entered: {valid_input}")


@argument("valid_filter", str, prompt_method="filter",
          choices=["item1", "item2", "item3"], placeholder="Search...", limit=2)
def valid_filter_example(valid_filter: str):
    """Valid filter example with allowed parameters."""
    selected = [item.strip() for item in valid_filter.split('\n') if item.strip()]
    print(f"You selected: {', '.join(selected)}")


def demonstrate_invalid_examples():
    """Show examples that would raise ValueError due to invalid parameters."""
    
    print("❌ Examples that would fail with ValueError:")
    print()
    
    invalid_examples = [
        {
            "code": '''@argument("bad_choose", str, prompt_method="choose", 
          choices=["A", "B"], invalid_param="not_allowed")''',
            "error": "Invalid parameters for choose: {'invalid_param'}. Allowed parameters: {'limit', 'height'}"
        },
        {
            "code": '''@argument("bad_input", str, prompt_method="input", 
          prompt="Text: ", theme="dark")  # theme not allowed for input''',
            "error": "Invalid parameters for input: {'theme'}. Allowed parameters: {'prompt', 'placeholder', 'password'}"
        },
        {
            "code": '''@argument("bad_filter", str, prompt_method="filter",
          placeholder="Search...", theme="dark")  # theme not valid for filter''',
            "error": "Invalid parameters for filter: {'theme'}. Allowed parameters: {'placeholder', 'limit'}"
        },
        {
            "code": '''@argument("bad_file", str, prompt_method="file",
          path=".", border="rounded")  # border not valid for file''',
            "error": "Invalid parameters for file: {'border'}. Allowed parameters: {'path'}"
        }
    ]
    
    for i, example in enumerate(invalid_examples, 1):
        print(f"{i}. Invalid Code:")
        code_display = GumWrapper.style(
            example["code"],
            foreground="red",
            border="dashed",
            padding="1"
        )
        print(code_display)
        
        print(f"   Would raise: {example['error']}")
        print()


def show_valid_parameters():
    """Display the valid parameters for each prompt method."""
    
    valid_params = {
        "choose": ["limit", "height"],
        "confirm": ["message"], 
        "input": ["prompt", "placeholder", "password"],
        "write": ["placeholder"],
        "filter": ["placeholder", "limit"],
        "file": ["path"]
    }
    
    print("✅ Valid Parameters by Method:")
    print("=" * 40)
    
    for method, params in valid_params.items():
        if params:
            params_str = ", ".join(params)
        else:
            params_str = "None"
            
        method_display = GumWrapper.style(f"{method:>8}", foreground="cyan", bold=True)
        params_display = GumWrapper.style(params_str, foreground="green")
        
        print(f"{method_display}: {params_display}")
    
    print()
    print("💡 Note: Only INPUT commands are valid for @argument decorators")
    print("   Output commands like 'style', 'format', 'join' are used directly via GumWrapper")
    
    input_note = GumWrapper.style(
        "Valid prompt_methods: choose, confirm, input, write, filter, file",
        foreground="yellow",
        border="rounded", 
        padding="1"
    )
    print(input_note)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("🔍 Parameter Validation Examples")
        print("=" * 40)
        print("\nAvailable examples:")
        print("  python validation_example.py valid")
        print("  python validation_example.py invalid")
        print("  python validation_example.py params")
        print("  python validation_example.py test_choose")
        print("  python validation_example.py test_input") 
        print("  python validation_example.py test_filter")
        
    elif "valid" in sys.argv:
        show_valid_parameters()
        
    elif "invalid" in sys.argv:
        demonstrate_invalid_examples()
        
    elif "params" in sys.argv:
        show_valid_parameters()
        
    elif "test_choose" in sys.argv:
        print("Testing valid choose example...")
        valid_choose_example()
        
    elif "test_input" in sys.argv:
        print("Testing valid input example...")
        valid_input_example()
        
    elif "test_filter" in sys.argv:
        print("Testing valid filter example...")
        valid_filter_example()
        
    else:
        print("Unknown option. Run without arguments to see available examples.")