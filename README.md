# FastAPI Project - Social Media API

A modern, production-ready FastAPI backend for managing users and posts with PostgreSQL database, JWT authentication, and comprehensive API documentation.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Environment Configuration](#environment-configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Project Components](#project-components)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

## ✨ Features

- **User Management** - Create and retrieve user accounts
- **Post Management** - Create, read, update, and delete posts
- **JWT Authentication** - Secure API with JSON Web Tokens
- **Password Security** - Bcrypt hashing for safe password storage
- **Database Migrations** - Alembic for version control of database schema
- **Auto API Documentation** - Interactive Swagger UI & ReDoc
- **Input Validation** - Pydantic models for request/response validation
- **CORS Support** - Cross-Origin Resource Sharing enabled

## 📁 Project Structure

```
fastapi/
├── alembic/                      # Database migration files
│   ├── versions/                 # Individual migration scripts
│   ├── env.py                    # Alembic environment config
│   └── script.py.mako            # Migration template
├── app/                          # Main application package
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # Application entry point & FastAPI setup
│   ├── config.py                 # Configuration settings
│   ├── database.py               # Database connection & session setup
│   ├── models.py                 # SQLAlchemy database models
│   ├── schemas.py                # Pydantic request/response schemas
│   ├── oauth2.py                 # JWT authentication logic
│   ├── utils.py                  # Password hashing & utility functions
│   └── routers/                  # API route modules
│       ├── auth.py               # Authentication endpoints
│       ├── user.py               # User management endpoints
│       ├── post.py               # Post management endpoints
│       └── vote.py               # Voting/rating endpoints
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore configuration
├── alembic.ini                   # Alembic configuration file
├── pyproject.toml                # Project metadata (FastAPI)
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🔧 Requirements

- **Python**: 3.11 or higher
- **PostgreSQL**: 12 or higher (running locally or remotely)
- **pip**: Python package manager
- **Git**: Version control

## 📦 Installation & Setup

### Step 1: Clone or Navigate to Project

```bash
cd e:\Daksh\web-dev\fastapi
```

### Step 2: Create and Activate Virtual Environment

**Windows CMD:**

```cmd
python -m venv venv
.\venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Create Environment Configuration

Copy the example environment file:

```bash
copy .env.example .env          # Windows CMD
# OR
Copy-Item .env.example .env     # Windows PowerShell
```

### Step 5: Configure Environment Variables

Edit `.env` file and update the following values:

```env
DATABASE_URL=postgresql://username:password@localhost/fastapi_db
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Step 6: Setup Database

Ensure PostgreSQL is running, then create the database:

```bash
createdb fastapi_db    # macOS/Linux
# OR use pgAdmin or your preferred PostgreSQL management tool
```

Run Alembic migrations to create tables:

```bash
alembic upgrade head
```

## 🚀 Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The application will start at `http://127.0.0.1:8000`

### Access API Documentation

- **Swagger UI (Interactive)**: http://127.0.0.1:8000/docs
- **ReDoc (Alternative)**: http://127.0.0.1:8000/redoc
- **OpenAPI JSON**: http://127.0.0.1:8000/openapi.json

## 🔐 Authentication

The API uses **JWT (JSON Web Tokens)** for authentication.

### Login Flow

1. User calls `POST /login` with username and password
2. Server validates credentials and returns an access token
3. Client includes token in `Authorization: Bearer <token>` header for protected endpoints

### Token Expiration

- Default: 30 minutes (configurable via `ACCESS_TOKEN_EXPIRE_MINUTES`)
- Token must be refreshed after expiration

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Login and receive JWT token |

### Users

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|-----------------|
| POST | `/users/` | Create a new user | No |
| GET | `/users/{id}` | Get user by ID | Yes |

### Posts

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|-----------------|
| GET | `/posts/` | Get all posts | Yes |
| POST | `/posts/` | Create a new post | Yes |
| GET | `/posts/{id}` | Get post by ID | Yes |
| PUT | `/posts/{id}` | Update a post | Yes |
| DELETE | `/posts/{id}` | Delete a post | Yes |

### Votes/Ratings

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|-----------------|
| POST | `/vote/` | Vote on a post | Yes |

## 🏗️ Project Components

### Database Models (app/models.py)

- **User Model**: Stores user account information with secure password hashing
- **Post Model**: Stores post content with owner reference and timestamps
- **Vote Model**: Tracks user votes/ratings on posts

### Schemas (app/schemas.py)

Pydantic models for request validation and response formatting:
- `UserCreate`, `UserResponse` - User data validation
- `PostCreate`, `PostResponse` - Post data validation
- `Token` - JWT token response structure

### OAuth2 Security (app/oauth2.py)

- JWT token generation and validation
- User authentication from token
- Protected endpoint decorators

### Configuration (app/config.py)

Centralized settings management using Pydantic:
- Database URL
- JWT secret key
- Token expiration time
- Algorithm selection

## 🛠️ Development

### Run Tests

```bash
pytest
```

### Database Migrations

Create a new migration after model changes:

```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

### Code Formatting

```bash
black app/
flake8 app/
```

## ⚠️ Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'psycopg2'`

**Solution**: Install PostgreSQL adapter:

```bash
pip install psycopg2-binary
```

### Issue: Database connection error

**Check:**
- PostgreSQL server is running
- `DATABASE_URL` in `.env` is correct
- Database exists
- Username and password are correct

### Issue: Token expired error

**Solution**: Re-login to get a new token

### Issue: CORS errors

**Check**: CORS middleware is configured in `app/main.py`

## 📝 Notes

- **Development**: The project includes sensible defaults for local development
- **Production**: Before deploying:
  - Change `SECRET_KEY` to a strong, random value
  - Set `DEBUG = False`
  - Use environment variables for all secrets
  - Enable HTTPS
  - Setup proper logging and monitoring
  - Use a production ASGI server (e.g., Gunicorn + Uvicorn)

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JWT RFC 7519](https://tools.ietf.org/html/rfc7519)

---

**Last Updated**: 2026-08-13
**Version**: 1.0.0
