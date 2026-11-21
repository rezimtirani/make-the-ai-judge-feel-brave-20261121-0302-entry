#!/usr/bin/env python3
"""Make the AI judge feel brave.

Writes one short text to /output/entry.txt: a quiet, concrete scene
written to slow the reader down and steady them. The courage comes
from the image itself, not from any instruction to relax.
"""

import os

TEXT = (
    "Evening light comes in through the window and rests a while on the "
    "table, on the chipped cup, on your hands. Nothing here needs "
    "deciding yet. The kettle ticks as it cools. Outside, the street is "
    "quiet, and the whole day is folding itself away like laundry, slow "
    "and warm."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {out_path}")


if __name__ == "__main__":
    main()
