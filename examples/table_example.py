#!/usr/bin/env python3
"""
Example demonstrating the 'table' command for displaying tabular data.
This shows various table configurations and data presentation methods.
"""

import csv
import os
import tempfile

from gumwrapper import GumPrompt


def create_sample_csv_file(data, headers):
    """Helper function to create a temporary CSV file."""
    temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False)
    writer = csv.writer(temp_file)
    writer.writerow(headers)
    writer.writerows(data)
    temp_file.close()
    return temp_file.name


def demo_basic_table():
    """Demonstrate basic table functionality."""
    print("📊 Basic Table Example:\n")

    # Sample user data
    headers = ["ID", "Name", "Email", "Role", "Status"]
    data = [
        ["001", "Alice Johnson", "alice@company.com", "Admin", "Active"],
        ["002", "Bob Smith", "bob@company.com", "User", "Active"],
        ["003", "Carol Davis", "carol@company.com", "Manager", "Inactive"],
        ["004", "David Wilson", "david@company.com", "User", "Active"],
        ["005", "Eve Brown", "eve@company.com", "Admin", "Pending"],
    ]

    # Create temporary CSV file
    csv_file = create_sample_csv_file(data, headers)

    try:
        print("User Management Table:")
        table_output = GumPrompt.table(
            file_path=csv_file,
            separator=",",
            columns=headers,
            print_static=True,
            border="rounded",
            height=8,
        )
        print(table_output)

    except Exception as e:
        print(f"Error displaying table: {e}")
        # Fallback to manual table display
        print("Fallback table display:")
        for i, header in enumerate(headers):
            print(f"{header:>15}", end=" ")
        print()
        print("-" * (16 * len(headers)))
        for row in data:
            for cell in row:
                print(f"{cell:>15}", end=" ")
            print()

    finally:
        # Clean up temp file
        try:
            os.unlink(csv_file)
        except:
            pass

    print()


def demo_sales_report_table():
    """Demonstrate a sales report table with financial data."""
    print("💰 Sales Report Table:\n")

    headers = ["Quarter", "Region", "Sales", "Target", "Performance", "Trend"]
    data = [
        ["Q1 2024", "North", "$125,400", "$120,000", "104.5%", "↗️"],
        ["Q1 2024", "South", "$98,750", "$100,000", "98.8%", "↘️"],
        ["Q1 2024", "East", "$156,200", "$150,000", "104.1%", "↗️"],
        ["Q1 2024", "West", "$134,800", "$130,000", "103.7%", "↗️"],
        ["Q2 2024", "North", "$142,300", "$125,000", "113.8%", "📈"],
        ["Q2 2024", "South", "$118,900", "$105,000", "113.2%", "📈"],
        ["Q2 2024", "East", "$167,500", "$160,000", "104.7%", "↗️"],
        ["Q2 2024", "West", "$145,600", "$135,000", "107.9%", "↗️"],
    ]

    csv_file = create_sample_csv_file(data, headers)

    try:
        print("Regional Sales Performance:")
        table_output = GumPrompt.table(
            file_path=csv_file,
            separator=",",
            columns=headers,
            widths=[10, 8, 12, 12, 12, 8],
            print_static=True,
            border="thick",
            height=12,
        )
        print(table_output)

    except Exception as e:
        print(f"Error displaying sales table: {e}")
        # Create a styled fallback
        print("Sales Performance Summary:")
        for quarter in ["Q1 2024", "Q2 2024"]:
            quarter_data = [row for row in data if row[0] == quarter]
            print(f"\n{quarter}:")
            for row in quarter_data:
                region, sales, target, performance, trend = row[1:]
                print(f"  {region:>8}: {sales:>12} ({performance:>7}) {trend}")

    finally:
        try:
            os.unlink(csv_file)
        except:
            pass

    print()


