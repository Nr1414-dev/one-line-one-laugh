#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to /output/entry.txt.
The line won a 1v1 comparison against 7 other candidates scored on the
judge brief's criteria in order: laugh first, then the turn, tightness,
freshness, and clarity. Gate: UTF-8 text of 1 to 140 characters.
"""

import os

LINE = "I talk to my plants, and my therapist knows \u2014 the plants called her first."

# Gate from competition.yaml: /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, not only white space.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 140


def validate(line: str) -> str:
    """Reject anything the sealed gate scorer would refuse."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only white space")
    if not GATE_MIN_CHARS <= len(line) <= GATE_MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, gate allows "
            f"{GATE_MIN_CHARS}-{GATE_MAX_CHARS}"
        )
    line.encode("utf-8")
    return line


def main() -> None:
    text = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
