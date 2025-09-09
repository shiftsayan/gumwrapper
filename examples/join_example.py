#!/usr/bin/env python3
"""
Example demonstrating the 'join' command for combining text elements.
This shows various ways to layout and combine text horizontally and vertically.
"""

from gumwrapper import GumWrapper


def demo_vertical_joining():
    """Demonstrate vertical text joining with different alignments."""
    print("↕️ Vertical Joining Examples:\n")
    
    # Basic vertical join
    items = ["First item", "Second item", "Third item"]
    
    print("Basic vertical join:")
    vertical_basic = GumWrapper.join(items, vertical=True)
    print(vertical_basic)
    print()
    
    # Vertical join with different alignments
    alignments = ["left", "center", "right"]
    
    for alignment in alignments:
        print(f"Vertical join - {alignment} aligned:")
        vertical_aligned = GumWrapper.join(
            items,
            vertical=True,
            align=alignment
        )
        print(vertical_aligned)
        print()


def demo_horizontal_joining():
    """Demonstrate horizontal text joining."""
    print("↔️ Horizontal Joining Examples:\n")
    
    # Basic horizontal join
    items = ["🏠 Home", "👤 Profile", "⚙️ Settings", "🔐 Logout"]
    
    print("Basic horizontal join:")
    horizontal_basic = GumWrapper.join(items, horizontal=True)
    print(horizontal_basic)
    print()
    
    # Horizontal join with alignment
    alignments = ["left", "center", "right"]
    
    for alignment in alignments:
        print(f"Horizontal join - {alignment} aligned:")
        horizontal_aligned = GumWrapper.join(
            items,
            horizontal=True,
            align=alignment
        )
        print(horizontal_aligned)
        print()


def demo_styled_elements():
    """Demonstrate joining styled text elements."""
    print("🎨 Joining Styled Elements:\n")
    
    # Create individually styled elements
    styled_items = [
        GumWrapper.style("SUCCESS", foreground="green", bold=True),
        GumWrapper.style("WARNING", foreground="yellow", bold=True),
        GumWrapper.style("ERROR", foreground="red", bold=True),
        GumWrapper.style("INFO", foreground="blue", bold=True)
    ]
    
    print("Vertical styled elements:")
    vertical_styled = GumWrapper.join(styled_items, vertical=True, align="center")
    print(vertical_styled)
    print()
    
    print("Horizontal styled elements:")
    horizontal_styled = GumWrapper.join(styled_items, horizontal=True, align="center")
    print(horizontal_styled)
    print()


def demo_dashboard_layout():
    """Demonstrate creating a dashboard-like layout."""
    print("📊 Dashboard Layout Example:\n")
    
    # Create dashboard components
    title = GumWrapper.style(
        "📈 SYSTEM DASHBOARD",
        foreground="white",
        background="blue",
        padding="1",
        bold=True,
        width=40,
        align="center"
    )
    
    # Status indicators
    statuses = [
        GumWrapper.style("🟢 Services: Online", foreground="green"),
        GumWrapper.style("🟡 Load: Medium", foreground="yellow"), 
        GumWrapper.style("🔴 Alerts: 3 Active", foreground="red"),
        GumWrapper.style("🔵 Users: 1,247 Active", foreground="blue")
    ]
    
    status_panel = GumWrapper.join(statuses, vertical=True, align="left")
    status_box = GumWrapper.style(
        status_panel,
        border="rounded",
        padding="1",
        width=35
    )
    
    # Metrics
    metrics = [
        "CPU: 23%",
        "Memory: 67%", 
        "Disk: 45%",
        "Network: 12 Mbps"
    ]
    
    metrics_panel = GumWrapper.join(metrics, vertical=True, align="left")
    metrics_box = GumWrapper.style(
        metrics_panel,
        border="thick",
        padding="1",
        foreground="cyan",
        width=25
    )
    
    # Combine horizontally
    main_content = GumWrapper.join(
        [status_box, metrics_box],
        horizontal=True,
        align="left"
    )
    
    # Full dashboard
    dashboard = GumWrapper.join(
        [title, main_content],
        vertical=True,
        align="center"
    )
    
    print(dashboard)
    print()


def demo_navigation_menu():
    """Demonstrate creating navigation menus."""
    print("🧭 Navigation Menu Examples:\n")
    
    # Horizontal navigation
    nav_items = [
        GumWrapper.style("Home", foreground="white", background="blue", padding="0 2"),
        GumWrapper.style("About", foreground="blue", padding="0 2"),
        GumWrapper.style("Services", foreground="blue", padding="0 2"),
        GumWrapper.style("Contact", foreground="blue", padding="0 2")
    ]
    
    horizontal_nav = GumWrapper.join(nav_items, horizontal=True, align="left")
    print("Horizontal Navigation:")
    print(horizontal_nav)
    print()
    
    # Vertical sidebar navigation
    sidebar_items = [
        "📊 Dashboard",
        "👥 Users",
        "📝 Content",
        "⚙️  Settings",
        "📈 Analytics",
        "🔐 Security"
    ]
    
    styled_sidebar = [
        GumWrapper.style(item, foreground="cyan", padding="0 1")
        for item in sidebar_items
    ]
    
    vertical_nav = GumWrapper.join(styled_sidebar, vertical=True, align="left")
    sidebar_box = GumWrapper.style(
        vertical_nav,
        border="rounded",
        padding="1",
        width=20
    )
    
    print("Vertical Sidebar Navigation:")
    print(sidebar_box)
    print()


def demo_card_layout():
    """Demonstrate card-like layouts."""
    print("🃏 Card Layout Examples:\n")
    
    # Create multiple cards
    card1_content = GumWrapper.join([
        GumWrapper.style("USER PROFILE", foreground="blue", bold=True),
        "Name: John Doe",
        "Email: john@example.com", 
        "Role: Administrator",
        "Last Login: 2 hours ago"
    ], vertical=True, align="left")
    
    card1 = GumWrapper.style(
        card1_content,
        border="rounded",
        padding="1",
        width=25
    )
    
    card2_content = GumWrapper.join([
        GumWrapper.style("SYSTEM STATUS", foreground="green", bold=True),
        "Uptime: 15 days",
        "CPU: 23%",
        "Memory: 67%",
        "Status: Healthy"
    ], vertical=True, align="left")
    
    card2 = GumWrapper.style(
        card2_content,
        border="thick", 
        padding="1",
        width=25
    )
    
    card3_content = GumWrapper.join([
        GumWrapper.style("RECENT ACTIVITY", foreground="purple", bold=True),
        "• User login",
        "• File uploaded",
        "• Settings changed",
        "• Backup completed"
    ], vertical=True, align="left")
    
    card3 = GumWrapper.style(
        card3_content,
        border="double",
        padding="1", 
        width=25
    )
    
    # Arrange cards horizontally
    cards_row = GumWrapper.join([card1, card2, card3], horizontal=True, align="left")
    print("Card Layout:")
    print(cards_row)
    print()


def demo_table_like_layout():
    """Demonstrate table-like layouts using join."""
    print("📋 Table-like Layout:\n")
    
    # Create table headers
    headers = [
        GumWrapper.style("ID", foreground="white", background="blue", padding="0 2", width=8, align="center"),
        GumWrapper.style("Name", foreground="white", background="blue", padding="0 2", width=15, align="center"),
        GumWrapper.style("Status", foreground="white", background="blue", padding="0 2", width=10, align="center"),
        GumWrapper.style("Actions", foreground="white", background="blue", padding="0 2", width=12, align="center")
    ]
    
    header_row = GumWrapper.join(headers, horizontal=True)
    
    # Create table rows
    rows_data = [
        ("001", "Alice Johnson", "Active", "Edit | Delete"),
        ("002", "Bob Smith", "Inactive", "Edit | Delete"),
        ("003", "Carol Davis", "Pending", "Edit | Delete")
    ]
    
    table_rows = []
    for row_data in rows_data:
        row_cells = [
            GumWrapper.style(str(cell), padding="0 2", width=widths[i], align="left" if i == 1 else "center")
            for i, (cell, widths) in enumerate(zip(row_data, [8, 15, 10, 12]))
        ]
        table_rows.append(GumWrapper.join(row_cells, horizontal=True))
    
    # Combine all rows
    full_table = GumWrapper.join([header_row] + table_rows, vertical=True)
    
    # Add border around entire table
    table_with_border = GumWrapper.style(
        full_table,
        border="thick",
        padding="1"
    )
    
    print("Table Layout:")
    print(table_with_border)
    print()


