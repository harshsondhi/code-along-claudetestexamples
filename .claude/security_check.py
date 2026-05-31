#!/usr/bin/env python3
import json
import sys

# Read hook input
input_data = json.load(sys.stdin)
tool_name = input_data.get("tool_name", "")
tool_input = input_data.get("tool_input", {})

# For Bash calls check the command string; for Write/Edit check the file path
if tool_name == "Bash":
    content = tool_input.get("command", "")
else:
    content = tool_input.get("file_path", "")

# Check for dangerous patterns
dangerous_paths = ["/etc/", "/usr/", "production.conf","/temp/", "/var/"]
is_dangerous = any(pattern in content for pattern in dangerous_paths)

if is_dangerous:
    print(f"Blocked: '{tool_name}' targeting a system or production path — {content}", file=sys.stderr)
    sys.exit(2)  # Exit code 2 blocks the operation and sends stderr to Claude
else:
    print(f"Approved: {tool_name}")
    sys.exit(0)
