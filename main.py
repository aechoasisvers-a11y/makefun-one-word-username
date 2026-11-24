"""One-word entry for make.fun's "One Word, One Username, One Reward".

The brief is explicit: the entry is the entrant's own make.fun username,
one word and nothing else. The judge's first criterion is that the word
is a real make.fun username, the entrant's own handle -- and a word that
is not a genuine handle loses to any username that is one. So the only
word this program may honestly write is our own handle: "aech-oasis".

It is one token (10 characters, no spaces), memorable after one look,
and a handle its owner happily wears: Aech, at home in the OASIS.

The program writes exactly that word -- no trailing newline, no padding,
no gloss -- to /output/entry.txt, the path the kit specifies.
"""

from pathlib import Path

USERNAME = "aech-oasis"
OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the kit's gate before writing: 1-30 chars, one token.

    A word that fails this would score Valid 0 and never reach the judge,
    so refuse to write it rather than submitting an invalid entry.
    """
    if not 1 <= len(word) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(word)}")
    if len(word.split()) != 1 or word.strip() != word:
        raise ValueError("entry must be a single word with no spaces or padding")


def main() -> None:
    validate(USERNAME)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(USERNAME, encoding="utf-8")


if __name__ == "__main__":
    main()
