# GumWrapper Examples

This directory contains comprehensive examples demonstrating all features of the GumWrapper library with decorator syntax. Each example shows practical usage patterns and real-world scenarios.

## 📁 Example Files

### Input Commands
- **[choose_example.py](choose_example.py)** - Selection menus with single/multi-select options
- **[confirm_example.py](confirm_example.py)** - Yes/no confirmation dialogs
- **[input_example.py](input_example.py)** - Text input with prompts, placeholders, and validation
- **[write_example.py](write_example.py)** - Multi-line text input for longer content
- **[filter_example.py](filter_example.py)** - Searchable/filterable lists
- **[file_example.py](file_example.py)** - File and directory picker dialogs

### Output & Formatting Commands  
- **[style_example.py](style_example.py)** - Text styling, colors, borders, and layouts
- **[format_example.py](format_example.py)** - Markdown and code syntax highlighting
- **[join_example.py](join_example.py)** - Combining text elements horizontally/vertically
- **[table_example.py](table_example.py)** - Tabular data display with CSV files
- **[log_example.py](log_example.py)** - Structured logging with different formatters

### Utility Commands
- **[spin_example.py](spin_example.py)** - Progress spinners for long-running operations

## 🚀 Running the Examples

Each example file can be run independently with different sub-commands to demonstrate various features:

```bash
# Show available sub-examples
python examples/choose_example.py

# Run specific example
python examples/choose_example.py task_selector

# Run all examples in a file
python examples/style_example.py all
```

## 📚 Example Categories

### Basic Usage Patterns
- Simple input collection
- Data validation
- User confirmations
- File/directory selection

### Advanced Layouts
- Dashboard creation
- Navigation menus
- Card-based layouts
- Table-like structures

### Real-World Scenarios
- CLI application setup
- Deployment workflows
- System monitoring
- Project management
- Security logging

### Styling & Theming
- Color schemes
- Border styles
- Text formatting
- Layout alignment
- Progress indicators

## 💡 Key Features Demonstrated

### Decorator Syntax
All examples use the enhanced decorator system:
```python
@argument("name", str, prompt_method="input", 
          prompt_kwargs={"prompt": "Enter name: "})
@command("myapp", description="My application")
def my_function(name: str):
    # Application logic here
    pass
```

### Prompt Customization
- **choices**: Predefined options for choose/filter
- **prompt_kwargs**: Custom prompts, placeholders, and settings
- **validation**: Type conversion and validation

### Styling Integration
All examples show integration between input collection and styled output:
```python
result = GumWriter.style(
    f"Hello {name}!",
    foreground="green",
    border="rounded",
    padding="1"
)
```

## 🎯 Use Cases by Domain

### **Development Tools**
- Package managers (`filter_example.py` - package installer)
- Build systems (`spin_example.py` - build workflows) 
- Project setup (`input_example.py` - project initialization)

### **System Administration**
- Service management (`filter_example.py` - service manager)
- System monitoring (`table_example.py` - monitoring dashboard)
- File operations (`file_example.py` - backup manager)

### **Business Applications**
- User management (`table_example.py` - user tables)
- Financial reporting (`table_example.py` - financial summaries)
- Project tracking (`table_example.py` - task management)

### **Security & Compliance**
- Audit logging (`log_example.py` - security logs)
- Access control (`confirm_example.py` - permission dialogs)
- Configuration management (`file_example.py` - config loaders)

## 🔧 Running Requirements

Most examples work without external dependencies, but some advanced features require:
- `gum` CLI tool installed on your system
- Python 3.12+ for type annotations
- Write permissions for temporary files (table/log examples)

## 📖 Learning Path

**Beginners**: Start with `input_example.py`, `choose_example.py`, and `confirm_example.py`

**Intermediate**: Explore `style_example.py`, `join_example.py`, and `filter_example.py` 

**Advanced**: Study `table_example.py`, `log_example.py`, and complex layouts in `join_example.py`

**Integration**: Review `spin_example.py` for workflow patterns and `format_example.py` for documentation

## 🤝 Contributing

When adding new examples:
1. Follow the existing file naming pattern: `{command}_example.py`
2. Include multiple sub-examples showing different use cases
3. Provide both basic and advanced scenarios
4. Add comprehensive docstrings and comments
5. Update this README with your new example

## 📝 Notes

- Examples prioritize demonstration over production-ready error handling
- Some examples create temporary files that are automatically cleaned up
- File paths are relative to the examples directory
- All examples include fallback displays for when `gum` is not available