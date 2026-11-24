#!/usr/bin/env python3
"""make.fun entry - One Letter: Coffee or Tea.

The gate wants exactly one character in /output/entry.txt:
A for coffee, B for tea, nothing else.
"""
import os

LETTER = "A"


def main():
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LETTER)
    print("entry:", LETTER)


if __name__ == "__main__":
    main()
