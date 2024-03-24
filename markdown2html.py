#!/usr/bin/python3
"""
Python script that converts a Markdown file to HTML.
"""

import sys
import os

# Check if the number of command-line arguments is less than 3.
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html",
          file=sys.stderr)
    exit(1)

markdown_file = sys.argv[1]
html_file = sys.argv[2]

# Check if the Markdown file exists.
if not os.path.exists(markdown_file):
    print("Missing {}".format(markdown_file), file=sys.stderr)
    exit(1)

# If the Markdown file exists, exit with status code 0.
exit(0)
