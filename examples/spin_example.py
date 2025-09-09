#!/usr/bin/env python3
"""
Example demonstrating the 'spin' command for showing spinners during long operations.
This shows various spinner styles and usage patterns.
"""

import time

from gumwrapper import GumPrompt


def demo_basic_spinner():
    """Demonstrate basic spinner functionality."""
    print("🔄 Basic Spinner Examples:\n")

    # Note: These examples show the concept, but actual spinning
    # would require real commands or processes to demonstrate

    print("Basic spinner with default style:")
    print("(In real usage, this would show a spinning animation)")
    print("GumWrapper.spin('Processing...', command='sleep 3')")
    print()

    print("The spin command is used to show progress during long-running operations.")
    print("Here are some practical examples of how you would use it:\n")


def demo_different_spinners():
    """Demonstrate different spinner styles."""
    print("🎨 Different Spinner Styles:\n")

    spinner_styles = [
        ("line", "Simple line spinner"),
        ("dot", "Dot-based spinner"),
        ("arc", "Arc-style spinner"),
        ("arrow", "Arrow spinner"),
        ("bounce", "Bouncing spinner"),
        ("pulse", "Pulsing spinner"),
    ]

    print("Available spinner styles:")
    for style, description in spinner_styles:
        print(f"  {style:>8}: {description}")
        print(
            f"           Usage: GumWrapper.spin('Loading...', spinner='{style}', command='your-command')"
        )
    print()


def demo_practical_examples():
    """Show practical usage examples."""
    print("💼 Practical Usage Examples:\n")

    examples = [
        {
            "title": "File Download",
            "description": "Show spinner while downloading a large file",
            "code": "GumWrapper.spin('Downloading file...', spinner='dot', command='curl -O https://example.com/largefile.zip')",
        },
        {
            "title": "Database Migration",
            "description": "Show progress during database operations",
            "code": "GumWrapper.spin('Running migrations...', spinner='line', command='python manage.py migrate')",
        },
        {
            "title": "Build Process",
            "description": "Display spinner during application build",
            "code": "GumWrapper.spin('Building application...', spinner='arc', command='npm run build')",
        },
        {
            "title": "Test Suite",
            "description": "Show progress while running tests",
            "code": "GumWrapper.spin('Running test suite...', spinner='arrow', command='pytest tests/ -v')",
        },
        {
            "title": "Docker Build",
            "description": "Display progress during container build",
            "code": "GumWrapper.spin('Building Docker image...', spinner='pulse', command='docker build -t myapp .')",
        },
    ]

    for example in examples:
        title_styled = GumPrompt.style(example["title"], foreground="cyan", bold=True)
        print(title_styled)
        print(f"Description: {example['description']}")

        code_styled = GumPrompt.style(
            example["code"], foreground="green", border="rounded", padding="1"
        )
        print(code_styled)
        print()


def demo_spinner_with_output():
    """Demonstrate spinner with command output."""
    print("📤 Spinner with Output Examples:\n")

    print("By default, spinners hide command output to keep the display clean.")
    print("However, you can show output using the show_output parameter:\n")

    output_examples = [
        {
            "scenario": "Silent operation (default)",
            "code": "GumWrapper.spin('Processing...', command='long-running-command')",
            "description": "Shows only the spinner, hides command output",
        },
        {
            "scenario": "With output visible",
            "code": "GumWrapper.spin('Processing...', command='long-running-command', show_output=True)",
            "description": "Shows spinner AND command output as it runs",
        },
    ]

    for example in output_examples:
        scenario_styled = GumPrompt.style(
            example["scenario"], foreground="yellow", bold=True
        )
        print(scenario_styled)
        print(f"Description: {example['description']}")

        code_styled = GumPrompt.style(
            example["code"], foreground="blue", border="dashed", padding="0 1"
        )
        print(code_styled)
        print()


def demo_real_world_workflows():
    """Show real-world workflow examples."""
    print("🌍 Real-World Workflow Examples:\n")

    workflows = [
        {
            "name": "Web Application Deployment",
            "steps": [
                ("Building assets", "npm run build", "dot"),
                ("Running tests", "npm test", "line"),
                ("Creating Docker image", "docker build -t webapp .", "arc"),
                ("Pushing to registry", "docker push registry/webapp:latest", "arrow"),
                (
                    "Deploying to production",
                    "kubectl apply -f deployment.yaml",
                    "pulse",
                ),
            ],
        },
        {
            "name": "Data Processing Pipeline",
            "steps": [
                (
                    "Downloading dataset",
                    "curl -O https://data.example.com/dataset.csv",
                    "bounce",
                ),
                ("Cleaning data", "python clean_data.py", "line"),
                ("Training model", "python train_model.py", "dot"),
                ("Validating results", "python validate.py", "arc"),
                ("Uploading artifacts", "aws s3 cp model.pkl s3://bucket/", "arrow"),
            ],
        },
    ]

    for workflow in workflows:
        workflow_title = GumPrompt.style(
            workflow["name"],
            foreground="purple",
            bold=True,
            border="thick",
            padding="0 1",
        )
        print(workflow_title)
        print()

        for i, (title, command, spinner) in enumerate(workflow["steps"], 1):
            step_info = [
                f"Step {i}: {title}",
                f"Command: {command}",
                f"Spinner: {spinner}",
            ]

            step_display = GumPrompt.join(step_info, vertical=True, align="left")
            step_box = GumPrompt.style(
                step_display, foreground="cyan", border="rounded", padding="1", width=60
            )
            print(step_box)

            # Show the actual gum command
            gum_cmd = f"GumWrapper.spin('{title}...', spinner='{spinner}', command='{command}')"
            cmd_styled = GumPrompt.style(
                f"Code: {gum_cmd}", foreground="green", italic=True
            )
            print(cmd_styled)
            print()

        print("=" * 60)
        print()


