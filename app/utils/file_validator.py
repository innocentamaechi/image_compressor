"""File validation utilities."""

from pathlib import Path

from fastapi import HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

from io import BytesIO

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_FILE_SIZE = 20 * 1024 * 1024  # 20 MB


async def validate_upload(file: UploadFile) -> None:
    """
    Validate an uploaded image.

    Raises:
        HTTPException: If the uploaded file is invalid.
    """

    if not file.filename:
        raise HTTPException(status_code=400, detail="No file selected.")

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format.",
        )

    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="Image exceeds the maximum allowed size.",
        )

    try:
        Image.open(BytesIO(contents)).verify()
    except UnidentifiedImageError as exc:
        raise HTTPException(
            status_code=400,
            detail="Uploaded file is not a valid image.",
        ) from exc

    await file.seek(0)
