#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (three lines, 5-7-5 syllables,
at most 200 characters) as plain text to entry.txt.

Standard library only, no network, fully deterministic: the same
bytes are written on every run.
"""

import os

HAIKU = (
    "Red log line at dawn,\n"
    "the trace ends where I began\n"
    "the error was me."
)

# Syllable counts, counted by hand:
#   Line 1: Red(1) log(1) line(1) at(1) dawn(1) = 5
#   Line 2: the(1) trace(1) ends(1) where(1) I(1) be-gan(2) = 7
#   Line 3: the(1) er-ror(2) was(1) me(1) = 5
# Total: 17 syllables, 68 characters (see WORKING-NOTES.md).


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
