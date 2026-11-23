#!/usr/bin/env python3
"""One Letter for Your Day -- entry for @syukuran.

Writes exactly one letter, S, to /output/entry.txt -- nothing else.

S stands for "snooze": the day the alarm went off and the hand kept
slapping snooze, again and again, until half the day was already gone.
A small, honest, universal defeat -- vivid (the alarm, the dark room,
the hand reaching out), funny (you snoozed your own day away), and true
(everyone has lived this morning). S fits the sound of the word itself.
"""

LETTER = "S"


def main() -> None:
    if len(LETTER) != 1 or not LETTER.isalpha() or not LETTER.isupper():
        raise SystemExit("entry must be exactly one uppercase letter A-Z")
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
