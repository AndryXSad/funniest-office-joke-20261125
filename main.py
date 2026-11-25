"""Funniest office joke entry.

Writes one single-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke was picked by a local pairwise tournament over 20 original
candidates, judged against the bounty brief: a real joke with a setup
and a turn, built on something anyone who has worked in an office
recognises, with a surprise turn and the punchline last.
"""

import os

JOKE = (
    "The office plant died, so facilities replaced it with a "
    "laminated photo of a plant and a ticket to water it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = JOKE.strip()
    # The gate reads one line of 1-200 characters: enforce it here so a
    # bad edit fails loudly in our own run instead of at grading time.
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} chars, gate needs 1-200")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
