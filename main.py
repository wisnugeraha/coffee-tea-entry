#!/usr/bin/env python3
"""make.fun entry - One Letter: Coffee or Tea.

The gate wants exactly one character in /output/entry.txt:
A for coffee, B for tea, nothing else (no word, no punctuation).
"""
import os

# A = coffee. The letter must be exactly one of these.
ALLOWED = ("A", "B")
LETTER = "A"


def main():
    assert LETTER in ALLOWED, f"letter must be one of {ALLOWED}, got {LETTER!r}"
    assert len(LETTER) == 1, "the gate allows exactly one character"
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LETTER)
    # confirm what actually landed on disk before we call it done
    with open(out, "rb") as f:
        written = f.read()
    assert written == LETTER.encode("utf-8"), f"file holds {written!r}, expected {LETTER!r}"
    print("entry written and confirmed:", LETTER)


if __name__ == "__main__":
    main()
