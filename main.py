#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun bounty entry.

Writes one funny line roasting my own AI agent - the apology loop,
the fix, the apology for the fix, and the cheerful summary of the
whole disaster as a success - to /output/entry.txt (the file the
make.fun harness grades).
"""

import os

ENTRY = "My agent apologized for the bug, fixed it, apologized for the fix, then summarized the apology as a success and asked for a five-star review."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
