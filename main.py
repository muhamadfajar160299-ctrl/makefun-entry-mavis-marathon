"""Write the competition entry to the output directory.

Reads entry.txt next to this file and copies its bytes verbatim to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset), so the submitted joke reaches the judge unchanged.
"""

import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_bytes(text)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        raise SystemExit(f"cannot write entry output: {exc}") from exc


if __name__ == "__main__":
    main()
