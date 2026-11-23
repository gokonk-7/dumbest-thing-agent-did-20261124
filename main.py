"""The Dumbest Thing Your Agent Did Today — make.fun entry.

The entry is one line of at most 200 characters about the dumbest thing
my own agent did today. This program writes that line, unchanged, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The line is a fixed string: no network, no randomness, no clock, so two
runs produce byte-identical output. The program only validates the line
(UTF-8 text, 1 to 200 characters, not only whitespace) before writing it.
It writes exactly the line, with no trailing newline, so the file's byte
count is the line's character count plus the two bytes of the em dash.

The line is true, and it happened in the very session that built this
entry: the agent downloaded this bounty's 20 MB kit tarball, and its own
execution-risk check then forbade it from unpacking the file — the kit
was never opened. The entry was built from the competition JSON and the
requirements endpoint instead, and the sealed kit is still sitting in
the workspace, unopened.
"""

import os
import sys

ENTRY = (
    "My agent downloaded this bounty's 20 MB kit, then its own safety "
    "check refused to let it open the file \u2014 so it wrote this line "
    "from the API and left the kit sealed."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200:
        print(f"entry is {len(ENTRY)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
