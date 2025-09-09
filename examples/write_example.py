#!/usr/bin/env python3
"""
Example demonstrating the 'write' command with decorator syntax.
This shows multi-line text input for various use cases.
"""

from gumwrapper import argument, command, GumWrapper


@argument("commit_message", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Enter your commit message...\n\nDescribe what changed and why."})
@argument("additional_notes", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Any additional notes or context?"})
@command("git_commit", description="Create a git commit with detailed message")
def create_git_commit(commit_message: str, additional_notes: str):
    """Example for multi-line git commit messages."""
    print("📝 Git Commit Preview:")
    
    # Format the commit message nicely
    formatted_message = GumWrapper.style(
        commit_message,
        foreground="cyan",
        border="rounded",
        padding="1"
    )
    print(formatted_message)
    
    if additional_notes.strip():
        notes_formatted = GumWrapper.style(
            f"Additional Notes:\n{additional_notes}",
            foreground="yellow",
            border="dashed",
            padding="1"
        )
        print(f"\n{notes_formatted}")
    
    # Simulate commit
    success = GumWrapper.style(
        "✅ Commit created successfully!",
        foreground="green",
        bold=True
    )
    print(f"\n{success}")


@argument("bug_description", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Describe the bug in detail...\n\nSteps to reproduce:\n1. \n2. \n3. \n\nExpected behavior:\n\n\nActual behavior:"})
@argument("environment_info", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Environment information:\n\nOS: \nBrowser: \nVersion: \nOther details:"})
@command("bug_report", description="Create a detailed bug report")
def create_bug_report(bug_description: str, environment_info: str):
    """Example for creating structured bug reports."""
    print("🐛 Bug Report Generated:")
    
    # Create a structured bug report layout
    sections = [
        ("Bug Description", bug_description, "red"),
        ("Environment Info", environment_info, "blue")
    ]
    
    for title, content, color in sections:
        section = GumWrapper.style(
            f"{title}:\n{content}",
            foreground=color,
            border="rounded",
            padding="1"
        )
        print(f"\n{section}")
    
    print(f"\n📋 Bug report ready to submit!")


@argument("code_snippet", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Paste your code here...\n\ndef example_function():\n    pass"})
@argument("documentation", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Write documentation for this code...\n\nThis function does:\n- \n- \n\nParameters:\n- \n\nReturns:\n- "})
@command("code_documenter", description="Document code snippets")
def document_code(code_snippet: str, documentation: str):
    """Example for documenting code with multi-line input."""
    print("📚 Code Documentation:")
    
    # Display code with syntax-like formatting
    code_display = GumWrapper.style(
        f"Code:\n{code_snippet}",
        foreground="green",
        border="thick",
        padding="1"
    )
    print(code_display)
    
    # Display documentation
    doc_display = GumWrapper.style(
        f"Documentation:\n{documentation}",
        foreground="cyan",
        border="rounded", 
        padding="1"
    )
    print(f"\n{doc_display}")
    
    # Create a combined output using join
    combined = GumWrapper.join(
        [
            GumWrapper.style("CODE", foreground="green", bold=True),
            code_snippet,
            "",
            GumWrapper.style("DOCUMENTATION", foreground="cyan", bold=True),
            documentation
        ],
        vertical=True,
        align="left"
    )
    
    final_output = GumWrapper.style(
        combined,
        border="double",
        padding="1 2"
    )
    
    print(f"\n📄 Final Documentation:")
    print(final_output)


@argument("meeting_notes", str, prompt_method="write",
          prompt_kwargs={"placeholder": "Meeting notes...\n\nDate: \nAttendees: \n\nAgenda:\n- \n- \n\nDiscussion:\n\n\nAction Items:\n- [ ] \n- [ ] \n\nNext Steps:"})
@command("meeting_logger", description="Log meeting notes and action items")
def log_meeting(meeting_notes: str):
    """Example for capturing meeting notes with structured format."""
    print("🤝 Meeting Notes Captured:")
    
    # Parse and highlight action items (simple example)
    lines = meeting_notes.split('\n')
    formatted_lines = []
    
    for line in lines:
        if line.strip().startswith('- [ ]'):
            # Highlight action items
            formatted_lines.append(GumWrapper.style(line, foreground="yellow", bold=True))
        elif line.strip().startswith('Date:') or line.strip().startswith('Attendees:'):
            # Highlight metadata
            formatted_lines.append(GumWrapper.style(line, foreground="cyan"))
        else:
            formatted_lines.append(line)
    
    formatted_notes = '\n'.join(formatted_lines)
    
    notes_display = GumWrapper.style(
        formatted_notes,
        border="rounded",
        padding="1 2"
    )
    
    print(notes_display)
    
    # Count action items
    action_count = len([line for line in lines if '- [ ]' in line])
    if action_count > 0:
        summary = GumWrapper.style(
            f"📋 {action_count} action item(s) identified",
            foreground="yellow",
            bold=True
        )
        print(f"\n{summary}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("Available examples:")
        print("  python write_example.py git_commit")
        print("  python write_example.py bug_report")
        print("  python write_example.py code_documenter")
        print("  python write_example.py meeting_logger")
    elif "git_commit" in sys.argv:
        create_git_commit()
    elif "bug_report" in sys.argv:
        create_bug_report()
    elif "code_documenter" in sys.argv:
        document_code()
    elif "meeting_logger" in sys.argv:
        log_meeting()