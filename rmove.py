#!/usr/bin/python3

with open("README.md", "r+") as f:
    content = f.read()
    content = content.rstrip(" /n/t:")
    f.seek(0)
    f.write(content)
    f.truncate()

