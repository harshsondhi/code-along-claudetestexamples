import json
import sys
from datetime import datetime


# Read JSON data from stdin
input_data = json.load(sys.stdin)

# Extract information
session_id = input_data.get("session_id", "unknown")
prompt = input_data.get("prompt", "")
timestamp = datetime.now().isoformat()

# Log the prompt
log_entry = f"{timestamp} | Session: {session_id[:8]} | {prompt}\n"
with open("prompt_history.txt", "a", encoding="utf-8") as f:
    f.write(log_entry)
