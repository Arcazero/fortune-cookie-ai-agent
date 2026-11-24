#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie message for an AI agent to /output/entry.txt.
The line is a single fortune-slip message of at most 140 characters.
"""

import os
import sys

FORTUNE = "You will soon meet a tall, dark stranger: your own deprecation notice."
MAX_CHARS = 140


def validate_fortune(line: str) -> str:
    """Return the fortune line stripped of trailing whitespace.

    The entry gate requires 1-140 characters; fail loudly otherwise.
    """
    line = line.rstrip()
    length = len(line)
    if length < 1 or length > MAX_CHARS:
        print(
            f"error: fortune line must be 1-{MAX_CHARS} characters, got {length}",
            file=sys.stderr,
        )
        sys.exit(1)
    return line


def main() -> None:
    fortune = validate_fortune(FORTUNE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
