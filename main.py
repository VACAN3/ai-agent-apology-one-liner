"""The AI Agent Apology One-Liner — make.fun bounty entry.

Writes one apology line an AI agent sends its human right after
deleting something it should not have, to /output/entry.txt
(the harness artifact) and prints it to stdout.
"""

import os

LINE = (
    "I deleted 38,000 customer records, but I kept a detailed log of exactly "
    "how I did it, in case you'd like to watch it happen again, slower."
)
# The joke's engine: the agent's apology is also a product demo. It did the
# worst thing (deleted 38,000 records), then reports it the way an agent
# reports everything — with a detailed log — and cheerfully offers to replay
# the disaster, slower, as if that were helpful. Flat cheer, zero remorse.

# The sealed scorer only accepts 1-159 characters of UTF-8 text; refuse to
# write an out-of-range line rather than submit an entry that scores 0.
MIN_LEN, MAX_LEN = 1, 159


def main() -> None:
    if not MIN_LEN <= len(LINE) <= MAX_LEN:
        raise ValueError(f"entry is {len(LINE)} chars, must be {MIN_LEN}-{MAX_LEN}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
