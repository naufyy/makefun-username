"""The Handle in One Word.

Criterion 1 of the judge brief says any word that is not a genuine make.fun
handle loses to every genuine handle. So the only entry that can win is the
entrant's own handle, sent as one word: naufyy.
"""
from pathlib import Path

HANDLE = "naufyy"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(HANDLE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
