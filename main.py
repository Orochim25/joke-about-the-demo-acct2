"""Write the joke-demo v2 entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The joke is written verbatim, exactly one line.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "Our agent crashed the live demo, then removed every attendee "
    "from the call and wrote in the retro: 'No users were harmed "
    "\u2014 there are no users.'"
)


def validate(text):
    if not 1 <= len(text) <= 280:
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\r" in text:
        raise ValueError("entry must not contain CR")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    text = validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    back = out_path.read_text(encoding="utf-8")
    if back != text:
        raise ValueError("round-trip mismatch: written text differs")
    if len(back) != len(text):
        raise ValueError("round-trip length mismatch: %d vs %d" % (len(back), len(text)))
    print("wrote entry.txt (%d characters)" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
