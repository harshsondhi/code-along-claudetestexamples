import json
import sys
import re

DANGEROUS_PATTERNS = [
    (r'\brm\s+.*-[a-z]*r[a-z]*f',          "recursive force delete (rm -rf)"),
    (r'\bsudo\s+rm\b',                       "sudo rm"),
    (r'\bchmod\s+777\b',                     "world-writable chmod 777"),
    (r'\bgit\s+push\s+.*--force.*\bmain\b',  "force push to main"),
    (r'\bgit\s+push\s+.*--force.*\bmaster\b',"force push to master"),
    (r'\bdrop\s+database\b',                 "DROP DATABASE"),
    (r'\btruncate\s+table\b',                "TRUNCATE TABLE"),
    (r'>\s*/dev/sd[a-z]',                    "writing directly to a disk device"),
    (r'\bmkfs\b',                            "filesystem format (mkfs)"),
    (r'\bdd\s+.*of=/dev/',                   "dd to a raw device"),
]

try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError as e:
    print(f"[HOOK ERROR]: Failed to parse stdin JSON: {e}", file=sys.stderr)
    sys.exit(0)

tool_name = input_data.get("tool_name", "")

if tool_name.lower() != "bash":
    sys.exit(0)

command = input_data.get("tool_input", {}).get("command", "").strip()

if not command:
    sys.exit(0)

for pattern, description in DANGEROUS_PATTERNS:
    if re.search(pattern, command, re.IGNORECASE):
        print(json.dumps({
            "decision": "block",
            "reason": f"Unsafe command blocked — {description}.\nCommand: {command!r}"
        }))
        sys.exit(2)

print(f"[ALLOWED]: {command!r}", file=sys.stderr)
sys.exit(0)
