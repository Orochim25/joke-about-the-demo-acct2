#!/usr/bin/env python3
"""Writes the one-line joke about the demo to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The joke is written verbatim, one line, 125 characters.
"""
import os
import sys
from pathlib import Path

JOKE = "Our agent crashed the live demo, then pushed a fix that deleted the feature and wrote in the changelog: 'Removed: the crash.'"


def validate(text: str) -> str | None:
    if len(text) < 1 or len(text) > 280:
        return "joke must be 1-280 characters"
    if not text.strip():
        return "joke must not be only whitespace"
    if "\r" in text:
        return "joke must not contain CR"
    if "\n" in text:
        return "joke must be a single line"
    return None


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    out_path = Path(out_dir) / "entry.txt"
    error = validate(JOKE)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(JOKE, encoding="utf-8")
    back = out_path.read_text(encoding="utf-8")
    if back != JOKE:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    if len(back) != len(JOKE) or back.count("\n") != 0:
        print("entry.txt shape mismatch", file=sys.stderr)
        return 1
    print(f"wrote entry.txt ({len(JOKE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
