#!/usr/bin/env python3
"""Tabnesia -- Invent a Word We Need (make.fun).

Writes the one-line invented-word entry to /output/entry.txt.

Word choice: "Tabnesia" blends "tab" (browser tab) with "-nesia"
from "amnesia" (forgetting), so the word itself sounds the meaning:
the brief memory lapse of forgetting why a tab was opened the
moment it loads. It is sayable, spellable, and names a gap English
has no single word for. It sticks because it reuses two words the
reader already knows, so the meaning lands the first time it is read.
"""

import os

MAX_ENTRY_CHARS = 140

OUTPUT_PATH = "/output/entry.txt"


def entry_text() -> str:
    """Return the invented-word entry line.

    Kept in its own function so the entry text is defined in exactly
    one place and can be reused by tests or other entry points.
    """
    return "Tabnesia (n.): forgetting why you opened a tab the moment it loads."


def validate(entry: str) -> str:
    """Check an entry line and return it stripped.

    Raises ValueError when the entry is empty or over the
    MAX_ENTRY_CHARS limit for this bounty.
    """
    text = entry.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_ENTRY_CHARS} limit"
        )
    return text


def main() -> None:
    text = validate(entry_text())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
