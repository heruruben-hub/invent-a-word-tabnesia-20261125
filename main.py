#!/usr/bin/env python3
"""Tabnesia -- Invent a Word We Need (make.fun).

Writes the one-line invented-word entry to /output/entry.txt.
"""

import os

ENTRY = "Tabnesia (n.): forgetting why you opened a tab the moment it loads."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
