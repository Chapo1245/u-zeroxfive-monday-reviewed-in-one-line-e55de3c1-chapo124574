#!/usr/bin/env python3
"""Monday, Reviewed in One Line.

Entry program for make.fun's "Monday, Reviewed in One Line" bounty.
It writes exactly one line -- the funniest one-line review of my own
Monday, and nothing else -- to /output/entry.txt.

Deterministic: the same bytes on every run, no input, no network,
Python 3.13 standard library only.
"""

from pathlib import Path

REVIEW = (
    "Monday's 9 a.m. meeting could have been an email; instead it was "
    "a 90-minute hostage situation with slides."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the review as a single line to /output/entry.txt."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
