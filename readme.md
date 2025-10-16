# User Profile API (with Cat Facts)

A FastAPI project that exposes a simple endpoint returning a user profile plus a random cat fact.

## What this repo contains

- `main.py` — FastAPI application and CORS setup.
- `routers.py` — API routes (prefix `/me`).
- `services.py` — business logic: reads environment variables and fetches a cat fact from an external API.
- `schema.py` — Pydantic models used for responses.
- `middleware.py` — request id + timing middleware.
- `logger.py` — logger helper (used across modules).
- `requirements.txt` — Python dependencies.
- `test_app.py` — simple pytest tests using FastAPI TestClient.

## Tech Stack
- Python 3.10+
- FastAPI
- Uvicorn
- HTTPX
- Python-dotenv
- Pytest

## Quick setup 
1. Clone the Repository
``` bash 
git clone https://github.com/Mr-kings042/HNG_dynamic_profile_endpoint.git
cd HNG_dynamic_profile_endpoint
```
2. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies from `requirements.txt`:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (or set environment variables in your shell). Example `.env`:

```text
# Example .env
USER_EMAIL=okohkings042@gmail.com
USER_NAME=Okoh Kingsley
USER_STACK=Python(FastAPI, Django) | JavaScript(React, Node) | HTML | CSS
# The external cat facts API URL used by the service
CAT_FACT_URL=https://catfact.ninja/fact
```

The app uses `python-dotenv` to load `.env` automatically when starting.

## Environment variables

- `USER_EMAIL` — user email to return in the profile (required)
- `USER_NAME` — user full name to return in the profile (required)
- `USER_STACK` — a short description of the developer stack (required)
- `CAT_FACT_URL` — full URL for the cat-fact endpoint (defaults not provided by code; set to `https://catfact.ninja/fact` recommended)

If any required variable is missing the Pydantic model validation or the response may fail; make sure they are set before running.

## Run the app locally (development)

Start with uvicorn (from project root):

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open your browser or use a request tool to visit:

- API root: http://127.0.0.1:8000/
- Swagger UI (interactive docs): http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## API Documentation

endpoint is JSON and use HTTP/HTTPS.

1) GET /

- Description: Simple welcome endpoint.
- Response: 200
- Example response:

```json
{ "message": "Welcome to the User Profile API and CatFActs" }
```

2) GET /me/

- Description: Returns a user profile (from environment variables) and a random cat fact fetched from `CAT_FACT_URL`.
- Response model: `UserProfileResponse` (see `schema.py`)

Response JSON shape:

```json
{
	"status": "success",
	"user": {
		"name": "Okoh Kingsley",
		"email": "okohkings042@gmail.com",
		"stack": "Python(FastAPI, Django) | JavaScript(React, Node) | HTML | CSS"
	},
	"timestamp": "2025-10-16T12:34:56.789012+00:00",
	"fact": "Cats have five toes on their front paws, but only four toes on their back paws."
}
```

Errors:
- If the cat facts API fails or the service raises an error, the endpoint returns HTTP 500 with `{"detail": "Internal Server Error"}`.

Example request (PowerShell):

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/me/ -Method GET
```

Or using curl (if available):

```powershell
curl http://127.0.0.1:8000/me/
```

## Running tests

Run the pytest suite:

```powershell
pytest -q
```

The repo includes basic tests in `test_app.py` that assert the root endpoint and the `/me/` route behavior. Tests mock a failure to ensure the endpoint returns a 500 on internal errors.

## Dependencies

Dependencies are listed in `requirements.txt`. Key packages used:

- fastapi
- uvicorn
- httpx
- python-dotenv
- pydantic
- pytest (for tests)

Install them with `pip install -r requirements.txt` (see setup steps above).

## Troubleshooting

- "await allowed only within async function" — this happens when `await` is used in non-async functions. The project uses async endpoints and `httpx.AsyncClient`, make sure you do not change route functions to sync.
- "GET is not defined" — CORS middleware expects method names as strings; the project uses `allow_methods=["GET"]`. If you see a NameError, ensure the code uses quoted method names.
- If you get errors about missing environment variables, create a `.env` with the variables shown above or export them in your shell before starting.

## Next steps / Suggestions

- For production: lock dependency versions with a lockfile, configure stricter CORS rules, and consider a small health-check endpoint and circuit-breaking/retries for the external cat-fact call.
- Add logging of external API latency and gracefully degrade to a cached/default fact if external service is down.

## Contact
- okohkings042@gmail.com

