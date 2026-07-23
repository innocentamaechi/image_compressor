"""Application routes."""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.views import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Render the application homepage."""

    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )
