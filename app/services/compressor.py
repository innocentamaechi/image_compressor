"""Image compression service."""

from pathlib import Path

from PIL import Image


def compress_image(
    input_path: Path,
    output_path: Path,
    quality: int = 80,
) -> None:
    """
    Compress an image.

    Args:
        input_path: Original image.
        output_path: Destination image.
        quality: Compression quality.
    """

    with Image.open(input_path) as image:

        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        image.save(
            output_path,
            optimize=True,
            quality=quality,
        )
