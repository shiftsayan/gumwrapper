# Gum Wrapper

A Python wrapper for the [gum](https://github.com/charmbracelet/gum) command-line tool that provides beautiful terminal UI components.

## Features

This wrapper provides Python interfaces for all gum commands:

### Input Commands
- `choose` - Choose from a list of options  
- `confirm` - Ask for confirmation
- `input` - Get text input
- `write` - Get multi-line text input
- `filter` - Filter through a list of items
- `file` - File/directory picker

### Output/Formatting Commands  
- `style` - Apply colors, borders, and formatting to text
- `format` - Format text using templates (markdown, code, etc.)
- `join` - Join text vertically or horizontally
- `pager` - Scroll through content
- `table` - Display tabular data
- `log` - Log messages with formatting
- `spin` - Show a spinner while running commands

### Decorator System

The wrapper includes a decorator system for creating CLI applications:

```python
from gumwrapper import argument, command, GumWrapper

@argument("name", str, prompt_method="input", prompt_kwargs={"prompt": "Enter name: "})
@argument("color", str, prompt_method="choose", choices=["red", "green", "blue"])  
@command("myapp", description="My CLI app")
def my_app(name: str, color: str):
    styled = GumWrapper.style(f"Hello {name}!", foreground=color, bold=True)
    print(styled)
```

## Installation

```bash
# First install gum (required dependency)
# macOS
brew install gum

# Or see https://github.com/charmbracelet/gum for other platforms

# Then install this package
pip install -e .
```

## Usage Examples

See `example_usage.py` for comprehensive examples of all features.
