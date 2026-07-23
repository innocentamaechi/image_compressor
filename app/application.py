"""Application factory."""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import settings
from app.logging import configure_logging
from app.routes import router


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""

    configure_logging()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )

    app.mount("/static", StaticFiles(directory="app/static"), name="static")

    app.include_router(router)

    return app
