Perfect. Before writing any code, I'd define the project in **phases**. This keeps the project focused and prevents feature creep.

# Phase 0 — Foundation (Current Phase)

Goal: Build a secure, maintainable project skeleton.

Deliverables:

* ✅ Repository created
* ✅ `README.md`
* ✅ Dependency policy
* ⬜ Project structure
* ⬜ Virtual environment
* ⬜ `requirements.txt`
* ⬜ `.gitignore`
* ⬜ `LICENSE` (optional)
* ⬜ `.env.example`
* ⬜ Basic FastAPI application
* ⬜ Homepage

No image compression yet.

---

# Phase 1 — MVP

Goal: Compress one image.

Features

* Upload image
* Validate image
* Compress image
* Download image
* Delete temporary file
* Handle errors gracefully

---

# Phase 2 — Better UX

* Drag and Drop
* Compression slider
* Before/After size
* Preview
* Progress bar
* Better UI

---

# Phase 3 — More Image Tools

Instead of creating another project:

```
Image Tools

├── Compress
├── Resize
├── Convert
├── Crop
├── Rotate
├── Watermark
```

---

# Phase 4 — AI Features

Later.

---

# Architecture

I want the project to stay modular from day one.

```
image-compressor/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── services/
│   ├── utils/
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── temp/
│       ├── uploads/
│       └── compressed/
│
├── tests/
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── main.py
```

Notice something.

There is already a **tests** folder.

Even if we don't write tests today, we know where they belong.

---

# The First Dependency Discussion

According to the dependency policy, we should **not install anything until we justify it.**

## Dependency 1 — FastAPI

**Official Source**

* PyPI: [https://pypi.org/project/fastapi/](https://pypi.org/project/fastapi/)
* GitHub: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

**Purpose**

FastAPI provides the web framework that receives uploaded images, processes requests, and returns responses.

**Why it's needed**

The Python Standard Library (`http.server`, `wsgiref`) can serve web pages but lacks modern routing, request validation, file upload handling, and a good developer experience. FastAPI provides these in a lightweight, well-maintained package.

**Alternatives considered**

* Flask
* Django
* Python Standard Library

**Decision**

Choose **FastAPI** because it is lightweight, modular, and aligns with the project's architecture.

---

## Dependency 2 — Uvicorn

**Official Source**

* PyPI: [https://pypi.org/project/uvicorn/](https://pypi.org/project/uvicorn/)
* GitHub: [https://github.com/encode/uvicorn](https://github.com/encode/uvicorn)

**Purpose**

ASGI server used to run the FastAPI application.

**Why it's needed**

FastAPI requires an ASGI server. Uvicorn is the recommended implementation.

**Alternatives**

* Hypercorn
* Daphne

**Decision**

Use Uvicorn.

---

## Dependency 3 — Pillow

**Official Source**

* PyPI: [https://pypi.org/project/pillow/](https://pypi.org/project/pillow/)
* GitHub: [https://github.com/python-pillow/Pillow](https://github.com/python-pillow/Pillow)

**Purpose**

Image loading, validation, compression, resizing, and format conversion.

**Why it's needed**

The Python Standard Library does not provide image processing capabilities. Pillow is the de facto standard for basic image manipulation.

**Alternatives**

* OpenCV (much larger; designed for computer vision)
* pyvips (very fast but more complex)
* imageio (good for I/O but not a full replacement)

**Decision**

Use Pillow for the MVP because it is mature, widely used, and sufficient for image compression.

---

# Initial `requirements.txt`

After approving the above, the initial dependencies would be:

```text
fastapi
uvicorn
pillow
```

No additional packages should be added without going through the same review process.

---

## Next Step

We'll begin by creating the project skeleton, setting up the virtual environment, and adding the minimal FastAPI application that serves a simple homepage. Once that foundation is stable, we'll implement image upload and compression one step at a time, keeping every addition documented and justified.

