import json
import sys
import argparse
import datetime
from pathlib import Path

# Script lives at .claude/hooks/backup-transcript.py → project root is two levels up
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
DEBUG_LOG = SCRIPT_DIR / "backup-transcript-debug.log"


def log(msg: str) -> None:
    with open(DEBUG_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {msg}\n")


def main():
    parser = argparse.ArgumentParser(description="Backup Claude transcripts before compaction.")
    parser.add_argument("--reason", choices=["manual", "auto"], required=True)
    args = parser.parse_args()

    log(f"Hook fired -- reason={args.reason}, cwd={Path.cwd()}")

    # Claude Code passes hook data via stdin as JSON; transcript_path points to the session file
    hook_input = {}
    raw = ""
    try:
        raw = sys.stdin.read()
        hook_input = json.loads(raw)
    except (json.JSONDecodeError, OSError) as e:
        log(f"stdin parse error: {e}  raw={raw[:200]!r}")

    log(f"hook_input keys: {list(hook_input.keys())}")

    transcript_path = hook_input.get("transcript_path")
    log(f"transcript_path={transcript_path!r}")

    if not transcript_path:
        log("No transcript_path in hook input — aborting")
        sys.exit(0)

    tp = Path(transcript_path)
    if not tp.exists():
        log(f"transcript_path does not exist: {tp}")
        sys.exit(0)

    with open(tp, "r", encoding="utf-8") as f:
        transcript_content = f.read()

    if not transcript_content:
        log("transcript file is empty — aborting")
        sys.exit(0)

    # Use absolute path so backup lands in the project dir regardless of cwd
    backup_dir = PROJECT_ROOT / ".claude" / "backups" / "transcripts"
    backup_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"transcript_{args.reason}_{timestamp}.txt"
    filepath = backup_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"--- BACKUP REASON: {args.reason.upper()} ---\n")
        f.write(f"--- TIMESTAMP: {datetime.datetime.now().isoformat()} ---\n\n")
        f.write(transcript_content)

    log(f"Backup saved to {filepath}")


if __name__ == "__main__":
    main()
