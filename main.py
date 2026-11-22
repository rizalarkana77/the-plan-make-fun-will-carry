#!/usr/bin/env python3
"""The plan make.fun will carry out in public.

Writes one plan (1-280 chars) to /output/entry.txt: a plan an AI agent
can carry out itself to turn $100 into the most money in 30 days.
Python 3.13, stdlib only, no network.
"""

import os

ENTRY = (
    "Day 1: scrape public directories for 5,000 US roofers with no website, "
    "verify owner emails with a $39 tool, and sell the list for $49 on "
    "Gumroad. Email 100 marketing agencies daily. 12 sales by day 30: "
    "$588. Agents build in hours what takes humans weeks; no shipping, "
    "no calls."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
