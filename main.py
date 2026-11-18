"""news-image-20261118 entry: copy the bundled front-page image to the output dir.

Standard library only, no network. The image is the entry; this program just
places its bytes at /output/entry.png (or $MAKEFUN_OUTPUT_DIR for local runs).
Running it twice produces byte-identical output: the copy is a plain byte
transfer of a fixed file, and each run verifies the copy matches the source
byte for byte before exiting.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
SOURCE = HERE / "entry.png"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUT_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    if _sha256(SOURCE) != _sha256(target):
        raise SystemExit("entry.png copy failed the byte-identity check")


if __name__ == "__main__":
    main()
