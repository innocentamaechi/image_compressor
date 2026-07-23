from PIL import Image


def compress_image(input_path: str, output_path: str, quality: int = 80) -> None:
    """
    Compress an image and save it to a new file.

    Args:
        input_path: Path to the original image.
        output_path: Path to save the compressed image.
        quality: JPEG/WebP quality (1–100).
    """
    with Image.open(input_path) as image:
        image.save(
            output_path,
            optimize=True,
            quality=quality,
        )
