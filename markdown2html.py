#!/usr/bin/python
import sys
import os

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)
sys.exit(0)