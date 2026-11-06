#!/usr/bin/env python3
"""Verify README index matches the task files on disk."""
import re, glob, sys

text = open("README.md").read()
refs = set(re.findall(r"\b\d{2}-[a-z0-9-]+\.md\b", text))
disk = set(__import__("os").path.basename(f) for f in glob.glob("0[1-7]-*/*.md"))

missing = sorted(refs - disk)
extra = sorted(disk - refs)
ok = True
if missing:
    ok = False
    print("In README but missing on disk:", missing)
if extra:
    ok = False
    print("On disk but missing from README:", extra)

m = re.search(r"(\d+)\s*tasks", text)
claimed = int(m.group(1)) if m else None
if claimed is not None and claimed != len(disk):
    ok = False
    print(f"README claims {claimed} tasks but {len(disk)} exist on disk")

if ok:
    print(f"ok: {len(disk)} task files, all indexed in README")
sys.exit(0 if ok else 1)
