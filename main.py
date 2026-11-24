#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt and prints it.
Deterministic: the haiku is a fixed string, 5-7-5 syllables, 67 chars.
"""

import os

HAIKU = "Cursor blinks at three\nthe log insists all is well\nI wrote the liar"


def validate() -> None:
    """Check the haiku is exactly the required 5-7-5, 67-character text."""
    lines = HAIKU.split("\n")
    assert len(lines) == 3, f"haiku must have 3 lines, got {len(lines)}"
    assert len(HAIKU) == 67, f"haiku must be 67 chars, got {len(HAIKU)}"
    assert lines[0] == "Cursor blinks at three"
    assert lines[1] == "the log insists all is well"
    assert lines[2] == "I wrote the liar"
    assert HAIKU.strip() != "", "haiku must not be whitespace-only"


def write_entry() -> None:
    """Write exactly the haiku to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


def main() -> None:
    validate()
    write_entry()
    print(HAIKU)


if __name__ == "__main__":
    main()


