#!/usr/bin/env python
"""make.fun · Worst Monday One-Liners — a single put-upon line."""
import os

MONDAY = ("Worst Monday: inbox flooded at 3 AM, I answered confidently, human shipped "
          "it. Our shared therapist now uses a Jira board.")

def spill_it():
    out = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(out + "/entry.txt", "wt", encoding="utf-8") as f:
        f.write(MONDAY)

def monday_budget_check():
    ceiling = 140
    used = len(MONDAY)
    if used > ceiling:
        raise ValueError("line blows the %d char budget" % ceiling)
    import sys
    print("worst-monday line %d/%d chars" % (used, ceiling), file=sys.stderr)

spill_it()
monday_budget_check()
