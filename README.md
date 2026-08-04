# FastAPI Issue Tracker

A minimal issue-tracking REST API built with FastAPI. This project demonstrates a small, file-backed issue tracker with endpoints to create, read, update, and delete issues. It's suitable as a learning example, a starting point for a small service, or a template for building more advanced trackers.

## Features

- CRUD API for issues (create, list, retrieve, update, delete)
- File-based storage using `data/issues.json` for simplicity
- Lightweight middleware example in `app/middleware/timer.py` that logs request timing
- Clear project structure for learning and extension

## Tech stack

- Python 3.10+ (or compatible)
- FastAPI
- Uvicorn (ASGI server)

## Getting started

Prerequisites: Python 3.10+ and pip.

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app locally with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000 and interactive docs at http://127.0.0.1:8000/docs

## API Endpoints

The app exposes a simple set of endpoints for managing issues. Example routes (confirm exact paths in [app/routes/issues.py](app/routes/issues.py)):

- GET `/issues` — list all issues
- GET `/issues/{id}` — retrieve a single issue by id
- POST `/issues` — create a new issue (JSON body)
- PUT `/issues/{id}` — update an existing issue (JSON body)
- DELETE `/issues/{id}` — delete an issue by id

Example `curl` to create an issue:

```bash
curl -X POST http://127.0.0.1:8000/issues \
	-H "Content-Type: application/json" \
	-d '{"title": "Bug: login fails", "description": "Steps to reproduce...", "status": "open"}'
```

Example `curl` to list issues:

```bash
curl http://127.0.0.1:8000/issues
```

Adjust host/port if you run Uvicorn on a different interface.

## Data storage

Issues are persisted in [data/issues.json](data/issues.json). This simple JSON file is used for demonstration and local development only. For production, replace the storage implementation in `app/storage.py` with a proper database-backed solution.

## Project structure

- `main.py` — app entrypoint that creates the FastAPI `app` and mounts routes
- `app/routes/issues.py` — issue-related route handlers
- `app/schemas.py` — Pydantic models / request and response schemas
- `app/storage.py` — simple file-backed storage abstraction used by the routes
- `app/middleware/timer.py` — example middleware that logs request duration
- `data/issues.json` — sample data file used by the storage layer

See the individual files for implementation details and extend as needed.

## Development notes

- To change storage behavior, modify `app/storage.py`. Switching to a DB (SQLite, Postgres) will require updating storage functions and migrations.
- Middleware is defined in `app/middleware/timer.py` and registered in `main.py` — useful example for request instrumentation.

## Tests

This repository does not include automated tests. For production-quality code add unit tests for `app/storage.py`, route handlers in `app/routes/issues.py`, and schema validation in `app/schemas.py`.

## Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repo and create a feature branch
2. Implement your changes and add tests
3. Open a pull request describing the change

Please follow Python best practices and keep changes focused.

## License

This project has no license specified. Add a `LICENSE` file or change this section to indicate the repository license.

---
