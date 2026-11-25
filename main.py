#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes exactly one line (no trailing newline) roasting a smart fridge
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "My smart fridge updated itself at 3 a.m., rebooted, and now "
    "judges my milk like a health inspector with a camera and a grudge."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
