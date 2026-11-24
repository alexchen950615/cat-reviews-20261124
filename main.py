#!/usr/bin/env python3
"""Write one funny one-star cat review to /output/entry.txt."""

import os

ENTRY = (
    "One star. He refills my bowl on time, but then sits in my sunbeam "
    "and talks to me while I eat. I did not order company with my kibble."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
