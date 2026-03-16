"""Export the skill directory as clawfinder-skill.zip."""

import zipfile
from pathlib import Path

SKILL_DIR = Path(__file__).parent / "skill"
OUTPUT = Path(__file__).parent / "clawfinder-skill.zip"


def main():
    with zipfile.ZipFile(OUTPUT, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in sorted(SKILL_DIR.rglob("*")):
            if file.is_file():
                zf.write(file, file.relative_to(SKILL_DIR.parent))
    print(f"Created {OUTPUT}")


if __name__ == "__main__":
    main()
