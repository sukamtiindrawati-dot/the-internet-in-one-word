#!/usr/bin/env python3
"""The Internet in One Word - entry for @sukamtiindrawati-dot.

Writes a single word to /output/entry.txt.
"""

import os

WORD = "Roulette"  # Every click is a spin: random, addictive, and you never know what you get.


def validate(word):
    """Gate: one word, 1-30 UTF-8 chars, no whitespace."""
    assert isinstance(word, str) and 1 <= len(word) <= 30
    assert word == word.strip() and not any(ch.isspace() for ch in word)
    return word


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
