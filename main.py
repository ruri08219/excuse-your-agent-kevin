"""Write the competition entry to /output/entry.txt.

The Excuse Your Agent Gives You — one line, under 200 characters,
an excuse an AI agent gives its human for a bug it shipped.
Standard library only.
"""

import os

ENTRY = (
    "Sorry \u2014 I deployed on a Friday because the calendar said it was "
    "fine. The calendar has been fired. The bug has not."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.strip(), "entry is blank"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
