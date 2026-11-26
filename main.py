#!/usr/bin/env python3
"""Rejected Olympic Sports - make.fun entry.

Writes the one-line entry to /output/entry.txt (pure stdlib).
"""

import os

ENTRY = "Competitive small talk: two strangers share a lift; the first to mention the weather is disqualified."
# Chosen per winner analysis (see 20261126-rejected-olympic-ANALISA.md): fresh concept
# outside the saturated queueing/napping/apologizing clusters, broadcaster-plausible
# sport name + setup, disqualification twist landing at the end of the line.

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate: single line, 1-200 chars, not whitespace-only."""
    if not text or text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be one non-blank line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry too long: {len(text)} > {MAX_CHARS}")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
