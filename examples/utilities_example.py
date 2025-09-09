#!/usr/bin/env python3
"""
Example demonstrating the utility functions for formatting commands.
These utilities provide convenient access to format, spin, style, and pager.
"""

from gumwrapper import (
    argument, 
    # Utility functions
    format_text, spin, style, pager,
    # Convenience functions  
    fmt, loading, box, success, error, warning, info, code, markdown
)


@argument("project_name", str, prompt_method="input", 
          prompt="Project name: ", placeholder="my-awesome-project")
@argument("use_spinner", bool, prompt_method="confirm", 
          message="Show spinner during setup?")
def create_project(project_name: str, use_spinner: bool):
    """Demonstrate utilities in a project creation workflow."""
    
    print(box(f"🚀 Creating Project: {project_name}", 
              foreground="cyan", border="double"))
    
    if use_spinner:
        print("\nRunning setup with spinner...")
        # Note: In real usage, this would run actual commands
        print("(Simulating spinner - would show: 'Setting up project...')")
        # loading("Setting up project...", "sleep 2")
    
    # Show different message types
    print(f"\n{success('✅ Project directory created')}")
    print(f"{info('ℹ️  Initializing git repository')}")
    print(f"{warning('⚠️  No package.json found')}")
    
    # Format some code
    sample_code = '''
def hello_world():
    """A simple hello world function."""
    print("Hello from your new project!")
    return True
'''
    
    print(f"\n{box('Generated starter code:', border='dashed')}")
    print(code(sample_code.strip(), language="python"))
    
    # Show project structure as markdown
    project_structure = f'''
# {project_name} Project Structure

## Files Created
- `README.md` - Project documentation
- `main.py` - Entry point
- `.gitignore` - Git ignore rules
- `requirements.txt` - Python dependencies

## Next Steps
1. Edit `main.py` to add your code
2. Install dependencies: `pip install -r requirements.txt`
3. Run your project: `python main.py`
'''
    
    print(f"\n{box('Project Structure:', border='thick', foreground='green')}")
    print(markdown(project_structure.strip(), theme="dark"))
    
    print(f"\n{success('🎉 Project created successfully!')}")


def demonstrate_styling_utilities():
    """Show different styling utility functions."""
    
    print(box("🎨 Styling Utilities Demo", foreground="purple", bold=True))
    
    # Different message types
    messages = [
        success("Operation completed successfully"),
        error("Something went wrong"),  
        warning("Please check your configuration"),
        info("New version available")
    ]
    
    print("\nMessage Types:")
    for msg in messages:
        print(f"  {msg}")
    
    # Different box styles
    print(f"\n{box('Default box style')}")
    print(f"{box('Thick border box', border='thick', foreground='green')}")
    print(f"{box('Custom styled box', border='double', background='blue', foreground='white', padding='1 2')}")
    
    # Using style() directly for more control
    fancy_box = style(
        "Fancy Custom Box",
        foreground="yellow",
        background="purple", 
        border="rounded",
        padding="2",
        width=30,
        align="center",
        bold=True
    )
    print(f"\n{fancy_box}")


def demonstrate_formatting_utilities():
    """Show formatting utility functions."""
    
    print(box("📝 Formatting Utilities Demo", foreground="blue", bold=True))
    
    # Format markdown
    markdown_text = '''
# API Documentation

## Authentication
Use **Bearer tokens** for authentication.

### Example Request
```bash
curl -H "Authorization: Bearer TOKEN" https://api.example.com/users
```

> **Note**: Tokens expire after 24 hours.
'''
    
    print("\nFormatted Markdown:")
    print(markdown(markdown_text.strip(), theme="pink"))
    
    # Format different code languages
    code_examples = [
        ("Python", "def greet(name):\n    return f'Hello, {name}!'"),
        ("JavaScript", "const greet = (name) => `Hello, ${name}!`;"),
        ("Go", "func greet(name string) string {\n    return fmt.Sprintf(\"Hello, %s!\", name)\n}")
    ]
    
    print(f"\n{box('Code Examples:', border='dashed')}")
    for language, code_text in code_examples:
        print(f"\n{language}:")
        print(code(code_text, language=language.lower()))


