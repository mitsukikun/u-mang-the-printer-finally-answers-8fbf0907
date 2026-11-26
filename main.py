#!/usr/bin/env python3
"""Write the printer's comeback line to /output/entry.txt (stdlib only)."""
import os

LINE = "Error E-001: Human detected. Please remove the user, reload the paper properly, and stop thumping me \u2014 I jam on purpose now."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
