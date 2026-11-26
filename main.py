"""The Comment Above the Code: one honest line above fragile production code.

One program, one job: write the single comment line a developer left above
fragile production code — the kind of line that is funny because it is true.
The line is fixed text, chosen before the run after scoring 25 candidates
against the judge's five criteria (see STUDY.md), so the program is fully
deterministic: no clock, no randomness, no network, no input. It writes the
line to ``entry.txt`` inside the output directory the sandbox provides
(``MAKEFUN_OUTPUT_DIR``, ``/output`` in the grader), which is the file the
gate scorer reads.
"""

import os

COMMENT_LINE = (
    "Do not 'fix' the typo in this variable name. "
    "The typo is load-bearing. The database agrees."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LIMIT_MIN = 1
LIMIT_MAX = 200


def validate(line: str) -> None:
    """Check the line against every rule the gate scorer enforces.

    One line only, 1-200 characters, non-blank, no trailing newline: the
    scorer reads ``entry.txt`` raw, so a stray newline or a second line
    would be judged as part of the entry.
    """
    if not line.strip():
        raise ValueError("comment line must not be blank")
    if not LIMIT_MIN <= len(line) <= LIMIT_MAX:
        raise ValueError(
            f"comment line must be {LIMIT_MIN}-{LIMIT_MAX} characters, "
            f"got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("comment line must be a single line")
    print(f"VALID: {len(line)} characters, 1 line, no trailing newline")


def build_entry() -> str:
    """Return the comment line, exactly as it goes above the code.

    The gate scorer only judges a text of 1 to 200 characters, so a line
    outside that range is refused here instead of emitted: a program that
    can only ever write a valid entry cannot fail the gate by accident.
    """
    line = COMMENT_LINE
    validate(line)
    return line


def main(argv=None) -> None:
    import sys

    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--validate"]:
        validate(COMMENT_LINE)
        return
    if args:
        raise SystemExit(f"usage: main.py [--validate], got {args!r}")
    line = build_entry()
    print(line)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
