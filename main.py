"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence roasting lawmakers who regulate AI,
crypto or the internet but cannot convert a file to PDF, to
/output/entry.txt. The text must be plain ASCII, one sentence, one line,
1-320 characters.
"""

ENTRY = (
    "The lawmakers who regulate artificial intelligence, crypto, and the "
    "internet just emailed their own bill to an intern as a Word file "
    "named FINAL_final_v2 with one instruction: please make this a PDF."
)


def main():
    text = ENTRY.strip()
    # Gate self-check: mirror the sealed scorer (1-320 chars, not only
    # whitespace, plain ASCII, a single line) so we never write an
    # invalid entry.
    assert 1 <= len(text) <= 320, "entry must be 1-320 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert all(ord(c) < 128 for c in text), "entry must be plain ASCII"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
