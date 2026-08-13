# FastAPI Project

A FastAPI backend for managing users and posts with PostgreSQL and JWT authentication.

## Project structure

- app/main.py: application entry point
- app/database.py: database configuration
- app/models.py: SQLAlchemy models
- app/schemas.py: Pydantic schemas
- app/oauth2.py: JWT authentication helpers
- app/utils.py: password hashing and verification
- app/routers/: API route modules for auth, users, and posts

## Requirements

- Python 3.11+
- PostgreSQL running locally
- Virtual environment

## Setup

1. Create and activate the virtual environment

   Windows CMD:

   ```bat
   python -m venv venv
   .\venv\Scripts\activate
   ```

   Windows PowerShell:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies

   ```bat
   pip install -r requirements.txt
   ```

3. Create your environment file

   ```bat
   copy .env.example .env
   ```

4. Update the values in .env if needed.

5. Run the application

   ```bat
   uvicorn app.main:app --reload
   ```

The app will be available at:

- http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

## Default endpoints

- POST /users/
- GET /users/{id}
- POST /login
- GET /posts/
- POST /posts/
- GET /posts/{id}
- PUT /posts/{id}
- DELETE /posts/{id}

## Notes

This project currently uses hardcoded values in the source code for local development. For production, move secrets and configuration to environment variables and use a safer setup.
