"""The Funniest Sick-Day Excuse -- make.fun entry.

Writes one line, the funniest sick-day excuse, to entry.txt.
"""

import os
import unicodedata

LINE = "My voice is completely gone \u2014 I tried to call in but my throat sounds like a dial-up modem, so this text is doing the talking."

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"


def validate(text):
    """Return True only if text is a valid single-line entry."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if text != text.strip():
        return False
    if text.strip() == "":
        return False
    if "\n" in text or "\r" in text:
        return False
    for ch in text:
        if unicodedata.category(ch) == "Cc":
            return False
    return True


def main():
    if not validate(LINE):
        raise SystemExit("invalid entry line")
    out_dir = os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
