### README.md

# Task Management API

This project is a RESTful API built using **FastAPI** for managing tasks with user authentication using **JWT**. 
It features task CRUD, secure login, and registration.

---

## Features

- User Registration and Login
- JWT-based Authentication
- Task Creation, Retrieval, Update (rewrite task), Update (change task), and Deletion
- SQLite for local development (PostgreSQL-ready with Docker)
- Unit and Integration Testing with `pytest`
- Docker and Docker Compose support


## Task info

- Tasks are represented by the variables: title [str], description [str], start_date, due_date, and completed [bool].
  Dates can be datetime, YYYY-MM-DD, YYYY/MM-DD, DD-MM-YYYY, DD/MM/YYYY.


---

## Technologies

- Python 3.11+
- FastAPI
- SQLAlchemy
- SQLite / PostgreSQL
- Pydantic
- JWT (`python-jose`)
- Pytest
- Docker

---

## Installation

### 🚀 Local Development

1. **Clone the repo**
```bash
git clone https://github.com/niraskmat/qpurpose.git
cd qpurpose
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
uvicorn main:app --reload
```

4. **Access API Docs**
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

---

## API Endpoints

### 🧑 User
- `POST /register`: Register new user
- `POST /login`: Login and get JWT token

### ✅ Task
- `GET /tasks`: List all user tasks
- `POST /tasks`: Create a task
- `PUT /tasks/{task_id}`: Update task - rewrite all variables
- `DELETE /tasks/{task_id}`: Delete task
- `PATCH /tasks/{task_id}`: Update task - change given variables only 

Use the `Authorization: Bearer <token>` header for task routes.

---

## Running Tests

```bash
export PYTHONPATH=.  # only needed in local environment, not docker container 
pytest
```

---

### 🐳 Docker Setup

```bash
docker-compose up --build
```
- Access API at http://localhost:8000

---

## Design Decisions

- **FastAPI** was chosen for its speed, documentation, and async support.
- **JWT** enables stateless authentication.
- **SQLite** simplifies local testing; **PostgreSQL** used via Docker.

---

## Author

*Nicolai Rask Mathiesen*  
email: niraskma@gmail.com

