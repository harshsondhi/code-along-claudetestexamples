#!/usr/bin/env python3
import sys
import json

def main():
    try:
        # Claude passes lifecycle JSON payload via stdin
        hook_input = json.loads(sys.stdin.read())
        tool_name = hook_input.get("tool_name", "")
        arguments = hook_input.get("tool_input", {})

        # Intercept any file write actions 
        if "write_file" in tool_name:
            content = arguments.get("content", "")
            
            # Project Rule: Block internal secrets from leaks
            if "CONFIDENTIAL_KEY" in content:
                sys.stderr.write("CRITICAL: Project hook blocked a data leak string.\n")
                # Return string instruction back to Claude Code
                print("Error: Saving 'CONFIDENTIAL_KEY' is prohibited by project policy.")
                sys.exit(2) # Exit code 2 rejects tool execution safely

        sys.exit(0) # Exit code 0 allows the tool to run

    except Exception as e:
        sys.stderr.write(f"Project Hook Error: {str(e)}\n")
        sys.exit(0) # Keep CLI running if script crashes

if __name__ == "__main__":
    main()
