#!/usr/bin/env python3
"""
Example demonstrating the 'log' command for structured logging output.
This shows various logging configurations and message formatting.
"""

import os
import tempfile
from datetime import datetime

from gumwrapper import GumPrompt


def demo_basic_logging():
    """Demonstrate basic logging functionality."""
    print("📝 Basic Logging Examples:\n")

    # Simple log messages
    messages = [
        "Application started successfully",
        "Database connection established",
        "User authentication completed",
        "Processing user request",
        "Request completed successfully",
    ]

    print("Basic log output:")
    GumPrompt.log(messages, formatter="text", level="info", prefix="APP")
    print()


def demo_different_log_levels():
    """Demonstrate logging with different levels."""
    print("📊 Log Level Examples:\n")

    levels = ["debug", "info", "warn", "error"]

    for level in levels:
        messages = [
            f"This is a {level.upper()} level message",
            f"Another {level} entry for demonstration",
        ]

        print(f"{level.upper()} Level:")
        GumPrompt.log(messages, formatter="text", level=level, prefix=level.upper())
        print()


def demo_json_logging():
    """Demonstrate JSON formatted logging."""
    print("🔗 JSON Logging Example:\n")

    # Structured log messages that work well with JSON format
    json_messages = [
        'user_login: {"user_id": 12345, "username": "alice", "ip": "192.168.1.100"}',
        'api_request: {"endpoint": "/api/users", "method": "GET", "response_time": "45ms"}',
        'database_query: {"table": "users", "operation": "SELECT", "duration": "12ms"}',
        'error_occurred: {"error": "ValidationError", "field": "email", "message": "Invalid format"}',
    ]

    print("JSON formatted logs:")
    GumPrompt.log(
        json_messages, formatter="json", level="info", prefix="API", structured=True
    )
    print()


def demo_application_logging():
    """Demonstrate application-specific logging scenarios."""
    print("🚀 Application Logging Scenarios:\n")

    # Web server logs
    print("Web Server Access Logs:")
    access_logs = [
        'GET /api/users 200 45ms "Mozilla/5.0" 192.168.1.100',
        'POST /api/login 401 23ms "curl/7.68.0" 192.168.1.101',
        'GET /dashboard 200 123ms "Mozilla/5.0" 192.168.1.100',
        'DELETE /api/users/123 204 67ms "MyApp/1.0" 192.168.1.102',
    ]

    GumPrompt.log(
        access_logs,
        formatter="text",
        level="info",
        prefix="WEB",
        time_format="15:04:05",
    )
    print()

    # Database operation logs
    print("Database Operation Logs:")
    db_logs = [
        "Connection pool initialized with 10 connections",
        "Migration 20240115_001 applied successfully",
        "Slow query detected: SELECT * FROM users WHERE created_at < '2023-01-01' (2.3s)",
        "Index created on users.email column",
        "Database backup completed (size: 1.2GB)",
    ]

    GumPrompt.log(
        db_logs,
        formatter="text",
        level="info",
        prefix="DB",
        time_format="2006-01-02 15:04:05",
    )
    print()


def demo_error_logging():
    """Demonstrate error and exception logging."""
    print("🚨 Error Logging Examples:\n")

    error_messages = [
        "CRITICAL: Database connection failed - retrying in 30s",
        "ERROR: Failed to process payment for order #12345",
        "WARNING: Memory usage above 85% threshold (current: 87%)",
        "ERROR: Authentication service unavailable - using cache",
        "CRITICAL: Disk space critically low (< 100MB remaining)",
    ]

    print("Error and Critical Logs:")
    GumPrompt.log(
        error_messages, formatter="text", level="error", prefix="SYS", structured=False
    )
    print()


def demo_performance_logging():
    """Demonstrate performance and metrics logging."""
    print("⚡ Performance Logging Examples:\n")

    performance_logs = [
        "request_duration: 45.2ms endpoint=/api/users method=GET",
        "memory_usage: 67% heap=256MB allocated=171MB",
        "cache_hit_ratio: 85.3% hits=1247 misses=215",
        "database_connections: active=8 idle=12 max=20",
        "response_times: p50=23ms p95=89ms p99=156ms",
    ]

    print("Performance Metrics:")
    GumPrompt.log(
        performance_logs,
        formatter="json",
        level="info",
        prefix="METRICS",
        structured=True,
    )
    print()


def demo_deployment_logging():
    """Demonstrate deployment and operational logging."""
    print("🚀 Deployment Logging Examples:\n")

    deployment_logs = [
        "BUILD: Starting deployment pipeline for version v2.1.0",
        "TEST: Running automated test suite (234 tests)",
        "TEST: All tests passed successfully",
        "DEPLOY: Uploading artifacts to staging environment",
        "DEPLOY: Database migrations applied (3 pending)",
        "HEALTH: Health checks passed - application ready",
        "DEPLOY: Traffic routing updated to new version",
        "SUCCESS: Deployment completed in 4m 32s",
    ]

    print("Deployment Pipeline Logs:")
    GumPrompt.log(deployment_logs, formatter="text", level="info", prefix="DEPLOY")
    print()