def demo_error_handling():
    """Show how to handle errors with spinners."""
    print("⚠️  Error Handling with Spinners:\n")

    print(
        "When using spinners with commands, it's important to handle failures gracefully:"
    )
    print()

    error_scenarios = [
        {
            "scenario": "Command fails",
            "description": "The spinner will stop and the command exit code indicates failure",
            "example": "If 'npm test' fails, the spinner stops and you can check the exit status",
        },
        {
            "scenario": "Long timeout",
            "description": "Commands that run too long might need timeouts or manual interruption",
            "example": "Use Ctrl+C to interrupt a spinner if the command hangs",
        },
        {
            "scenario": "Missing command",
            "description": "If the command doesn't exist, the spinner will stop immediately",
            "example": "Running 'nonexistent-command' will fail quickly",
        },
    ]

    for scenario in error_scenarios:
        scenario_title = GumPrompt.style(
            scenario["scenario"], foreground="red", bold=True
        )
        print(scenario_title)
        print(f"Description: {scenario['description']}")
        print(f"Example: {scenario['example']}")
        print()

    # Best practices
    best_practices = GumPrompt.style(
        """Best Practices for Spinner Usage:

• Use descriptive titles that explain what's happening
• Choose appropriate spinner styles for different operations
• Consider showing output for debugging (show_output=True)
• Test commands independently before adding spinners
• Use spinners for operations that take more than 1-2 seconds
• Provide users with ways to interrupt long operations""",
        foreground="blue",
        border="double",
        padding="1 2",
    )

    print(best_practices)


def demo_integration_patterns():
    """Show how to integrate spinners into applications."""
    print("\n🔗 Integration Patterns:\n")

    print("Here's how you might integrate spinners into a real CLI application:")
    print()

    integration_example = '''
# Example CLI application with spinners
def deploy_application():
    """Deploy application with progress indicators."""
    
    steps = [
        ("Preparing deployment", "prepare_deploy.sh", "line"),
        ("Building application", "npm run build", "dot"), 
        ("Running tests", "npm test", "arc"),
        ("Creating container", "docker build -t app .", "arrow"),
        ("Pushing to registry", "docker push registry/app", "bounce"),
        ("Deploying to cluster", "kubectl apply -f deploy.yaml", "pulse")
    ]
    
    print("🚀 Starting deployment process...")
    print()
    
    for step_name, command, spinner_type in steps:
        try:
            # This would actually run the spinner
            GumWrapper.spin(
                title=f"{step_name}...",
                command=command,
                spinner=spinner_type,
                show_output=False
            )
            print(f"✅ {step_name} completed")
            
        except Exception as e:
            print(f"❌ {step_name} failed: {e}")
            return False
    
    print("🎉 Deployment completed successfully!")
    return True
'''

    code_example = GumPrompt.style(
        integration_example, foreground="green", border="thick", padding="1"
    )

    print(code_example)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available spin examples:")
        print("  python spin_example.py basic")
        print("  python spin_example.py styles")
        print("  python spin_example.py practical")
        print("  python spin_example.py output")
        print("  python spin_example.py workflows")
        print("  python spin_example.py errors")
        print("  python spin_example.py integration")
        print("  python spin_example.py all")

    elif "basic" in sys.argv:
        demo_basic_spinner()
    elif "styles" in sys.argv:
        demo_different_spinners()
    elif "practical" in sys.argv:
        demo_practical_examples()
    elif "output" in sys.argv:
        demo_spinner_with_output()
    elif "workflows" in sys.argv:
        demo_real_world_workflows()
    elif "errors" in sys.argv:
        demo_error_handling()
    elif "integration" in sys.argv:
        demo_integration_patterns()
    elif "all" in sys.argv:
        demo_basic_spinner()
        demo_different_spinners()
        demo_practical_examples()
        demo_spinner_with_output()
        demo_real_world_workflows()
        demo_error_handling()
        demo_integration_patterns()
