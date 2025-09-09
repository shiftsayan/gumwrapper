#!/usr/bin/env python3
"""
Example demonstrating the 'confirm' command with decorator syntax.
This shows how to create confirmation dialogs with various messages.
"""

from gumwrapper import GumPrompt, argument, command


@argument(
    "delete_confirm",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "⚠️  Are you sure you want to delete all files?"},
)
@argument(
    "backup_confirm",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "📦 Create backup before proceeding?"},
)
@command("delete_files", description="Dangerous file deletion with confirmations")
def delete_files_with_confirmation(delete_confirm: bool, backup_confirm: bool):
    """Example showing multiple confirmation steps for dangerous operations."""
    if not delete_confirm:
        print("❌ Operation cancelled by user")
        return

    if backup_confirm:
        print("📦 Creating backup...")
        # Simulate backup process
        result = GumPrompt.style(
            "Backup completed successfully!", foreground="green", bold=True
        )
        print(result)

    print("🗑️  Deleting files...")
    success_msg = GumPrompt.style(
        "Files deleted successfully!",
        foreground="red",
        border="rounded",
        padding="1",
        bold=True,
    )
    print(success_msg)


@argument(
    "agree_terms",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "Do you agree to the terms and conditions?"},
)
@argument(
    "newsletter",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "Subscribe to our newsletter?"},
)
@argument(
    "analytics",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "Allow anonymous analytics data collection?"},
)
@command(
    "setup_wizard", description="Application setup wizard with multiple confirmations"
)
def setup_wizard(agree_terms: bool, newsletter: bool, analytics: bool):
    """Example setup wizard with multiple boolean confirmations."""
    print("\n🛠️  Setup Configuration:")

    if not agree_terms:
        error_msg = GumPrompt.style(
            "❌ Cannot proceed without agreeing to terms!", foreground="red", bold=True
        )
        print(error_msg)
        return

    config = {
        "Terms Accepted": "✅" if agree_terms else "❌",
        "Newsletter": "✅" if newsletter else "❌",
        "Analytics": "✅" if analytics else "❌",
    }

    for setting, status in config.items():
        print(f"{setting}: {status}")

    summary = GumPrompt.style(
        "Setup completed successfully!",
        foreground="green",
        border="rounded",
        padding="1",
        bold=True,
    )
    print(f"\n{summary}")


@argument(
    "proceed",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "🚀 Deploy to production environment?"},
)
@command("deploy", description="Production deployment with confirmation")
def deploy_to_production(proceed: bool):
    """Simple deployment confirmation example."""
    if proceed:
        print("🚀 Deploying to production...")

        # Simulate deployment steps
        steps = [
            "Building application",
            "Running tests",
            "Uploading assets",
            "Updating servers",
        ]
        for step in steps:
            print(f"   • {step}...")

        success = GumPrompt.style(
            "🎉 Deployment successful!",
            foreground="green",
            border="double",
            padding="1 2",
            bold=True,
        )
        print(f"\n{success}")
    else:
        cancelled = GumPrompt.style(
            "Deployment cancelled", foreground="yellow", italic=True
        )
        print(cancelled)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python confirm_example.py delete_files")
        print("  python confirm_example.py setup_wizard")
        print("  python confirm_example.py deploy")
    elif "delete_files" in sys.argv:
        delete_files_with_confirmation()
    elif "setup_wizard" in sys.argv:
        setup_wizard()
    elif "deploy" in sys.argv:
        deploy_to_production()