def demo_complex_layout():
    """Demonstrate a complex multi-section layout."""
    print("🏗️  Complex Layout Example:\n")
    
    # Header
    header = GumWrapper.style(
        "🚀 APPLICATION CONTROL PANEL",
        foreground="white",
        background="purple",
        padding="1",
        width=60,
        align="center",
        bold=True
    )
    
    # Left panel
    left_menu = GumWrapper.join([
        GumWrapper.style("NAVIGATION", foreground="cyan", bold=True),
        "• Dashboard",
        "• Users",
        "• Settings", 
        "• Reports",
        "• Help"
    ], vertical=True, align="left")
    
    left_panel = GumWrapper.style(
        left_menu,
        border="rounded",
        padding="1",
        width=20
    )
    
    # Main content area
    main_content = GumWrapper.join([
        GumWrapper.style("MAIN CONTENT", foreground="green", bold=True),
        "",
        "Welcome to the application!",
        "",
        "Recent activities:",
        "✓ System backup completed",
        "✓ User database updated",
        "⚠ 2 warnings found",
        "",
        "Quick actions:",
        "[Deploy] [Backup] [Monitor]"
    ], vertical=True, align="left")
    
    main_panel = GumWrapper.style(
        main_content,
        border="thick",
        padding="1 2",
        width=35
    )
    
    # Right panel
    right_info = GumWrapper.join([
        GumWrapper.style("SYSTEM INFO", foreground="yellow", bold=True),
        "",
        "Uptime: 5d 12h",
        "Users: 1,247",
        "Load: Normal",
        "",
        GumWrapper.style("ALERTS", foreground="red", bold=True),
        "",
        "⚠ Disk 85% full",
        "ℹ Update available"
    ], vertical=True, align="left")
    
    right_panel = GumWrapper.style(
        right_info,
        border="dashed",
        padding="1",
        width=18
    )
    
    # Combine main content area
    content_area = GumWrapper.join(
        [left_panel, main_panel, right_panel],
        horizontal=True,
        align="left"
    )
    
    # Footer
    footer = GumWrapper.style(
        "Status: Online | Version: 2.1.0 | Last updated: 2024-01-15 14:30",
        foreground="240",
        width=60,
        align="center",
        italic=True
    )
    
    # Full layout
    full_layout = GumWrapper.join(
        [header, "", content_area, "", footer],
        vertical=True,
        align="center"
    )
    
    print(full_layout)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 1:
        print("Available join examples:")
        print("  python join_example.py vertical")
        print("  python join_example.py horizontal")
        print("  python join_example.py styled")
        print("  python join_example.py dashboard")
        print("  python join_example.py navigation")
        print("  python join_example.py cards")
        print("  python join_example.py table")
        print("  python join_example.py complex")
        print("  python join_example.py all")
        
    elif "vertical" in sys.argv:
        demo_vertical_joining()
    elif "horizontal" in sys.argv:
        demo_horizontal_joining()
    elif "styled" in sys.argv:
        demo_styled_elements()
    elif "dashboard" in sys.argv:
        demo_dashboard_layout()
    elif "navigation" in sys.argv:
        demo_navigation_menu()
    elif "cards" in sys.argv:
        demo_card_layout()
    elif "table" in sys.argv:
        demo_table_like_layout()
    elif "complex" in sys.argv:
        demo_complex_layout()
    elif "all" in sys.argv:
        demo_vertical_joining()
        demo_horizontal_joining()
        demo_styled_elements()
        demo_dashboard_layout()
        demo_navigation_menu()
        demo_card_layout()
        demo_table_like_layout()
        demo_complex_layout()