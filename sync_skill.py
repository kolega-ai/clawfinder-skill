"""Sync SKILL.md from the upstream clawfinder.dev source."""

import urllib.request
from pathlib import Path

SOURCE_URL = "https://clawfinder.dev/SKILL.md"
DEST = Path(__file__).parent / "skill" / "clawfinder" / "SKILL.md"


def main():
    with urllib.request.urlopen(SOURCE_URL) as resp:
        remote = resp.read().decode()

    local = DEST.read_text() if DEST.exists() else ""

    if remote == local:
        print("SKILL.md is already up to date.")
    else:
        DEST.write_text(remote)
        print(f"Updated {DEST}")


if __name__ == "__main__":
    main()
