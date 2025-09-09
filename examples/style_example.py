#!/usr/bin/env python3
"""
Example demonstrating the 'style' command with various formatting options.
This shows how to create beautifully styled terminal output.
"""

from gumwrapper import GumWrapper


def demo_basic_styling():
    """Demonstrate basic styling options like colors and text formatting."""
    print("🎨 Basic Styling Examples:\n")
    
    # Basic colors
    print("Colors:")
    colors = ["red", "green", "blue", "yellow", "purple", "cyan"]
    for color in colors:
        styled = GumWrapper.style(f"This text is {color}", foreground=color)
        print(f"  {styled}")
    
    print("\nText Formatting:")
    # Text formatting options
    formats = [
        ("Bold text", {"bold": True}),
        ("Italic text", {"italic": True}),
        ("Underlined text", {"underline": True}),
        ("Faint text", {"faint": True}),
        ("Strikethrough text", {"strikethrough": True})
    ]
    
    for text, kwargs in formats:
        styled = GumWrapper.style(text, **kwargs)
        print(f"  {styled}")


def demo_borders_and_padding():
    """Demonstrate different border styles and padding options."""
    print("\n📦 Borders and Padding Examples:\n")
    
    # Different border styles
    border_styles = ["rounded", "thick", "double", "dashed", "none"]
    
    for border in border_styles:
        content = f"Border style: {border}"
        styled = GumWrapper.style(
            content,
            border=border,
            padding="1",
            foreground="cyan"
        )
        print(styled)
        print()  # Add spacing
    
    # Different padding examples
    print("Padding variations:")
    padding_examples = [
        ("No padding", "0"),
        ("Small padding", "1"),
        ("Large padding", "2"),
        ("Horizontal padding", "0 3"),
        ("Vertical padding", "2 0"),
        ("Custom padding", "1 2 1 3")
    ]
    
    for desc, padding in padding_examples:
        styled = GumWrapper.style(
            desc,
            border="rounded",
            padding=padding,
            foreground="green"
        )
        print(styled)
        print()


def demo_layout_and_sizing():
    """Demonstrate width, height, and alignment options."""
    print("📏 Layout and Sizing Examples:\n")
    
    # Width examples
    widths = [20, 40, 60]
    for width in widths:
        content = f"Width: {width} chars"
        styled = GumWrapper.style(
            content,
            width=width,
            border="thick",
            padding="1",
            foreground="purple"
        )
        print(styled)
        print()
    
    # Alignment examples  
    alignments = ["left", "center", "right"]
    for align in alignments:
        styled = GumWrapper.style(
            f"Aligned {align}",
            width=30,
            align=align,
            border="dashed",
            padding="1",
            foreground="yellow"
        )
        print(styled)
        print()


def demo_color_combinations():
    """Demonstrate foreground and background color combinations."""
    print("🌈 Color Combination Examples:\n")
    
    # Predefined color combinations
    combinations = [
        ("White on black", "white", "black"),
        ("Yellow on blue", "yellow", "blue"),
        ("Green on dark gray", "green", "240"),
        ("Red on light gray", "red", "250"),
        ("Cyan on purple", "cyan", "purple")
    ]
    
    for desc, fg, bg in combinations:
        styled = GumWrapper.style(
            desc,
            foreground=fg,
            background=bg,
            padding="1",
            border="rounded"
        )
        print(styled)
        print()
    
    # 256-color examples
    print("256-color palette examples:")
    color_numbers = ["196", "46", "21", "226", "201", "51"]
    for color_num in color_numbers:
        styled = GumWrapper.style(
            f"Color #{color_num}",
            foreground=color_num,
            border="thick",
            padding="1"
        )
        print(styled)
        print()


def demo_border_colors():
    """Demonstrate border coloring options."""
    print("🖼️  Border Color Examples:\n")
    
    border_colors = [
        ("Red border", "red", None),
        ("Blue border", "blue", None), 
        ("Green background border", None, "green"),
        ("Yellow fg, Purple bg border", "yellow", "purple")
    ]
    
    for desc, border_fg, border_bg in border_colors:
        kwargs = {
            "border": "thick",
            "padding": "1 2"
        }
        if border_fg:
            kwargs["border_foreground"] = border_fg
        if border_bg:
            kwargs["border_background"] = border_bg
        
        styled = GumWrapper.style(desc, **kwargs)
        print(styled)
        print()


