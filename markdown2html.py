#!/usr/bin/env python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

elif not os.path.isfile(sys.argv[1]):
    print(f"Missing {sys.argv[1]}", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
