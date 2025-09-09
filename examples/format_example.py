#!/usr/bin/env python3
"""
Example demonstrating the 'format' command for rendering markdown and code.
This shows various formatting capabilities for different content types.
"""

from gumwrapper import GumWrapper


def demo_markdown_formatting():
    """Demonstrate markdown formatting with different themes."""
    print("📝 Markdown Formatting Examples:\n")
    
    markdown_content = """# Project Documentation

## Overview
This is a **sample project** with *various features*.

### Features
- Easy to use
- Well documented  
- `Highly configurable`
- Written in Python

### Code Example
```python
def hello_world():
    print("Hello, World!")
    return True
```

> **Note:** This is just an example to demonstrate markdown formatting.

## Installation
1. Clone the repository
2. Install dependencies
3. Run the application

---

For more information, visit our [website](https://example.com)."""
    
    # Different themes
    themes = ["dark", "light", "pink", "notty", "auto"]
    
    for theme in themes:
        print(f"Theme: {theme}")
        print("-" * 40)
        
        try:
            formatted = GumWrapper.format(
                markdown_content,
                theme=theme,
                format_type="markdown"
            )
            print(formatted)
        except Exception as e:
            print(f"Error with theme {theme}: {e}")
        
        print("\n" + "="*50 + "\n")


def demo_code_formatting():
    """Demonstrate code formatting with syntax highlighting."""
    print("💻 Code Formatting Examples:\n")
    
    # Python code example
    python_code = '''def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence

# Example usage
if __name__ == "__main__":
    result = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {result}")'''
    
    print("Python Code with syntax highlighting:")
    print("-" * 40)
    
    formatted_python = GumWrapper.format(
        python_code,
        language="python",
        theme="dark",
        format_type="code"
    )
    print(formatted_python)
    print()
    
    # JavaScript code example
    js_code = '''function createUser(name, email) {
    return {
        id: Math.random().toString(36).substr(2, 9),
        name: name,
        email: email,
        createdAt: new Date(),
        isActive: true,
        
        getInfo() {
            return `${this.name} (${this.email})`;
        },
        
        activate() {
            this.isActive = true;
            console.log(`User ${this.name} activated`);
        }
    };
}

// Usage
const user = createUser("John Doe", "john@example.com");
console.log(user.getInfo());'''
    
    print("JavaScript Code with syntax highlighting:")
    print("-" * 45)
    
    formatted_js = GumWrapper.format(
        js_code,
        language="javascript",
        theme="pink",
        format_type="code"
    )
    print(formatted_js)
    print()


def demo_json_formatting():
    """Demonstrate JSON formatting."""
    print("📋 JSON Formatting Example:\n")
    
    json_content = '''{
    "name": "Sample API Response",
    "version": "1.0.0",
    "data": {
        "users": [
            {
                "id": 1,
                "username": "johndoe",
                "email": "john@example.com",
                "profile": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "age": 30,
                    "preferences": {
                        "theme": "dark",
                        "notifications": true,
                        "language": "en"
                    }
                }
            },
            {
                "id": 2, 
                "username": "janedoe",
                "email": "jane@example.com",
                "profile": {
                    "firstName": "Jane",
                    "lastName": "Doe",
                    "age": 28,
                    "preferences": {
                        "theme": "light",
                        "notifications": false,
                        "language": "es"
                    }
                }
            }
        ],
        "pagination": {
            "page": 1,
            "limit": 10,
            "total": 2,
            "hasNext": false
        }
    },
    "meta": {
        "timestamp": "2024-01-15T10:30:00Z",
        "apiVersion": "v2",
        "responseTime": "45ms"
    }
}'''
    
    formatted_json = GumWrapper.format(
        json_content,
        language="json",
        theme="auto",
        format_type="code"
    )
    print(formatted_json)
    print()


def demo_yaml_formatting():
    """Demonstrate YAML formatting."""
    print("⚙️  YAML Configuration Formatting:\n")
    
    yaml_content = '''# Application Configuration
app:
  name: "My Application"
  version: "2.1.0"
  debug: true
  
server:
  host: "0.0.0.0"
  port: 8080
  ssl:
    enabled: false
    certificate: "/path/to/cert.pem"
    key: "/path/to/key.pem"

database:
  driver: "postgresql"
  host: "localhost"
  port: 5432
  name: "myapp_db"
  username: "dbuser"
  password: "${DB_PASSWORD}"
  pool:
    min_connections: 5
    max_connections: 20

logging:
  level: "info"
  handlers:
    - type: "console"
      format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    - type: "file"
      filename: "app.log"
      max_size: "10MB"
      backup_count: 5

features:
  authentication: true
  rate_limiting: true
  caching: false
  metrics: true
  
external_apis:
  weather:
    base_url: "https://api.weather.com"
    api_key: "${WEATHER_API_KEY}"
    timeout: 30
  payment:
    base_url: "https://api.stripe.com"
    api_key: "${STRIPE_API_KEY}"
    webhook_secret: "${STRIPE_WEBHOOK_SECRET}"'''
    
    formatted_yaml = GumWrapper.format(
        yaml_content,
        language="yaml", 
        theme="light",
        format_type="code"
    )
    print(formatted_yaml)
    print()


