#!/usr/bin/env python3
"""
Example demonstrating the 'input' command with decorator syntax.
This shows various input configurations including prompts, placeholders, and validation.
"""

from gumwrapper import GumPrompt, argument, command


@argument(
    "name",
    str,
    prompt_method="input",
    prompt_kwargs={
        "prompt": "👤 What's your name? ",
        "placeholder": "Enter your full name",
    },
)
@argument(
    "email",
    str,
    prompt_method="input",
    prompt_kwargs={"prompt": "📧 Email address: ", "placeholder": "user@example.com"},
)
@argument(
    "age",
    int,
    prompt_method="input",
    prompt_kwargs={"prompt": "🎂 Your age: ", "placeholder": "25"},
)
@command("user_profile", description="Create user profile with various input types")
def create_user_profile(name: str, email: str, age: int):
    """Example collecting different types of user input."""
    print(f"\n📋 User Profile Created:")

    profile_data = [f"Name: {name}", f"Email: {email}", f"Age: {age} years old"]

    profile_box = GumPrompt.style(
        "\n".join(profile_data),
        foreground="212",
        border="rounded",
        padding="1 2",
        bold=True,
    )
    print(profile_box)

    # Validation example
    if age < 13:
        warning = GumPrompt.style(
            "⚠️  Note: Parental consent may be required for users under 13",
            foreground="yellow",
            italic=True,
        )
        print(f"\n{warning}")


@argument(
    "password",
    str,
    prompt_method="input",
    prompt_kwargs={"prompt": "🔐 Enter password: ", "password": True},
)
@argument(
    "confirm_password",
    str,
    prompt_method="input",
    prompt_kwargs={"prompt": "🔐 Confirm password: ", "password": True},
)
@command("secure_setup", description="Password setup with hidden input")
def setup_password(password: str, confirm_password: str):
    """Example demonstrating password input (hidden text)."""
    if password != confirm_password:
        error = GumPrompt.style(
            "❌ Passwords don't match!", foreground="red", bold=True
        )
        print(error)
        return

    success = GumPrompt.style(
        "✅ Password set successfully!",
        foreground="green",
        border="rounded",
        padding="1",
        bold=True,
    )
    print(success)

    # Show password strength (mock)
    strength = "Strong" if len(password) >= 8 else "Weak"
    strength_color = "green" if strength == "Strong" else "red"

    strength_msg = GumPrompt.style(
        f"Password strength: {strength}", foreground=strength_color
    )
    print(strength_msg)


@argument(
    "project_name",
    str,
    prompt_method="input",
    prompt_kwargs={"prompt": "📁 Project name: ", "placeholder": "my-awesome-project"},
)
@argument(
    "description",
    str,
    prompt_method="input",
    prompt_kwargs={
        "prompt": "📝 Description: ",
        "placeholder": "A brief description of your project",
    },
)
@argument(
    "version",
    str,
    prompt_method="input",
    prompt_kwargs={"prompt": "🏷️  Initial version: ", "value": "1.0.0"},
)
@argument(
    "author", str, prompt_method="input", prompt_kwargs={"prompt": "👨‍💻 Author: "}
)
@command("project_init", description="Initialize new project with metadata")
def initialize_project(project_name: str, description: str, version: str, author: str):
    """Example project initialization with default values and validation."""
    print(f"\n🚀 Initializing Project: {project_name}")

    # Create project metadata display
    metadata = [
        f"Project: {project_name}",
        f"Description: {description}",
        f"Version: {version}",
        f"Author: {author}",
    ]

    # Use join to create a nice layout
    metadata_display = GumPrompt.join(
        [GumPrompt.style(item, foreground="cyan") for item in metadata],
        vertical=True,
        align="left",
    )

    project_box = GumPrompt.style(metadata_display, border="double", padding="1 2")

    print(project_box)

    # Simulate project creation
    steps = [
        "Creating directory structure",
        "Initializing git repository",
        "Creating config files",
    ]
    for step in steps:
        print(f"   ✓ {step}")

    complete = GumPrompt.style(
        f"🎉 Project '{project_name}' created successfully!",
        foreground="green",
        bold=True,
    )
    print(f"\n{complete}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python input_example.py user_profile")
        print("  python input_example.py secure_setup")
        print("  python input_example.py project_init")
    elif "user_profile" in sys.argv:
        create_user_profile()
    elif "secure_setup" in sys.argv:
        setup_password()
    elif "project_init" in sys.argv:
        initialize_project()
