#!/usr/bin/env python3
"""
Example usage of the enhanced GumWrapper with all available commands.
This script demonstrates how to use each gum command wrapper.
"""

from gumwrapper import GumWrapper, argument, command


def demo_basic_commands():
    """Demonstrate basic gum command usage."""
    print("=== Basic GumWrapper Commands Demo ===\n")
    
    # Input command
    print("1. Input command:")
    name = GumWrapper.input(prompt="Enter your name: ")
    print(f"Hello, {name}!\n")
    
    # Choose command
    print("2. Choose command:")
    choice = GumWrapper.choose(["Option 1", "Option 2", "Option 3"])
    print(f"You chose: {choice}\n")
    
    # Confirm command
    print("3. Confirm command:")
    confirmed = GumWrapper.confirm("Do you like this demo?")
    print(f"Confirmed: {confirmed}\n")
    
    # Filter command
    print("4. Filter command:")
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    filtered = GumWrapper.filter(items, placeholder="Select fruits...")
    print(f"You selected: {', '.join(filtered)}\n")
    
    # File picker command
    print("5. File picker command:")
    selected_file = GumWrapper.file(path=".", file_selection=True)
    print(f"Selected file: {selected_file}\n")


def demo_formatting_commands():
    """Demonstrate formatting and styling commands."""
    print("=== Formatting Commands Demo ===\n")
    
    # Style command
    print("1. Style command:")
    styled_text = GumWrapper.style(
        "This is styled text!",
        foreground="212",
        border="rounded",
        padding="1 2",
        bold=True
    )
    print(styled_text)
    
    # Format command
    print("\n2. Format command (markdown):")
    markdown = "# Hello World\n\nThis is **bold** text and *italic* text."
    formatted = GumWrapper.format(markdown, theme="pink")
    print(formatted)
    
    # Join command
    print("\n3. Join command:")
    texts = ["Line 1", "Line 2", "Line 3"]
    joined_vertical = GumWrapper.join(texts, vertical=True)
    print("Vertical join:")
    print(joined_vertical)
    
    joined_horizontal = GumWrapper.join(texts, horizontal=True, align="center")
    print("\nHorizontal join:")
    print(joined_horizontal)


def demo_data_commands():
    """Demonstrate data presentation commands."""
    print("=== Data Commands Demo ===\n")
    
    # Table command (static print)
    print("1. Table command:")
    # Note: For demo purposes, we'll create a simple CSV data
    csv_data = "Name,Age,City\nAlice,30,New York\nBob,25,Los Angeles\nCharlie,35,Chicago"
    
    # Write CSV data to a temporary file for table display
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(csv_data)
        temp_file = f.name
    
    try:
        table_output = GumWrapper.table(
            file_path=temp_file,
            separator=",",
            columns=["Name", "Age", "City"],
            print_static=True,
            border="rounded"
        )
        print(table_output)
    except Exception as e:
        print(f"Table demo skipped: {e}")
    finally:
        import os
        try:
            os.unlink(temp_file)
        except:
            pass
    
    # Log command
    print("\n2. Log command:")
    GumWrapper.log(
        ["Info: Application started", "Debug: Processing data", "Error: Something went wrong"],
        formatter="json",
        level="info",
        prefix="DEMO"
    )


@argument("name", str, prompt_method="input", prompt_kwargs={"prompt": "What's your name? "})
@argument("age", int, prompt_method="input", prompt_kwargs={"prompt": "What's your age? "})
@argument("favorite_color", str, prompt_method="choose", choices=["Red", "Green", "Blue", "Yellow"])
@argument("confirm_info", bool, prompt_method="confirm", prompt_kwargs={"message": "Is this information correct?"})
@command("demo_app", description="Demo application using gumwrapper decorators")
def demo_decorator_app(name: str, age: int, favorite_color: str, confirm_info: bool):
    """Example CLI app using the enhanced decorator system."""
    print(f"\n=== User Information ===")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Favorite Color: {favorite_color}")
    print(f"Information Confirmed: {confirm_info}")
    
    if confirm_info:
        # Use styling to make a nice output
        styled_message = GumWrapper.style(
            f"Welcome, {name}! You are {age} years old and love {favorite_color.lower()}!",
            foreground="212",
            border="rounded",
            padding="1 2",
            bold=True
        )
        print(f"\n{styled_message}")
    else:
        print("\nInformation not confirmed. Please run again.")


if __name__ == "__main__":
    try:
        # Uncomment the demos you want to run
        
        # Run basic commands demo
        # demo_basic_commands()
        
        # Run formatting commands demo
        # demo_formatting_commands()
        
        # Run data commands demo
        # demo_data_commands()
        
        # Run decorator demo (this will be run by default when script is executed with arguments)
        demo_decorator_app()
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
    except Exception as e:
        print(f"Demo error: {e}")