def demo_documentation_formatting():
    """Demonstrate formatting for documentation and help text."""
    print("📚 Documentation Formatting:\n")
    
    help_doc = """# CLI Tool Help Documentation

## SYNOPSIS
    mytool [OPTIONS] COMMAND [ARGS]...

## DESCRIPTION
    A powerful CLI tool for managing projects and deployments.
    
    This tool provides a comprehensive set of commands for:
    - **Project Management**: Create, configure, and maintain projects
    - **Deployment**: Deploy to various environments with confidence  
    - **Monitoring**: Track application health and performance
    - **Configuration**: Manage settings and environment variables

## COMMANDS

### Project Commands
- `init`     - Initialize a new project
- `build`    - Build the project artifacts
- `test`     - Run project tests
- `clean`    - Clean build artifacts

### Deployment Commands  
- `deploy`   - Deploy to target environment
- `rollback` - Rollback to previous version
- `status`   - Check deployment status

### Configuration Commands
- `config set KEY VALUE` - Set configuration value
- `config get KEY`       - Get configuration value  
- `config list`          - List all configuration

## OPTIONS
    -v, --verbose    Enable verbose output
    -q, --quiet      Suppress output
    -h, --help       Show help message
    --version        Show version information

## EXAMPLES

Initialize a new project:
```bash
mytool init myproject --template python
```

Deploy to staging:
```bash  
mytool deploy staging --confirm
```

Check deployment status:
```bash
mytool status --environment production
```

## ENVIRONMENT VARIABLES
- `MYTOOL_CONFIG_PATH` - Path to configuration file
- `MYTOOL_LOG_LEVEL`   - Logging level (debug, info, warn, error)
- `MYTOOL_API_TOKEN`   - API authentication token

---
*For more detailed information, visit our documentation site.*"""
    
    themes = ["dark", "pink"]
    for theme in themes:
        print(f"Documentation theme: {theme}")
        print("-" * 40)
        
        formatted_help = GumWrapper.format(
            help_doc,
            theme=theme,
            format_type="markdown"
        )
        print(formatted_help)
        print("\n" + "="*60 + "\n")


def demo_mixed_content():
    """Demonstrate formatting mixed content types."""
    print("🔀 Mixed Content Formatting:\n")
    
    # API documentation with code examples
    api_doc = """# User API Documentation

## Create User Endpoint

**POST** `/api/users`

Creates a new user in the system.

### Request Body
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123",
  "profile": {
    "firstName": "John",
    "lastName": "Doe"
  }
}
```

### Response
```json
{
  "success": true,
  "data": {
    "id": 12345,
    "username": "johndoe", 
    "email": "john@example.com",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

### Python Example
```python
import requests

url = "https://api.example.com/api/users"
payload = {
    "username": "johndoe",
    "email": "john@example.com", 
    "password": "securepassword123"
}

response = requests.post(url, json=payload)
if response.status_code == 201:
    user_data = response.json()
    print(f"User created: {user_data['data']['username']}")
```

### cURL Example
```bash
curl -X POST https://api.example.com/api/users \\
  -H "Content-Type: application/json" \\
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

> **Note**: Make sure to use HTTPS in production and implement proper password security."""
    
    formatted_api_doc = GumWrapper.format(
        api_doc,
        theme="auto",
        format_type="markdown"
    )
    print(formatted_api_doc)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("Available format examples:")
        print("  python format_example.py markdown")
        print("  python format_example.py code")
        print("  python format_example.py json")
        print("  python format_example.py yaml")
        print("  python format_example.py docs")
        print("  python format_example.py mixed")
        print("  python format_example.py all")
        
    elif "markdown" in sys.argv:
        demo_markdown_formatting()
    elif "code" in sys.argv:
        demo_code_formatting()
    elif "json" in sys.argv:
        demo_json_formatting()
    elif "yaml" in sys.argv:
        demo_yaml_formatting()
    elif "docs" in sys.argv:
        demo_documentation_formatting()
    elif "mixed" in sys.argv:
        demo_mixed_content()
    elif "all" in sys.argv:
        demo_markdown_formatting()
        demo_code_formatting()
        demo_json_formatting()
        demo_yaml_formatting()
        demo_documentation_formatting()
        demo_mixed_content()