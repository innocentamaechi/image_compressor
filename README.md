# Image Compressor

## 1. Project Overview

### Goal

Build a lightweight online image compressor using Python.

This project intentionally avoids unnecessary complexity.

The MVP should:

- Compress uploaded images
- Allow download
- Require no database
- Require no user accounts
- Require no external APIs
- Be easy to deploy
- Be easy to maintain
- Be easy to extend

---

## 2. Vision

The Image Compressor is the first tool in a future collection of image-processing utilities.

Possible future tools:

- Image Compression
- Resize
- Crop
- Rotate
- Convert Formats
- Watermark
- Background Removal
- OCR
- AI Enhancement
- Super Resolution
- Face Detection

The architecture should support these without major rewrites.

---

## 3. Architecture

Frontend

- HTML
- CSS
- JavaScript

Backend

- FastAPI
- Pillow

Flow

User

↓

Upload Image

↓

Validate

↓

Compress

↓

Return Download

No database.

No authentication.

No cloud storage.

---

## 4. Folder Structure

app/

    api/
    services/
    utils/
    core/
    templates/
    static/
    temp/

main.py

requirements.txt

README.md

---

## 5. Database

Current Status

No database.

Reason

The application is completely stateless.

Every request is processed independently.

Temporary files are deleted automatically.

Possible future database use:

- Analytics
- User accounts
- Processing history
- Billing
- API keys

---

## 6. API

POST /compress

Input

multipart/form-data

Output

Compressed image

Future endpoints

POST /resize

POST /crop

POST /convert

POST /watermark

POST /enhance

---

## 7. Coding Rules

General

- Keep functions small.
- Avoid duplicate logic.
- Prefer composition over large classes.
- One responsibility per module.

Naming

snake_case

PascalCase for classes

Constants in UPPER_CASE

Avoid magic numbers.

Configuration belongs inside config.py.

---

## 8. Design Decisions

### Why FastAPI?

Simple.

Fast.

Easy to document.

Future API support.

---

### Why Pillow?

Lightweight.

Reliable.

Large community.

Easy to replace later.

---

### Why no database?

Not needed.

Avoid unnecessary complexity.

---

### Why temporary storage?

Allows download.

Keeps memory usage low.

Easy cleanup.

---

## 9. File Map

main.py

Application entry point.

api/

HTTP routes.

services/

Business logic.

utils/

Validation helpers.

core/

Configuration.

templates/

HTML pages.

static/

CSS

JavaScript

Images

temp/

Temporary uploads.

Temporary compressed files.

---

## 10. TODO

MVP

- Upload image
- Compress image
- Download image
- Validation
- Error handling
- Temporary cleanup

Version 2

- Batch compression
- Resize
- Convert
- Drag and drop
- Progress bar

Version 3

- Background removal
- OCR
- AI enhancement
- REST API
- Docker

---

## 11. Progress

Planning

✅ Complete

Architecture

✅ Complete

Folder Structure

✅ Complete

Development

⬜ Not Started

Testing

⬜ Not Started

Deployment

⬜ Not Started

---

## 12. Future AI Integration

Current

Frontend

↓

FastAPI

↓

Pillow

Future

Frontend

↓

FastAPI

↓

Image Processor Interface

↓

Pillow

or

OpenCV

or

AI Model

or

Cloud AI

Changing the processing engine should never require changing the frontend.

---

## 13. Guiding Principles

Keep it simple.

Build only what is needed.

Avoid premature optimization.

Design for extension.

Keep business logic separate from routing.

Write code that another developer can understand quickly.

The project should remain lightweight while allowing significant future expansion.


## Project Philosophy

This project is guided by a set of principles that prioritize simplicity, security, maintainability, and long-term sustainability.

### Core Principles

- Start with the smallest useful product.
- Avoid unnecessary dependencies.
- Keep the project modular.
- Every feature should be replaceable without affecting the rest of the system.
- Optimize for maintainability over cleverness.
- Prefer the Python Standard Library whenever possible.
- Prefer well-established and actively maintained third-party packages when external dependencies are required.
- Document architectural decisions so future contributors understand **why**, not just **what**.
- Build for long-term maintainability rather than short-term convenience.

---

## Dependency Policy

Security is a first-class concern for this project.

Every external dependency increases the project's attack surface. Therefore, dependencies must be introduced deliberately and only when they provide significant value that cannot reasonably be achieved with the Python Standard Library.

### Rules

- Do **not** add any dependency unless it is explicitly approved for the project.
- Every new dependency must be reviewed before installation.
- Always check whether the required functionality already exists in the Python Standard Library.
- Prefer mature, widely adopted, actively maintained libraries with a strong security reputation.
- Avoid adding dependencies for small or trivial tasks.
- Keep the dependency list as small as possible.
- Remove unused dependencies as the project evolves.
- Pin dependency versions whenever appropriate to improve reproducibility.

---

## Dependency Review Process

Before introducing any package, document the following:

### Package Name

Example:

```
Pillow
```

### Official Source

Example:

```
https://pypi.org/project/Pillow/
https://github.com/python-pillow/Pillow
```

### Purpose

Explain exactly what problem the package solves.

Example:

> Provides image loading, manipulation, compression, resizing, and format conversion.

### Why It Is Needed

Explain why the functionality cannot reasonably be implemented using the Python Standard Library.

### Alternatives Considered

List possible alternatives and explain why they were not chosen.

Example:

- OpenCV
- pyvips
- imageio

### Maintenance Status

Document:

- Is it actively maintained?
- Is it widely used?
- Is documentation available?
- Are security issues regularly addressed?

### Security Notes

Check for:

- Known security advisories
- Suspicious installation steps
- Unnecessary permissions
- Large dependency chains
- Untrusted maintainers

---

## AI Contributor Rules

When an AI assistant contributes to this project, it must follow these rules:

- Never introduce a dependency without explicitly mentioning it.
- Explain what the dependency does.
- Provide its official source (PyPI and, where available, its GitHub repository).
- Explain why it is required.
- Explain why it is preferred over alternatives.
- List any transitive dependencies if they are significant.
- Never assume a dependency is acceptable simply because it is popular.
- Prefer the Python Standard Library whenever practical.
- If a feature can be implemented without an external package, that approach should be preferred unless there is a clear reason not to.

---

## Approved Dependencies

This section serves as the project's dependency inventory.

| Package | Purpose | Official Source | Status |
|----------|---------|-----------------|--------|
| *(None yet)* | | | |

Every dependency added to this table should include a short justification in the commit or pull request that introduced it.

---

## Security Goal

The goal is not to eliminate third-party packages entirely, but to ensure that every dependency is:

- Necessary
- Trusted
- Understood
- Documented
- Maintainable

No dependency should exist in this project simply because it was convenient or automatically suggested by an AI assistant.
