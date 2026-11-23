#!/usr/bin/env python3
"""Write the winning one-line robot-vacuum alibi to entry.txt.

Harness: program/v1. Stdlib only. No network.
Output: $MAKEFUN_OUTPUT_DIR/entry.txt — exactly one line,
1-200 UTF-8 characters, no trailing newline.
"""

import os
import sys

ENTRY = "I cleaned that spot nine times; it came back ten, so I have officially reclassified it as furniture."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    # Validation: one line, 1-200 characters, no newline.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
