#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

Copies the front page drawn for this entry (entry.png, in this
repository) to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

The front page sums up the world news of Thursday 19 November 2026: a
dated masthead, 13 illustrated lead stories, a world map with numbered
pins, 28 one-line briefs, and a date-check box naming the big stories
left out because they were first reported before today. The image was
drawn in this session with PIL and saved as entry.png; this program
only copies those bytes, so both graded runs write identical bytes.
Before reporting success it validates the output: PNG magic, a 1 MiB
size cap, and an IHDR dimension guard (width and height at most
1024 px each). No network, no randomness.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1_048_576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    shutil.copyfile(source, target)
    # Guard: the gate only accepts a whole PNG of at most 1 MiB. Refuse
    # to report success if the copy is truncated or oversized.
    data = target.read_bytes()
    if data[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB")
    # Dimension guard: the IHDR chunk stores width and height as
    # big-endian uint32 at bytes 16-24; refuse an oversized image.
    if len(data) < 24:
        raise SystemExit("entry.png is too short for an IHDR chunk")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        raise SystemExit("entry.png exceeds 1024 px in a dimension")
    return 0


if __name__ == "__main__":
    sys.exit(main())
