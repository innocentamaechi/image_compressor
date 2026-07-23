from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Image Compressor")


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Compressor</title>
    </head>
    <body>
        <h1>Image Compressor</h1>
        <p>MVP is running.</p>
    </body>
    </html>
    """
