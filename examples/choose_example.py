#!/usr/bin/env python3
"""
Example demonstrating the 'choose' command with decorator syntax.
This shows how to create selection menus with various configurations.
"""

from gumwrapper import argument, command, GumWrapper


@argument("task", str, prompt_method="choose", 
          choices=["Start new project", "Review code", "Deploy to production", "Write documentation"],
          prompt_kwargs={"height": 6})
@argument("priority", str, prompt_method="choose",
          choices=["Low", "Medium", "High", "Critical"])
@command("task_selector", description="Select a task and priority level")
def select_task(task: str, priority: str):
    """Example CLI app for task selection."""
    print(f"\n📋 Task Selected: {task}")
    print(f"⚡ Priority Level: {priority}")
    
    # Use styling to make output more attractive
    result = GumWrapper.style(
        f"Task: {task}\nPriority: {priority}",
        foreground="212",
        border="rounded",
        padding="1 2",
        bold=True
    )
    print(f"\n{result}")


@argument("environment", str, prompt_method="choose",
          choices=["development", "staging", "production"],
          prompt_kwargs={"limit": 1})
@argument("services", str, prompt_method="choose", 
          choices=["api", "frontend", "database", "cache", "monitoring"],
          prompt_kwargs={"limit": 3})  # Allow multiple selections
@command("deploy_config", description="Configure deployment settings")
def configure_deployment(environment: str, services: str):
    """Example showing single vs multi-select choose options."""
    print(f"\n🚀 Deployment Configuration")
    print(f"Environment: {environment}")
    print(f"Services to deploy: {services}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python choose_example.py task_selector")
        print("  python choose_example.py deploy_config")
    elif "task_selector" in sys.argv:
        select_task()
    elif "deploy_config" in sys.argv:
        configure_deployment()