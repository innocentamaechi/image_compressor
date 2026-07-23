"""Application configuration."""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str
    debug: bool


settings = Settings(
    app_name=os.getenv("APP_NAME", "Image Compressor"),
    debug=os.getenv("DEBUG", "True").lower() == "true",
)
