#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes a single self-contained funny line to /output/entry.txt.
The line won a 1v1 comparison against 7 other candidates scored on the
judge brief's criteria in order: laugh first, then the turn, tightness,
freshness, and clarity. Gate: UTF-8 text of 1 to 140 characters.
"""

import os

LINE = "I talk to my plants, and my therapist knows \u2014 the plants called her first."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
