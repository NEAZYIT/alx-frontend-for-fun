#!/usr/bin/python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>",
          file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Process Markdown to HTML conversion here
# This script currently doesn't perform any conversion, only checks for
# arguments and file existence

sys.exit(0)
