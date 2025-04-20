#!/usr/bin/env python3
import sys
import os

if __name__ == "__main__":
    # Check if we have fewer than 2 arguments after the script name
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Success: nothing to print, just exit 0
    sys.exit(0)