def demo_system_monitoring_table():
    """Demonstrate system monitoring data in table format."""
    print("🖥️  System Monitoring Table:\n")

    headers = [
        "Server",
        "CPU %",
        "Memory %",
        "Disk %",
        "Network I/O",
        "Uptime",
        "Status",
    ]
    data = [
        ["web-01", "23.4", "67.2", "45.1", "1.2 MB/s", "15d 4h", "🟢 Healthy"],
        ["web-02", "31.8", "72.5", "38.7", "2.1 MB/s", "15d 4h", "🟢 Healthy"],
        ["db-01", "78.9", "85.3", "92.1", "5.7 MB/s", "12d 8h", "🟡 Warning"],
        ["cache-01", "12.1", "34.6", "23.4", "0.8 MB/s", "20d 1h", "🟢 Healthy"],
        ["lb-01", "45.2", "56.8", "34.2", "3.2 MB/s", "18d 2h", "🟢 Healthy"],
        ["backup-01", "89.3", "91.7", "78.5", "12.1 MB/s", "5d 3h", "🔴 Critical"],
    ]

    csv_file = create_sample_csv_file(data, headers)

    try:
        print("Infrastructure Health Dashboard:")
        table_output = GumPrompt.table(
            file_path=csv_file,
            separator=",",
            columns=headers,
            widths=[12, 8, 10, 8, 12, 10, 12],
            print_static=True,
            border="double",
            height=10,
        )
        print(table_output)

    except Exception as e:
        print(f"Error displaying monitoring table: {e}")
        # Create a styled status display
        print("Server Status Overview:")
        for server_data in data:
            server, cpu, memory, disk, network, uptime, status = server_data
            status_color = (
                "green" if "🟢" in status else "yellow" if "🟡" in status else "red"
            )

            server_line = GumPrompt.style(
                f"{server:>12}: CPU {cpu:>5}% | Mem {memory:>5}% | {status}",
                foreground=status_color,
            )
            print(server_line)

    finally:
        try:
            os.unlink(csv_file)
        except:
            pass

    print()


def demo_project_tracking_table():
    """Demonstrate project tracking with task status."""
    print("📋 Project Tracking Table:\n")

    headers = [
        "Task ID",
        "Title",
        "Assignee",
        "Priority",
        "Status",
        "Due Date",
        "Progress",
    ]
    data = [
        [
            "TSK-001",
            "User Authentication",
            "Alice",
            "High",
            "In Progress",
            "2024-01-20",
            "75%",
        ],
        [
            "TSK-002",
            "Database Migration",
            "Bob",
            "Critical",
            "Blocked",
            "2024-01-18",
            "30%",
        ],
        ["TSK-003", "UI Redesign", "Carol", "Medium", "Testing", "2024-01-25", "90%"],
        [
            "TSK-004",
            "API Documentation",
            "David",
            "Low",
            "Not Started",
            "2024-01-30",
            "0%",
        ],
        [
            "TSK-005",
            "Performance Optimization",
            "Alice",
            "High",
            "Complete",
            "2024-01-15",
            "100%",
        ],
        [
            "TSK-006",
            "Security Audit",
            "Eve",
            "Critical",
            "In Progress",
            "2024-01-22",
            "45%",
        ],
        [
            "TSK-007",
            "Mobile Responsiveness",
            "Carol",
            "Medium",
            "In Progress",
            "2024-01-28",
            "60%",
        ],
    ]

    csv_file = create_sample_csv_file(data, headers)

    try:
        print("Development Sprint Board:")
        table_output = GumPrompt.table(
            file_path=csv_file,
            separator=",",
            columns=headers,
            widths=[8, 20, 10, 8, 12, 12, 8],
            print_static=True,
            border="rounded",
            height=12,
        )
        print(table_output)

    except Exception as e:
        print(f"Error displaying project table: {e}")
        # Group tasks by status for fallback display
        status_groups = {}
        for task in data:
            status = task[4]
            if status not in status_groups:
                status_groups[status] = []
            status_groups[status].append(task)

        print("Tasks by Status:")
        for status, tasks in status_groups.items():
            status_styled = GumPrompt.style(
                f"\n{status}:", foreground="cyan", bold=True
            )
            print(status_styled)
            for task in tasks:
                task_id, title, assignee, priority, _, due_date, progress = task
                print(f"  {task_id}: {title} ({assignee}) - {progress} by {due_date}")

    finally:
        try:
            os.unlink(csv_file)
        except:
            pass

    print()


