"""File management utilities."""

from pathlib import Path
from uuid import uuid4

UPLOAD_DIR = Path("app/temp/uploads")
OUTPUT_DIR = Path("app/temp/compressed")

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_filename(filename: str) -> str:
    """Generate a unique filename while preserving the extension."""

    extension = Path(filename).suffix.lower()

    return f"{uuid4().hex}{extension}"


def delete_file(path: Path) -> None:
    """Delete a file if it exists."""

    if path.exits():
        path.unlink()