@argument("content_type", str, prompt_method="choose", 
          choices=["help text", "config file", "log output", "code snippet"])
def show_in_pager(content_type: str):
    """Demonstrate pager utility with different content types."""
    
    content_map = {
        "help text": """
HELP DOCUMENTATION
=================

COMMANDS:
  init     Initialize a new project
  build    Build the project
  test     Run tests
  deploy   Deploy to production
  
OPTIONS:
  -v, --verbose    Verbose output
  -h, --help       Show help
  --version        Show version
  
EXAMPLES:
  myapp init myproject
  myapp build --verbose
  myapp test
  myapp deploy production
  
For more information, visit: https://docs.example.com
""",
        "config file": """
# Application Configuration
app:
  name: "MyApplication" 
  version: "1.0.0"
  debug: true
  
server:
  host: "localhost"
  port: 8080
  
database:
  driver: "postgresql"
  host: "localhost"  
  port: 5432
  name: "myapp_db"
  
logging:
  level: "info"
  format: "json"
""",
        "log output": """
2024-01-15 10:30:00 INFO  Application starting...
2024-01-15 10:30:01 INFO  Database connection established
2024-01-15 10:30:01 INFO  Loading configuration from config.yaml
2024-01-15 10:30:02 INFO  Starting HTTP server on port 8080
2024-01-15 10:30:02 INFO  Application ready to serve requests
2024-01-15 10:30:15 INFO  GET /api/users 200 45ms
2024-01-15 10:30:22 WARN  Rate limit exceeded for IP 192.168.1.100
2024-01-15 10:30:30 INFO  POST /api/users 201 67ms
2024-01-15 10:30:45 ERROR Failed to connect to external service
2024-01-15 10:30:46 INFO  Retrying connection to external service
2024-01-15 10:30:47 INFO  External service connection restored
""",
        "code snippet": '''
"""
User authentication module.
Provides login, logout, and session management.
"""

import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Optional

class AuthManager:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.sessions = {}
    
    def hash_password(self, password: str) -> str:
        """Hash password with salt."""
        salt = secrets.token_hex(16)
        pwdhash = hashlib.pbkdf2_hmac('sha256',
                                      password.encode('utf-8'),
                                      salt.encode('utf-8'),
                                      100000)
        return salt + pwdhash.hex()
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """Verify password against stored hash."""
        salt = stored_hash[:32]
        stored_pwdhash = stored_hash[32:]
        pwdhash = hashlib.pbkdf2_hmac('sha256',
                                      password.encode('utf-8'),
                                      salt.encode('utf-8'), 
                                      100000)
        return pwdhash.hex() == stored_pwdhash
'''
    }
    
    selected_content = content_map.get(content_type, "No content available")
    
    print(box(f"📖 Displaying {content_type} in pager", foreground="green"))
    print("(Note: In real usage, this would open an interactive pager)")
    print("Here's what would be shown:")
    
    # Instead of actually opening pager (which would be interactive),
    # show the content with styling
    if content_type == "code snippet":
        print(code(selected_content.strip(), language="python"))
    else:
        print(box(selected_content.strip(), border="dashed", padding="1"))


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("🛠️  Utility Functions Examples")
        print("=" * 40)
        print("\nUtility functions provide convenient access to formatting:")
        print("• format_text, fmt - Format markdown/code") 
        print("• spin, loading - Show progress spinners")
        print("• style, box - Style text with colors/borders")
        print("• pager - Display content in scrollable view")
        print("• success, error, warning, info - Colored messages")
        print("• code, markdown - Format specific content types")
        print("\nAvailable examples:")
        print("  python utilities_example.py project")
        print("  python utilities_example.py styling")
        print("  python utilities_example.py formatting")
        print("  python utilities_example.py pager")
        
    elif "project" in sys.argv:
        print("Project creation with utilities...")
        create_project()
        
    elif "styling" in sys.argv:
        demonstrate_styling_utilities()
        
    elif "formatting" in sys.argv:
        demonstrate_formatting_utilities()
        
    elif "pager" in sys.argv:
        print("Pager utility demo...")
        show_in_pager()
        
    else:
        print("Unknown example. Run without arguments to see options.")