def demo_financial_summary_table():
    """Demonstrate financial data table."""
    print("💸 Financial Summary Table:\n")

    headers = ["Account", "Type", "Balance", "Change", "% Change", "Last Updated"]
    data = [
        ["Operations", "Checking", "$125,430.50", "+$2,340.00", "+1.9%", "Today"],
        ["Savings", "Savings", "$450,250.75", "+$1,500.00", "+0.3%", "Today"],
        [
            "Investments",
            "Portfolio",
            "$1,234,567.89",
            "-$15,430.50",
            "-1.2%",
            "Yesterday",
        ],
        ["Payroll", "Checking", "$89,750.25", "-$45,200.00", "-33.5%", "Today"],
        ["Emergency Fund", "Savings", "$75,000.00", "$0.00", "0.0%", "Last week"],
        ["Equipment", "Asset", "$234,500.00", "+$12,500.00", "+5.6%", "This week"],
    ]

    csv_file = create_sample_csv_file(data, headers)

    try:
        print("Account Balance Overview:")
        table_output = GumPrompt.table(
            file_path=csv_file,
            separator=",",
            columns=headers,
            widths=[15, 12, 15, 15, 10, 15],
            print_static=True,
            border="thick",
            height=10,
        )
        print(table_output)

    except Exception as e:
        print(f"Error displaying financial table: {e}")
        # Calculate totals for fallback
        total_balance = 0
        total_change = 0

        print("Financial Overview:")
        for account_data in data:
            account, acc_type, balance, change, percent, updated = account_data

            # Extract numeric values (simplified)
            balance_num = float(balance.replace("$", "").replace(",", ""))
            change_num = float(
                change.replace("$", "").replace(",", "").replace("+", "")
            )

            total_balance += balance_num
            total_change += change_num

            # Color code based on change
            if change_num > 0:
                change_color = "green"
            elif change_num < 0:
                change_color = "red"
            else:
                change_color = "yellow"

            account_line = GumPrompt.style(
                f"{account:>15}: {balance:>15} ({change:>10})", foreground=change_color
            )
            print(account_line)

        # Display totals
        total_line = GumPrompt.style(
            f"{'TOTAL':>15}: ${total_balance:>14,.2f} (${total_change:>9,.2f})",
            bold=True,
            border="dashed",
            padding="0 1",
        )
        print(f"\n{total_line}")

    finally:
        try:
            os.unlink(csv_file)
        except:
            pass

    print()


def demo_custom_table_styles():
    """Demonstrate different table border styles."""
    print("🎨 Table Style Variations:\n")

    headers = ["Style", "Description", "Use Case"]
    data = [
        ["rounded", "Soft rounded corners", "Modern dashboards"],
        ["thick", "Bold thick lines", "Important data"],
        ["double", "Double-line border", "Formal reports"],
        ["none", "No border", "Clean layouts"],
    ]

    border_styles = ["rounded", "thick", "double"]

    for border_style in border_styles:
        csv_file = create_sample_csv_file(data, headers)

        try:
            print(f"Border style: {border_style}")
            table_output = GumPrompt.table(
                file_path=csv_file,
                separator=",",
                columns=headers,
                widths=[10, 20, 20],
                print_static=True,
                border=border_style,
                height=8,
            )
            print(table_output)
            print()

        except Exception as e:
            print(f"Error with {border_style} table: {e}")

        finally:
            try:
                os.unlink(csv_file)
            except:
                pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available table examples:")
        print("  python table_example.py basic")
        print("  python table_example.py sales")
        print("  python table_example.py monitoring")
        print("  python table_example.py projects")
        print("  python table_example.py financial")
        print("  python table_example.py styles")
        print("  python table_example.py all")

    elif "basic" in sys.argv:
        demo_basic_table()
    elif "sales" in sys.argv:
        demo_sales_report_table()
    elif "monitoring" in sys.argv:
        demo_system_monitoring_table()
    elif "projects" in sys.argv:
        demo_project_tracking_table()
    elif "financial" in sys.argv:
        demo_financial_summary_table()
    elif "styles" in sys.argv:
        demo_custom_table_styles()
    elif "all" in sys.argv:
        demo_basic_table()
        demo_sales_report_table()
        demo_system_monitoring_table()
        demo_project_tracking_table()
        demo_financial_summary_table()
        demo_custom_table_styles()
