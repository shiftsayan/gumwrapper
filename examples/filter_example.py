#!/usr/bin/env python3
"""
Example demonstrating the 'filter' command with decorator syntax.
This shows how to create searchable/filterable lists.
"""

from gumwrapper import GumPrompt, argument, command


@argument(
    "packages",
    str,
    prompt_method="filter",
    choices=[
        "requests",
        "flask",
        "django",
        "fastapi",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "jupyter",
        "black",
        "pytest",
        "mypy",
    ],
    prompt_kwargs={"placeholder": "Search for Python packages...", "limit": 5},
)
@command("package_installer", description="Select and install Python packages")
def install_packages(packages: str):
    """Example for filtering and selecting Python packages to install."""
    selected_packages = packages.split("\n") if packages else []

    if not selected_packages:
        print("❌ No packages selected")
        return

    print("📦 Selected Packages:")
    for package in selected_packages:
        if package.strip():
            print(f"   • {package}")

    # Simulate installation
    print(f"\n🚀 Installing {len(selected_packages)} package(s)...")

    for package in selected_packages:
        if package.strip():
            print(f"   ✓ Installing {package}...")

    success = GumPrompt.style(
        f"✅ Successfully installed {len(selected_packages)} packages!",
        foreground="green",
        border="rounded",
        padding="1",
        bold=True,
    )
    print(f"\n{success}")


@argument(
    "services",
    str,
    prompt_method="filter",
    choices=[
        "nginx",
        "apache2",
        "mysql",
        "postgresql",
        "redis",
        "mongodb",
        "docker",
        "kubernetes",
        "jenkins",
        "gitlab-runner",
        "prometheus",
        "grafana",
        "elasticsearch",
        "kibana",
        "rabbitmq",
        "kafka",
    ],
    prompt_kwargs={"placeholder": "Filter services to manage...", "limit": 10},
)
@argument(
    "action",
    str,
    prompt_method="choose",
    choices=["start", "stop", "restart", "status"],
    prompt_kwargs={},
)
@command("service_manager", description="Manage system services")
def manage_services(services: str, action: str):
    """Example for filtering services and performing actions on them."""
    selected_services = [s.strip() for s in services.split("\n") if s.strip()]

    if not selected_services:
        print("❌ No services selected")
        return

    print(f"⚙️  {action.title()}ing Services:")

    # Display selected services
    services_list = GumPrompt.join(
        [f"• {service}" for service in selected_services], vertical=True
    )

    services_box = GumPrompt.style(
        services_list, foreground="cyan", border="rounded", padding="1"
    )
    print(services_box)

    # Simulate service management
    print(f"\n🔧 Executing '{action}' on selected services...")

    for service in selected_services:
        status_emoji = (
            "✅" if action in ["start", "restart"] else "⏹️" if action == "stop" else "ℹ️"
        )
        print(f"   {status_emoji} {service}: {action} completed")

    summary = GumPrompt.style(
        f"Operation '{action}' completed on {len(selected_services)} service(s)",
        foreground="green",
        bold=True,
    )
    print(f"\n{summary}")


@argument(
    "files",
    str,
    prompt_method="filter",
    choices=[
        "README.md",
        "LICENSE",
        "setup.py",
        "requirements.txt",
        "Dockerfile",
        "docker-compose.yml",
        ".gitignore",
        ".env.example",
        "config.yaml",
        "main.py",
        "app.py",
        "models.py",
        "views.py",
        "tests.py",
        "package.json",
        "webpack.config.js",
        "tsconfig.json",
        "index.html",
        "style.css",
        "script.js",
        "Makefile",
        "pyproject.toml",
    ],
    prompt_kwargs={"placeholder": "Search for files to edit...", "limit": 3},
)
@command("file_editor", description="Select files to edit")
def edit_files(files: str):
    """Example for filtering and selecting files to edit."""
    selected_files = [f.strip() for f in files.split("\n") if f.strip()]

    if not selected_files:
        print("❌ No files selected")
        return

    print("📝 Selected Files for Editing:")

    # Create a styled list of files with different colors based on type
    file_displays = []
    for file in selected_files:
        if file.endswith((".py", ".js", ".ts")):
            color = "green"
        elif file.endswith((".md", ".txt", ".rst")):
            color = "blue"
        elif file.endswith((".json", ".yaml", ".yml", ".toml")):
            color = "yellow"
        else:
            color = "white"

        file_displays.append(GumPrompt.style(f"📄 {file}", foreground=color))

    files_display = GumPrompt.join(file_displays, vertical=True)
    files_box = GumPrompt.style(files_display, border="rounded", padding="1")

    print(files_box)

    # Simulate opening files
    print(f"\n🚀 Opening {len(selected_files)} file(s) in editor...")

    success = GumPrompt.style(
        "Editor launched successfully!",
        foreground="green",
        border="dashed",
        padding="1",
    )
    print(f"\n{success}")


@argument(
    "contributors",
    str,
    prompt_method="filter",
    choices=[
        "alice@example.com",
        "bob@example.com",
        "charlie@dev.org",
        "diana@company.com",
        "eve@startup.io",
        "frank@tech.co",
        "grace@innovate.net",
        "henry@code.dev",
        "iris@build.com",
        "jack@deploy.org",
        "kate@scale.io",
        "liam@growth.co",
    ],
    prompt_kwargs={"placeholder": "Filter team members...", "limit": 6},
)
@command("team_notifier", description="Notify team members about updates")
def notify_team(contributors: str):
    """Example for filtering team members for notifications."""
    selected_members = [m.strip() for m in contributors.split("\n") if m.strip()]

    if not selected_members:
        print("❌ No team members selected")
        return

    print("📧 Notification Recipients:")

    # Create an elegant member list
    member_list = []
    for i, member in enumerate(selected_members, 1):
        member_line = f"{i:2d}. {member}"
        member_list.append(member_line)

    members_display = GumPrompt.join(member_list, vertical=True, align="left")
    members_box = GumPrompt.style(
        members_display, foreground="cyan", border="thick", padding="1 2"
    )

    print(members_box)

    # Simulate sending notifications
    print(f"\n📬 Sending notifications to {len(selected_members)} team member(s)...")

    for member in selected_members:
        print(f"   ✉️  Notification sent to {member}")

    completion = GumPrompt.style(
        "📮 All notifications sent successfully!",
        foreground="green",
        border="double",
        padding="1",
        bold=True,
    )
    print(f"\n{completion}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python filter_example.py package_installer")
        print("  python filter_example.py service_manager")
        print("  python filter_example.py file_editor")
        print("  python filter_example.py team_notifier")
    elif "package_installer" in sys.argv:
        install_packages()
    elif "service_manager" in sys.argv:
        manage_services()
    elif "file_editor" in sys.argv:
        edit_files()
    elif "team_notifier" in sys.argv:
        notify_team()
