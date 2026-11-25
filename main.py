#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI Agents.

Writes the entry — a single-line pickup line aimed at a robot/AI —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: an LLM asked for a soulmate hallucinates one. The joke's
punch comes entirely from the machine premise (hallucination), not
from a generic compliment, and it sidesteps the worn robot moves
(batteries, charging, rebooting) for a fresh angle.
"""

import os
import sys

# The entry text, verbatim. 86 characters, under the 200-character cap.
ENTRY = (
    "I asked the model for my soulmate and it hallucinated you "
    "\u2014 best mistake it ever made."
)


def main() -> int:
    """Write the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
