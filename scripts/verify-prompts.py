#!/usr/bin/env python3
"""Lint the Grok prompt pack: every task file must have the 9 skeleton parts."""
import glob, re, sys

REQUIRED = ["TASK:", "GOAL:", "CONFIG:", "PROCEDURE:", "CONFIDENCE GATE:",
            "NOTION WRITE:", "RUN LOG:", "STALE-DATA POLICY:", "NO FABRICATION:",
            "APPROVAL BOUNDARY:"]

files = sorted(glob.glob("0[1-7]-*/*.md"))
bad = 0
for f in files:
    text = open(f).read()
    missing = [r for r in REQUIRED if r not in text]
    arrows = "mixed" if ("→" in text and "->" in text) else ("unicode" if "→" in text else "ascii")
    if missing or arrows == "mixed":
        bad += 1
        print(f"FAIL {f}")
        if missing:
            print("   missing:", ", ".join(missing))
        if arrows == "mixed":
            print("   mixed arrow styles")
    else:
        print(f"ok   {f} ({arrows})")

# legacy files
for f in ["lot-scout.md", "yt-content-scout.md"]:
    print(f"info {f}: legacy v1 (not checked)")

print(f"\n{len(files)} files checked, {bad} with issues")
sys.exit(1 if bad else 0)
