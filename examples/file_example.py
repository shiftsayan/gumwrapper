#!/usr/bin/env python3
"""
Example demonstrating the 'file' command with decorator syntax.
This shows file and directory picking functionality.
"""

import os

from gumwrapper import GumPrompt, argument, command


@argument(
    "config_file",
    str,
    prompt_method="file",
    prompt_kwargs={"path": ".", "file_selection": True, "directory_selection": False},
)
@command("config_loader", description="Load configuration file")
def load_config_file(config_file: str):
    """Example for selecting a configuration file to load."""
    if not config_file:
        print("❌ No file selected")
        return

    print(f"📁 Selected Configuration File:")

    # Display file information
    file_info = [
        f"Path: {config_file}",
        f"Directory: {os.path.dirname(config_file)}",
        f"Filename: {os.path.basename(config_file)}",
        f"Exists: {'✅' if os.path.exists(config_file) else '❌'}",
    ]

    info_display = GumPrompt.join(file_info, vertical=True, align="left")
    file_box = GumPrompt.style(
        info_display, foreground="cyan", border="rounded", padding="1 2"
    )

    print(file_box)

    if os.path.exists(config_file):
        # Show file size if it exists
        size = os.path.getsize(config_file)
        size_msg = GumPrompt.style(f"📊 File size: {size} bytes", foreground="green")
        print(f"\n{size_msg}")

        print("✅ Configuration loaded successfully!")
    else:
        warning = GumPrompt.style(
            "⚠️  Selected file does not exist!", foreground="red", bold=True
        )
        print(f"\n{warning}")


@argument(
    "project_dir",
    str,
    prompt_method="file",
    prompt_kwargs={"path": ".", "file_selection": False, "directory_selection": True},
)
@argument(
    "create_structure",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "Create standard project structure?"},
)
@command("project_setup", description="Setup project in selected directory")
def setup_project_directory(project_dir: str, create_structure: bool):
    """Example for selecting a directory and setting up a project."""
    if not project_dir:
        print("❌ No directory selected")
        return

    print(f"📂 Selected Project Directory:")

    # Display directory information
    dir_info = [
        f"Path: {project_dir}",
        f"Absolute Path: {os.path.abspath(project_dir)}",
        f"Exists: {'✅' if os.path.exists(project_dir) else '❌'}",
        f"Is Directory: {'✅' if os.path.isdir(project_dir) else '❌'}",
    ]

    if os.path.exists(project_dir) and os.path.isdir(project_dir):
        # Count files in directory
        try:
            files = os.listdir(project_dir)
            dir_info.append(f"Contains: {len(files)} items")
        except PermissionError:
            dir_info.append("Contains: Permission denied")

    info_display = GumPrompt.join(dir_info, vertical=True, align="left")
    dir_box = GumPrompt.style(
        info_display, foreground="blue", border="rounded", padding="1 2"
    )

    print(dir_box)

    if create_structure:
        print(f"\n🏗️  Creating project structure in {project_dir}...")

        # Simulate creating project structure
        structure = [
            "src/",
            "tests/",
            "docs/",
            "README.md",
            "requirements.txt",
            ".gitignore",
        ]

        for item in structure:
            print(f"   ✓ Creating {item}")

        success = GumPrompt.style(
            "🎉 Project structure created successfully!",
            foreground="green",
            border="double",
            padding="1",
            bold=True,
        )
        print(f"\n{success}")


