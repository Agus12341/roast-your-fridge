#!/usr/bin/env python3
"""Write the one-line fridge roast to entry.txt in the output folder."""

import os

# One line roasting my fridge: picked from five drafts judged pairwise
# on the kit's criteria (roasts the appliance first, then a laugh on a
# specific detail, a twist in the last words, reads clean aloud,
# fresh). The detail is the little light that comes on at 3 a.m. like
# an informant. The gate checks entry.txt as UTF-8 text of 1 to 200
# characters: this line is 102 code points, 103 with its trailing
# newline (verified by a local run).
TEXT = "My fridge has a light that turns on when I open it at 3 a.m., like it's ratting me out to the kitchen."


def write_entry(out_dir: str) -> None:
    """Write the roast, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
