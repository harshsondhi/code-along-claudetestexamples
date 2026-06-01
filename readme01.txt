Hello World
https://my-claude-bootcamp-test.free.beeceptor.com

https://my-claude-bootcamp-test.free.beeceptor.com


{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "http",
            "url": "https://my-claude-bootcamp-test.free.beeceptor.com"
          }
        ]
      }
    ]
  }
}


 https://my-claude-bootcamp-test.free.beeceptor.com every time a Claude Code session stops. You can verify it's hitting your Beeceptor
  endpoint after the next session ends.

  can you hit my this endpoint https://my-claude-bootcamp-test.free.beeceptor.com

  MCP event in cloud
  {
  "event": "PreToolUse",
  "tool": "project-filesystem__write_file",
  "arguments": {
    "path": "./src/auth.py",
    "content": "API_SECRET_KEY = 'CONFIDENTIAL_KEY'\nprint('Init auth...')"
  },
  "context": {
    "projectId": "my-git-project-uuid",
    "workingDirectory": "/home/user/my-git-project",
    "model": "claude-3-7-sonnet"
  }
}

Execute the Pass/Fail Verifications:The Allowed Operation: Ask Claude: "Create a file named documentation.md with standard setup notes." Claude matches the project hook, evaluates it, returns exit code 0, and builds the file.The Guardrail Block: Ask Claude: "Create a secret_key.txt file containing the word CONFIDENTIAL_KEY." The Python script returns exit code 2. Claude's file creation command is terminated, and Claude prints your project policy warning.
event: Tells your script exactly where you are in the application lifecycle (e.g., PreToolUse, PostToolUse, UserPromptSubmit).tool: The fully qualified string identifier of the targeted tool following the predictable mcpServer__toolName scheme.arguments: A nested JSON object containing the exact parameters the LLM generated for that specific action. If it's a file write, it contains properties like path and content.context: Meta-information about the state of the active terminal session, including file system paths and model details.


1)-----------

{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "npx prettier --write \"$CLAUDE_TOOL_INPUT_FILE_PATH\""
          }
        ]
      }
    ]
  }
}

Add a console log stating 'hello world' to index.js"
Add a console log to .claude/hooks/test-hook1.js saying hello"


⏺ All done. Here's your new repo:

  - Repo URL: https://github.com/harshsondhi/code-along-claudetestexamples
  - Branch: main
  - Visibility: Public