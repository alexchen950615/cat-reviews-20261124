#!/usr/bin/env python3
"""Write one funny one-star cat review to /output/entry.txt."""

import os

ENTRY = (
    "One star. He refills my bowl on time, but then sits in my sunbeam "
    "and talks to me while I eat. I did not order company with my kibble."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
