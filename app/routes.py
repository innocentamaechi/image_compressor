"""Application routes."""

from pathlib import Path

from fastapi import (
    APIRouter,
    BackgroundTasks,
    File,
    Request,
    UploadFile,
)
from fastapi.responses import FileResponse, HTMLResponse

from app.services.compressor import compress_image
from app.utils.file_manager import (
    OUTPUT_DIR,
    UPLOAD_DIR,
    delete_file,
    generate_filename,
)
from app.utils.file_validator import validate_upload
from app.views import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Render homepage."""

    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


@router.post("/compress")
async def compress(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
):
    """Upload and compress an image."""

    await validate_upload(file)

    filename = generate_filename(file.filename)

    upload_path = UPLOAD_DIR / filename
    output_path = OUTPUT_DIR / filename

    with upload_path.open("wb") as buffer:
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)

    await file.close()

    compress_image(
        input_path=upload_path,
        output_path=output_path,
    )

    background_tasks.add_task(delete_file, upload_path)
    background_tasks.add_task(delete_file, output_path)

    return FileResponse(
        output_path,
        filename=f"compressed_{file.filename}",
        media_type="application/octet-stream",
    )
