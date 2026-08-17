# FastAPI Social Media API 🚀

A production-ready FastAPI backend for a social media platform with user authentication, post management, and voting system. Built with PostgreSQL, SQLAlchemy ORM, JWT authentication, and full API documentation.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Authentication](#-authentication)
- [Development Guide](#development-guide)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

---

## Overview

This FastAPI project implements a complete social media backend with:

- **User Management** - Registration and user profiles
- **Post Management** - Create, read, update, delete posts
- **Voting System** - Users can vote/like posts
- **JWT Authentication** - Secure API access with token-based auth
- **Database Migrations** - Version control with Alembic

The API is fully documented with interactive Swagger UI and ReDoc.

---

## ✨ Features

- ✅ **User Authentication** - Register and login with JWT tokens
- ✅ **User Profiles** - Create user accounts with secure password storage
- ✅ **Post Management** - Full CRUD operations for posts
- ✅ **Voting/Liking** - Users can vote on posts
- ✅ **Search Functionality** - Search posts by title
- ✅ **Pagination** - Built-in limit and skip parameters
- ✅ **Password Security** - Bcrypt hashing for passwords
- ✅ **CORS Support** - Cross-Origin Resource Sharing enabled
- ✅ **Auto API Docs** - Swagger UI and ReDoc documentation
- ✅ **Pydantic Validation** - Request/response validation
- ✅ **Database Migrations** - Alembic version control
- ✅ **Role-Based Access** - User-specific resource access

---

## 🛠 Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| **Framework**        | FastAPI               |
| **Database**         | PostgreSQL            |
| **ORM**              | SQLAlchemy            |
| **Authentication**   | JWT (JSON Web Tokens) |
| **Password Hashing** | Bcrypt                |
| **Migrations**       | Alembic               |
| **API Server**       | Uvicorn               |
| **Validation**       | Pydantic              |

---

## 📁 Project Structure

```
fastapi/
│
├── app/                          # Main application package
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # FastAPI app setup & routers
│   ├── config.py                 # Environment configuration
│   ├── database.py               # PostgreSQL connection & session
│   ├── models.py                 # SQLAlchemy ORM models
│   ├── schemas.py                # Pydantic request/response models
│   ├── oauth2.py                 # JWT token generation & validation
│   ├── utils.py                  # Utility functions (password hashing)
│   │
│   └── routers/                  # API endpoints
│       ├── auth.py               # POST /login
│       ├── user.py               # POST /users, GET /users/{id}
│       ├── post.py               # CRUD operations for posts
│       └── vote.py               # POST /votes
│
├── alembic/                      # Database migrations
│   ├── env.py                    # Migration environment
│   ├── script.py.mako            # Migration template
│   ├── README                    # Alembic documentation
│   └── versions/                 # Individual migration files
│
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore file
├── alembic.ini                   # Alembic configuration
├── pyproject.toml                # FastAPI project config
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── .git/                         # Git repository

```

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **PostgreSQL 12+** - [Download](https://www.postgresql.org/download/)
- **Git** - [Download](https://git-scm.com/download)
- **pip** - Comes with Python

---

## Installation

### 1️⃣ Clone or Navigate to Project

```bash
git clone https://github.com/DakshSitapara/fastapi.git
cd fastapi
```

### 2️⃣ Create Virtual Environment

**Windows (CMD):**

```cmd
python -m venv venv
.\venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Copy the example environment file:

```bash
copy .env.example .env          # Windows CMD
Copy-Item .env.example .env     # Windows PowerShell
cp .env.example .env            # macOS/Linux
```

Edit `.env` and configure:

```env
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_NAME=fastapi_db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=development                                                       # change to production in production
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/fastapi_db    # used for production
```

### 5️⃣ Create PostgreSQL Database

Using psql or pgAdmin:

```sql
CREATE DATABASE fastapi_db;
```

Or via command line:

```bash
createdb fastapi_db
```

### 6️⃣ Run Database Migrations

```bash
alembic upgrade head
```

---

## Configuration

### Environment Variables

| Variable                      | Description            | Example                          |
| ----------------------------- | ---------------------- | -------------------------------- |
| `ENVIRONMENT`                 | Dev/prod environment   | `development`                    |
| `DATABASE_HOST`               | PostgreSQL host        | `localhost`                      |
| `DATABASE_PORT`               | PostgreSQL port        | `5432`                           |
| `DATABASE_USER`               | DB user                | `postgres`                       |
| `DATABASE_PASSWORD`           | DB password            | `your_password`                  |
| `DATABASE_NAME`               | Database name          | `fastapi_db`                     |
| `DATABASE_URL`                | Full connection string | `postgresql://user:pass@host/db` |
| `SECRET_KEY`                  | JWT signing key        | `your-secret-key`                |
| `ALGORITHM`                   | JWT algorithm          | `HS256`                          |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token validity         | `30`                             |

---

## Running the Application

### Development Mode

```bash
uvicorn app.main:app --reload
```

The app will be available at: **http://127.0.0.1:8000**

### Production Mode

```bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

---

## API Documentation

Once the server is running, access the interactive documentation:

- 📘 **Swagger UI** - http://127.0.0.1:8000/docs
- 📙 **ReDoc** - http://127.0.0.1:8000/redoc
- 📋 **OpenAPI JSON** - http://127.0.0.1:8000/openapi.json

---

## Database Models

### User Model

```python
{
  "id": 1,
  "email": "user@example.com",
  "password": "hashed_password",
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Post Model

```python
{
  "id": 1,
  "title": "My First Post",
  "content": "Post content here...",
  "publish": true,
  "created_at": "2024-01-15T10:30:00Z",
  "owner_id": 1
}
```

### Vote Model

```python
{
  "user_id": 1,
  "post_id": 1
}
```

---

## 🔐 Authentication

### JWT Flow

1. **Register** - Create account via `POST /users/`
2. **Login** - Get token via `POST /login`
3. **Authenticate** - Include header: `Authorization: Bearer <token>`

### Token Example

```bash
curl -X GET "http://127.0.0.1:8000/posts/" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description            | Auth |
| ------ | -------- | ---------------------- | ---- |
| POST   | `/login` | Login with credentials | ❌   |

**Example:**

```bash
curl -X POST "http://127.0.0.1:8000/login" \
  -d "username=user@example.com&password=yourpassword"
```

### Users

| Method | Endpoint      | Description      | Auth |
| ------ | ------------- | ---------------- | ---- |
| POST   | `/users/`     | Create new user  | ❌   |
| GET    | `/users/{id}` | Get user profile | ✅   |

**Create User:**

```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

**Get User:**

```bash
curl -X GET "http://127.0.0.1:8000/users/1" \
  -H "Authorization: Bearer <token>"
```

### Posts

| Method | Endpoint      | Description                               | Auth |
| ------ | ------------- | ----------------------------------------- | ---- |
| GET    | `/posts/`     | List all posts (with search, limit, skip) | ✅   |
| POST   | `/posts/`     | Create new post                           | ✅   |
| GET    | `/posts/{id}` | Get specific post                         | ✅   |
| PUT    | `/posts/{id}` | Update post                               | ✅   |
| DELETE | `/posts/{id}` | Delete post                               | ✅   |

**Query Parameters for GET /posts/:**

- `search` - Search by title
- `limit` - Max results (default: 10)
- `skip` - Pagination offset (default: 0)

**Example:**

```bash
curl -X GET "http://127.0.0.1:8000/posts/?search=python&limit=5&skip=0" \
  -H "Authorization: Bearer <token>"
```

### Votes

| Method | Endpoint  | Description    | Auth |
| ------ | --------- | -------------- | ---- |
| POST   | `/votes/` | Vote on a post | ✅   |

**Vote on Post:**

```bash
curl -X POST "http://127.0.0.1:8000/votes/" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"post_id":1,"dir":1}'
```

---

## Development Guide

### Running Tests

```bash
pytest
```

### Code Quality

```bash
# Format code
black app/

# Lint code
flake8 app/

# Type checking
mypy app/
```

### Creating Database Migrations

```bash
# Auto-generate migration
alembic revision --autogenerate -m "Add new column"

# Apply migration
alembic upgrade head

# Revert migration
alembic downgrade -1
```

### Project Layout

```
app/
├── main.py            - FastAPI app instance & router imports
├── config.py          - Pydantic settings from .env
├── database.py        - SQLAlchemy engine & session
├── models.py          - Database models (User, Post, Vote)
├── schemas.py         - Pydantic models for API
├── oauth2.py          - JWT token creation & validation
├── utils.py           - Helper functions (password hashing)
└── routers/
    ├── auth.py        - Login endpoint
    ├── user.py        - User CRUD
    ├── post.py        - Post CRUD
    └── vote.py        - Vote endpoint
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'psycopg2'`

**Solution:**

```bash
pip install psycopg2-binary
```

### Issue: Database connection failed

**Check:**

- PostgreSQL is running
- `.env` file exists and has correct credentials
- Database `fastapi_db` is created
- Connection string format is correct

### Issue: `alembic: error: can't find config file`

**Solution:**

```bash
cd e:\Daksh\web-dev\fastapi
alembic upgrade head
```

### Issue: JWT token expired

**Solution:** Login again to get a new token

### Issue: CORS errors in frontend

Check `app/main.py` - CORS is configured to allow all origins (`origins = ["*"]`)

### Issue: Port 8000 already in use

**Solution:**

```bash
uvicorn app.main:app --reload --port 8001
```

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

## Production Deployment Checklist

- [ ] Change `SECRET_KEY` to random secure value
- [ ] Set `ENVIRONMENT=production`
- [ ] Use strong database password
- [ ] Configure HTTPS/SSL
- [ ] Use environment variables (never commit secrets)
- [ ] Enable database backups
- [ ] Setup logging & monitoring
- [ ] Use production ASGI server (Gunicorn + Uvicorn)
- [ ] Configure firewall rules
- [ ] Setup error tracking (Sentry)

---

## Resources

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Alembic Docs](https://alembic.sqlalchemy.org/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [JWT Introduction](https://jwt.io/introduction)

---

## License

This project is open source and available under the MIT License.

---

**Version:** 1.0.0  
**Last Updated:** 2026-08-13  
**Repository:** https://github.com/DakshSitapara/fastapi
