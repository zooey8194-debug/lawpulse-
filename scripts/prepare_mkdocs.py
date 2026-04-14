from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "_site_docs"
EXCLUDED_ROOTS = {
    ".git",
    ".github",
    ".obsidian",
    ".claude",
    ".claude-design",
    ".claudian",
    "_site_docs",
    "site",
    "scripts",
    ".venv",
    "venv",
    "__pycache__",
}


def should_copy(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    parts = relative.parts

    if not parts:
        return False

    if any(part in EXCLUDED_ROOTS for part in parts):
        return False

    if any(part.startswith(".") for part in parts):
        return False

    return path.is_file() and path.suffix.lower() == ".md"


def destination_for(path: Path) -> Path:
    relative = path.relative_to(ROOT)
    if relative.name == "_INDEX.md" and len(relative.parts) == 1:
        return OUTPUT_DIR / "index.md"
    return OUTPUT_DIR / relative


def main() -> None:
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    copied_files = 0
    for path in sorted(ROOT.rglob("*.md")):
        if not should_copy(path):
            continue

        destination = destination_for(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)
        copied_files += 1

    if copied_files == 0:
        raise SystemExit("No markdown files were found to publish.")

    print(f"Prepared {copied_files} markdown files in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
