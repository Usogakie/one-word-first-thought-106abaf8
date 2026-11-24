#!/usr/bin/env python3
"""One Word, First Thought -- make.fun entry.

Writes a single word, the first that came to mind, to entry.txt.
The word is "syzygy": the alignment of three celestial bodies.
It is surprising (three y's, rarely seen), vivid (an eclipse line-up
you can picture at once), and carries a spark of wit in its look and
sound -- chosen, not generic.
"""

import os

WORD = "syzygy"


def main() -> None:
    # The gate allows UTF-8 text of 1 to 24 characters, not only
    # whitespace, and the task wants exactly one word: check our own
    # output before writing it, so a bad word can never be submitted.
    assert WORD and len(WORD) <= 24 and WORD.split() == [WORD]
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
