# Placement Tracker API

A backend application built using **FastAPI, Python, SQLite, and SQLAlchemy** to manage job and internship applications. It provides RESTful APIs for creating, viewing, updating, and deleting placement records, with JWT-based authentication and user-specific data access.

## Features

- User registration and login
- Secure password hashing
- JWT access-token authentication
- Create, read, update, and delete placement applications
- User-specific application management
- SQLite database integration
- SQLAlchemy ORM for database operations
- Interactive API documentation using Swagger UI

## Tech Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** OAuth2 and JWT
- **Password Hashing:** pwdlib (Argon2)
- **API Documentation:** Swagger UI

## Project Structure

```text
placement_tracker/
│
├── main.py          # FastAPI application and API endpoints
├── auth.py          # Password hashing and JWT authentication
├── database.py      # Database connection and configuration
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic request and response schemas
├── crud.py          # Database CRUD operations
│
├── placement.db     # SQLite database (generated locally)
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd placement_tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy "pwdlib[argon2]" "PyJWT[crypto]" python-multipart
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

Visit:

```text
http://127.0.0.1:8000/docs
```

Use the interactive Swagger interface to explore and test the API endpoints.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate a user and generate an access token |
| GET | `/profile` | Retrieve the authenticated user's profile |

### Placement Applications

| Method | Endpoint | Description |
|---|---|---|
| POST | `/applications` | Create a new application |
| GET | `/applications` | Retrieve the logged-in user's applications |
| GET | `/applications/{app_id}` | Retrieve an application by ID |
| PUT | `/applications/{app_id}` | Update an application |
| PATCH | `/applications/{app_id}` | Partially update an application |
| DELETE | `/applications/{app_id}` | Delete an application |

## Authentication Flow

1. Register a user using `/register`.
2. Authenticate using `/login`.
3. Obtain a JWT access token.
4. Authorize requests through Swagger UI.
5. Access protected endpoints using the bearer token.
6. Each user can access and manage only their own applications.

## Database

The application uses SQLite with SQLAlchemy ORM.

Two primary database models are implemented:

- **User:** Stores user information and hashed passwords.
- **Application:** Stores company, role, application status, and the associated user ID.

Applications are associated with users through a foreign-key relationship.

## Future Improvements

- React-based frontend
- Search and filtering functionality
- Deployment to a cloud platform
- Automated API testing
- Docker containerization

## Learning Outcomes

Through this project, I gained practical experience with:

- Building REST APIs using FastAPI
- Database integration using SQLAlchemy
- Implementing CRUD operations
- User authentication and authorization
- JWT-based security
- Password hashing
- Testing APIs using Swagger UI

---

**Developed as a hands-on backend development project.**