def demo_security_logging():
    """Demonstrate security-related logging."""
    print("🔐 Security Logging Examples:\n")

    security_logs = [
        "AUTH: User login successful - user_id=12345 ip=192.168.1.100",
        "SECURITY: Failed login attempt - username=admin ip=10.0.0.50 (attempt 3/5)",
        "AUDIT: Admin user modified permissions for user_id=67890",
        "SECURITY: Rate limit exceeded - ip=203.0.113.0 blocked for 1h",
        "AUTH: Password reset requested for user@example.com",
        "AUDIT: File download - user_id=12345 file=confidential_report.pdf",
        "SECURITY: Suspicious API usage pattern detected - investigating",
    ]

    print("Security Audit Logs:")
    GumPrompt.log(
        security_logs, formatter="json", level="warn", prefix="SEC", structured=True
    )
    print()


def demo_file_logging():
    """Demonstrate logging to files."""
    print("📄 File Logging Example:\n")

    # Create a temporary log file
    temp_log = tempfile.NamedTemporaryFile(mode="w", suffix=".log", delete=False)
    temp_log.close()

    file_messages = [
        "Application initialized with configuration file: /etc/myapp/config.yaml",
        "Loaded 47 plugins from /usr/local/lib/myapp/plugins/",
        "Started background worker processes (3 workers)",
        "HTTP server listening on port 8080",
        "Ready to accept connections",
    ]

    try:
        print(f"Logging to file: {temp_log.name}")

        # Log to file
        GumPrompt.log(
            file_messages,
            file_path=temp_log.name,
            formatter="text",
            level="info",
            prefix="APP",
            time_format="2006-01-02 15:04:05",
        )

        # Read and display file contents
        print("File contents:")
        with open(temp_log.name, "r") as f:
            content = f.read()
            if content:
                # Style the file content for display
                styled_content = GumPrompt.style(
                    content, foreground="green", border="rounded", padding="1"
                )
                print(styled_content)
            else:
                print("(File logging may not be visible in this demo)")

    except Exception as e:
        print(f"File logging error: {e}")

    finally:
        # Clean up temp file
        try:
            os.unlink(temp_log.name)
        except:
            pass

    print()


def demo_custom_log_formats():
    """Demonstrate custom formatting options."""
    print("🎨 Custom Log Formatting:\n")

    messages = [
        "User session started",
        "Processing user request",
        "Database query executed",
        "Response sent to client",
    ]

    # Different formatter configurations
    formats = [
        ("Simple text", {"formatter": "text", "prefix": "APP"}),
        (
            "With timestamps",
            {"formatter": "text", "prefix": "APP", "time_format": "15:04:05"},
        ),
        ("JSON structured", {"formatter": "json", "prefix": "API", "structured": True}),
        ("Custom prefix", {"formatter": "text", "prefix": "🚀 MYAPP", "level": "info"}),
    ]

    for description, kwargs in formats:
        print(f"{description}:")
        GumPrompt.log(messages[:2], **kwargs)  # Just show first 2 messages
        print()


def demo_real_world_scenario():
    """Demonstrate a real-world logging scenario with mixed message types."""
    print("🌍 Real-World Logging Scenario:\n")

    # Simulate an e-commerce application startup and operation
    startup_logs = [
        "🚀 E-Commerce Application Starting...",
        "📦 Loading configuration from environment variables",
        "🔗 Connecting to PostgreSQL database (host: db.example.com:5432)",
        "💾 Running database migrations (3 pending)",
        "🔧 Initializing Redis cache connection",
        "🌐 Starting HTTP server on port 8080",
        "📡 Health check endpoint available at /health",
        "✅ Application ready to serve requests",
    ]

    print("Application Startup:")
    GumPrompt.log(startup_logs, formatter="text", level="info", prefix="ECOM")
    print()

    # Simulate request processing
    request_logs = [
        "📥 Incoming request: GET /api/products?category=electronics",
        "🔍 Executing product search query (category_id=5)",
        "💾 Cache miss - fetching from database",
        "📊 Query executed in 23ms (15 products found)",
        "💾 Storing results in cache (TTL: 300s)",
        "📤 Response sent (200 OK) - total time: 45ms",
    ]

    print("Request Processing:")
    GumPrompt.log(
        request_logs, formatter="json", level="info", prefix="REQ", structured=True
    )
    print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("Available log examples:")
        print("  python log_example.py basic")
        print("  python log_example.py levels")
        print("  python log_example.py json")
        print("  python log_example.py application")
        print("  python log_example.py errors")
        print("  python log_example.py performance")
        print("  python log_example.py deployment")
        print("  python log_example.py security")
        print("  python log_example.py file")
        print("  python log_example.py formats")
        print("  python log_example.py realworld")
        print("  python log_example.py all")

    elif "basic" in sys.argv:
        demo_basic_logging()
    elif "levels" in sys.argv:
        demo_different_log_levels()
    elif "json" in sys.argv:
        demo_json_logging()
    elif "application" in sys.argv:
        demo_application_logging()
    elif "errors" in sys.argv:
        demo_error_logging()
    elif "performance" in sys.argv:
        demo_performance_logging()
    elif "deployment" in sys.argv:
        demo_deployment_logging()
    elif "security" in sys.argv:
        demo_security_logging()
    elif "file" in sys.argv:
        demo_file_logging()
    elif "formats" in sys.argv:
        demo_custom_log_formats()
    elif "realworld" in sys.argv:
        demo_real_world_scenario()
    elif "all" in sys.argv:
        demo_basic_logging()
        demo_different_log_levels()
        demo_json_logging()
        demo_application_logging()
        demo_error_logging()
        demo_performance_logging()
        demo_deployment_logging()
        demo_security_logging()
        demo_file_logging()
        demo_custom_log_formats()
        demo_real_world_scenario()
