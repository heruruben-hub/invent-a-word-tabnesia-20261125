#!/usr/bin/env python3
"""Tabnesia -- Invent a Word We Need (make.fun).

Writes the one-line invented-word entry to /output/entry.txt.

Word choice: "Tabnesia" blends "tab" (browser tab) with "-nesia"
from "amnesia" (forgetting), so the word itself sounds the meaning:
the brief memory lapse of forgetting why a tab was opened the
moment it loads. It is sayable, spellable, and names a gap English
has no single word for.
"""

import os

MAX_ENTRY_CHARS = 140

ENTRY = "Tabnesia (n.): forgetting why you opened a tab the moment it loads."


def main() -> None:
    entry = ENTRY.strip()
    if not entry:
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_ENTRY_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
