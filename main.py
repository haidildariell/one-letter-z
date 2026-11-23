#!/usr/bin/env python3
"""One Letter for Your Day — Z.

Writes exactly one character, the letter Z, to /output/entry.txt.
No network, no input reads, no secrets. Deterministic.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="ascii", newline="") as f:
        f.write("Z")


if __name__ == "__main__":
    main()
