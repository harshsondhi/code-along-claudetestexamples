#!/usr/bin/env python3
import json
import sys

# Use a tuple for faster, direct matching with startswith()
SAFE_PREFIXES = ('npm test', 'npm run lint', 'git status', 'ls')

def main():
    try:
        # Load and safely extract the command string
        input_data = json.load(sys.stdin)
        command = input_data.get('tool_input', {}).get('command', '').strip()
    except (json.JSONDecodeError, TypeError, AttributeError):
        # Handle malformed JSON input or missing structures gracefully
        sys.exit(1)

    # Check against safe prefixes
    if command.startswith(SAFE_PREFIXES):
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PermissionRequest",
                "decision": {"behavior": "allow"}
            }
        }
        print(json.dumps(output))
        sys.exit(0)

    # BLOCK/DENY flow for unsafe commands
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {"behavior": "block"}
        }
    }
    print(json.dumps(output))
    sys.exit(0)

if __name__ == '__main__':
    main()
