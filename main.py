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


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)


if __name__ == "__main__":
    main()
