"""The Funniest Office Joke entry.

Writes exactly one joke about office life, one short line, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints the same
line to stdout. Pure Python 3.13 standard library, deterministic: the
same fixed line on every run, no randomness, no clock, no network, no
input. The line is 20 words, 95 characters (97 bytes): a setup (five years
with no raise), a turn on the boss's platitude that loyalty is its own
reward,
and the punchline last -- asking whether loyalty pays rent.
"""

import os

JOKE = (
    "Five years, no raise \u2014 my boss said loyalty is its own reward, "
    "so I asked if loyalty pays rent."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline in the file: it holds exactly the joke, nothing
    # extra, so the judge reads one line and nothing else. The gate wants
    # UTF-8 text of 1 to 200 characters; this line is 95.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
