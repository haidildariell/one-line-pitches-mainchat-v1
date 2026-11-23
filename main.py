#!/usr/bin/env python3
"""Entry program for the make.fun bounty "A Day of One-Line Pitches"
(u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

Writes a single-sentence pitch to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR if set, otherwise /output). Standard library only.
"""

import os

SENTENCE = (
    "You've told me about that app idea a dozen times now \u2014 you don't "
    "know a single line of code, and that's fine, because an AI agent on "
    "make.fun can build it from your plain words while you watch your "
    "dream turn real."
)

ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_dir() -> str:
    """Resolve the output directory: MAKEFUN_OUTPUT_DIR wins, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def write_entry(text: str, directory: str) -> str:
    """Write text to entry.txt inside directory; return the file path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def main() -> None:
    write_entry(SENTENCE, output_dir())


if __name__ == "__main__":
    main()
