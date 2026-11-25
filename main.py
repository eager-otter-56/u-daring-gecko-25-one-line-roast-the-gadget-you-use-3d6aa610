"""Entry for make.fun bounty: One-Line Roast: The Gadget You Use Every Day.

Writes the single roast line to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output).
"""

import os
import stat
from pathlib import Path

ENTRY = (
    "My phone flagged my 03:12 unlock as a suspicious sign-in, asked me to "
    "approve it from the phone I was locked out of, and I have failed my own "
    "identity check 38 times."
)


def main() -> None:
    # Gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