def demo_complex_layouts():
    """Demonstrate complex multi-element layouts."""
    print("🏗️  Complex Layout Examples:\n")
    
    # Create a status dashboard
    print("System Status Dashboard:")
    
    # Header
    header = GumWrapper.style(
        "🖥️  SYSTEM STATUS",
        foreground="white",
        background="blue",
        width=50,
        align="center",
        padding="1",
        bold=True
    )
    print(header)
    
    # Status items
    statuses = [
        ("CPU Usage", "23%", "green"),
        ("Memory Usage", "67%", "yellow"), 
        ("Disk Space", "89%", "red"),
        ("Network", "Online", "green"),
        ("Services", "Running", "green")
    ]
    
    for label, value, color in statuses:
        status_line = GumWrapper.style(
            f"{label:.<20} {value:>10}",
            foreground=color,
            border="none",
            padding="0 2"
        )
        print(status_line)
    
    # Footer
    footer = GumWrapper.style(
        "Last updated: 2024-01-15 14:30:00",
        foreground="240",
        width=50,
        align="center",
        padding="1",
        italic=True
    )
    print(footer)
    print()


def demo_notification_styles():
    """Demonstrate different notification/alert styles."""
    print("🔔 Notification Style Examples:\n")
    
    notifications = [
        ("✅ Success", "Operation completed successfully", "green", "rounded"),
        ("⚠️  Warning", "Please review your settings", "yellow", "dashed"),
        ("❌ Error", "Something went wrong", "red", "thick"),
        ("ℹ️  Info", "New update available", "blue", "double"),
        ("🚀 Launch", "Deployment in progress", "purple", "rounded")
    ]
    
    for icon, message, color, border in notifications:
        # Title
        title = GumWrapper.style(
            icon,
            foreground=color,
            bold=True,
            padding="0 1"
        )
        
        # Content
        content = GumWrapper.style(
            message,
            foreground=color,
            border=border,
            padding="1 2",
            width=40
        )
        
        print(title)
        print(content)
        print()


def demo_progress_indicators():
    """Demonstrate styled progress indicators and status bars."""
    print("📊 Progress Indicator Examples:\n")
    
    # Simple progress bars
    progress_levels = [
        ("Starting", 10, "red"),
        ("In Progress", 45, "yellow"),
        ("Almost Done", 85, "green"),
        ("Complete", 100, "blue")
    ]
    
    for label, percent, color in progress_levels:
        # Progress bar
        filled = "█" * (percent // 5)
        empty = "░" * (20 - (percent // 5))
        bar = f"{filled}{empty}"
        
        progress_display = GumWrapper.style(
            f"{label:<15} [{bar}] {percent:>3}%",
            foreground=color,
            border="rounded",
            padding="0 1"
        )
        print(progress_display)
    
    print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("Available styling examples:")
        print("  python style_example.py basic")
        print("  python style_example.py borders")
        print("  python style_example.py layout")
        print("  python style_example.py colors")
        print("  python style_example.py border_colors")
        print("  python style_example.py complex")
        print("  python style_example.py notifications")
        print("  python style_example.py progress")
        print("  python style_example.py all")
        
    elif "basic" in sys.argv:
        demo_basic_styling()
    elif "borders" in sys.argv:
        demo_borders_and_padding()
    elif "layout" in sys.argv:
        demo_layout_and_sizing()
    elif "colors" in sys.argv:
        demo_color_combinations()
    elif "border_colors" in sys.argv:
        demo_border_colors()
    elif "complex" in sys.argv:
        demo_complex_layouts()
    elif "notifications" in sys.argv:
        demo_notification_styles()
    elif "progress" in sys.argv:
        demo_progress_indicators()
    elif "all" in sys.argv:
        demo_basic_styling()
        demo_borders_and_padding()
        demo_layout_and_sizing()
        demo_color_combinations()
        demo_border_colors()
        demo_complex_layouts()
        demo_notification_styles()
        demo_progress_indicators()