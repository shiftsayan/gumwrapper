#!/usr/bin/env python3
"""
Simple example demonstrating the new simplified decorator syntax.
No @command decorator needed, direct parameter usage instead of prompt_kwargs.
"""

from gumwrapper import argument, GumWrapper


@argument("name", str, prompt_method="input", 
          prompt="What's your name? ", placeholder="Enter your full name")
@argument("age", int, prompt_method="input", 
          prompt="How old are you? ", placeholder="25")
@argument("favorite_color", str, prompt_method="choose", 
          choices=["Red", "Green", "Blue", "Yellow", "Purple"])
@argument("confirm_info", bool, prompt_method="confirm", 
          message="Is this information correct?")
def create_profile(name: str, age: int, favorite_color: str, confirm_info: bool):
    """Simple profile creation example - no @command decorator needed!"""
    print(f"\n📋 User Profile:")
    
    if not confirm_info:
        print("❌ Profile creation cancelled")
        return
    
    profile_info = [
        f"Name: {name}",
        f"Age: {age} years old", 
        f"Favorite Color: {favorite_color}"
    ]
    
    profile_display = GumWrapper.join(profile_info, vertical=True, align="left")
    profile_box = GumWrapper.style(
        profile_display,
        foreground="cyan",
        border="rounded",
        padding="1 2",
        bold=True
    )
    print(profile_box)


@argument("packages", str, prompt_method="filter", 
          choices=["requests", "flask", "django", "fastapi", "pandas", "numpy"],
          placeholder="Search packages...", limit=3)
def install_packages(packages: str):
    """Package installer example."""
    selected = [p.strip() for p in packages.split('\n') if p.strip()]
    
    if not selected:
        print("❌ No packages selected")
        return
    
    print(f"📦 Installing {len(selected)} package(s):")
    for package in selected:
        print(f"   ✓ {package}")
    
    success = GumWrapper.style(
        "Installation completed!",
        foreground="green", 
        bold=True
    )
    print(f"\n{success}")


@argument("config_file", str, prompt_method="file", path=".")
@argument("load_backup", bool, prompt_method="confirm", 
          message="Load backup configuration?")
def load_config(config_file: str, load_backup: bool):
    """Configuration loader example."""
    print(f"📁 Loading config from: {config_file}")
    
    if load_backup:
        print("📦 Loading backup configuration...")
    
    result = GumWrapper.style(
        f"Configuration loaded: {config_file}",
        foreground="blue",
        border="dashed",
        padding="1"
    )
    print(result)


@argument("commit_message", str, prompt_method="write",
          placeholder="Enter commit message...\n\nDescribe your changes here.")
def git_commit(commit_message: str):
    """Git commit example with multi-line input."""
    print("📝 Commit Message:")
    
    message_display = GumWrapper.style(
        commit_message,
        foreground="green",
        border="thick",
        padding="1"
    )
    print(message_display)
    
    print("\n✅ Commit created successfully!")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("🚀 GumWrapper Simplified Examples")
        print("=" * 40)
        print("\nAvailable examples:")
        print("  python simple_example.py profile")
        print("  python simple_example.py packages")
        print("  python simple_example.py config")
        print("  python simple_example.py commit")
        print("\nNote: No @command decorator needed! Just call the functions directly.")
        
    elif "profile" in sys.argv:
        print("Creating user profile...")
        create_profile()
        
    elif "packages" in sys.argv:
        print("Package installer...")
        install_packages()
        
    elif "config" in sys.argv:
        print("Configuration loader...")
        load_config()
        
    elif "commit" in sys.argv:
        print("Git commit...")
        git_commit()
        
    else:
        print("Unknown example. Run without arguments to see options.")