#!/usr/bin/env python3
"""make.fun entry - writes the competition text to /output/entry.txt

Entry: A
"""
import os

ENTRY_LETTER = 'A'
MAX_LEN = 1

def main():
    entry = ENTRY_LETTER
    if len(entry) > MAX_LEN:
        raise ValueError(f"Entry exceeds {MAX_LEN} char(s)")
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(entry)
    print(f"Wrote entry to {out}")

if __name__ == "__main__":
    main()