@argument(
    "backup_source",
    str,
    prompt_method="file",
    prompt_kwargs={"path": ".", "file_selection": False, "directory_selection": True},
)
@argument(
    "backup_dest",
    str,
    prompt_method="file",
    prompt_kwargs={"path": ".", "file_selection": False, "directory_selection": True},
)
@argument(
    "confirm_backup",
    bool,
    prompt_method="confirm",
    prompt_kwargs={"message": "Proceed with backup operation?"},
)
@command("backup_manager", description="Backup directory to another location")
def backup_directory(backup_source: str, backup_dest: str, confirm_backup: bool):
    """Example for selecting source and destination directories for backup."""
    if not backup_source or not backup_dest:
        print("❌ Both source and destination directories must be selected")
        return

    print("💾 Backup Configuration:")

    # Create backup info display
    backup_info = [
        f"Source: {backup_source}",
        f"Destination: {backup_dest}",
        f"Source exists: {'✅' if os.path.exists(backup_source) else '❌'}",
        f"Dest exists: {'✅' if os.path.exists(backup_dest) else '❌'}",
    ]

    # Add size information if directories exist
    if os.path.exists(backup_source) and os.path.isdir(backup_source):
        try:
            items = len(os.listdir(backup_source))
            backup_info.append(f"Source items: {items}")
        except PermissionError:
            backup_info.append("Source items: Permission denied")

    info_display = GumPrompt.join(backup_info, vertical=True, align="left")
    backup_box = GumPrompt.style(
        info_display, foreground="purple", border="thick", padding="1 2"
    )

    print(backup_box)

    if not confirm_backup:
        cancelled = GumPrompt.style(
            "❌ Backup cancelled by user", foreground="yellow", italic=True
        )
        print(f"\n{cancelled}")
        return

    if backup_source == backup_dest:
        error = GumPrompt.style(
            "⚠️  Source and destination cannot be the same!", foreground="red", bold=True
        )
        print(f"\n{error}")
        return

    print(f"\n📦 Starting backup process...")

    # Simulate backup steps
    steps = [
        "Scanning source directory",
        "Calculating backup size",
        "Creating destination structure",
        "Copying files",
        "Verifying backup integrity",
    ]

    for step in steps:
        print(f"   • {step}...")

    completion = GumPrompt.style(
        "✅ Backup completed successfully!",
        foreground="green",
        border="double",
        padding="1",
        bold=True,
    )
    print(f"\n{completion}")


@argument(
    "log_file",
    str,
    prompt_method="file",
    prompt_kwargs={"path": "/var/log", "file_selection": True},
)
@command("log_viewer", description="View system log files")
def view_log_file(log_file: str):
    """Example for selecting and viewing log files."""
    if not log_file:
        print("❌ No log file selected")
        return

    print(f"📄 Log File Analysis:")

    # Display file information
    file_details = [
        f"File: {os.path.basename(log_file)}",
        f"Full Path: {log_file}",
        f"Exists: {'✅' if os.path.exists(log_file) else '❌'}",
    ]

    if os.path.exists(log_file):
        try:
            size = os.path.getsize(log_file)
            file_details.extend(
                [
                    f"Size: {size:,} bytes",
                    f"Readable: {'✅' if os.access(log_file, os.R_OK) else '❌'}",
                ]
            )
        except (OSError, IOError):
            file_details.append("Size: Unable to determine")

    details_display = GumPrompt.join(file_details, vertical=True, align="left")
    file_box = GumPrompt.style(
        details_display, foreground="green", border="rounded", padding="1 2"
    )

    print(file_box)

    if os.path.exists(log_file) and os.access(log_file, os.R_OK):
        print(f"\n📖 Opening log file viewer...")

        # Simulate log viewing
        view_options = [
            "View recent entries",
            "Search for errors",
            "Filter by timestamp",
            "Export filtered logs",
        ]

        options_display = GumPrompt.join(
            [f"• {option}" for option in view_options], vertical=True
        )

        options_box = GumPrompt.style(
            f"Available options:\n{options_display}",
            foreground="cyan",
            border="dashed",
            padding="1",
        )

        print(options_box)
    else:
        error = GumPrompt.style(
            "❌ Cannot access selected log file", foreground="red", bold=True
        )
        print(f"\n{error}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python file_example.py config_loader")
        print("  python file_example.py project_setup")
        print("  python file_example.py backup_manager")
        print("  python file_example.py log_viewer")
    elif "config_loader" in sys.argv:
        load_config_file()
    elif "project_setup" in sys.argv:
        setup_project_directory()
    elif "backup_manager" in sys.argv:
        backup_directory()
    elif "log_viewer" in sys.argv:
        view_log_file()
