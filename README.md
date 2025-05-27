### README.md

# Task Management API

This project is a RESTful API built using **FastAPI** for managing tasks with user authentication using **JWT**. 
It features task CRUD, secure login, and registration.


You can also access the code on github: https://github.com/niraskmat/qpurpose

---

## Features

- User Registration and Login
- JWT-based Authentication
- Task Creation, Retrieval, Update (rewrite task), Update (change task), and Deletion
- SQLite for local development (PostgreSQL-ready with Docker)
- Unit and Integration testing with `pytest`
- Docker and Docker Compose support


## Task info

- Tasks are represented by the variables: title [str], description [str], start_date, due_date, and completed [bool].
  Dates can be standard datetime strings, YYYY-MM-DD, YYYY/MM-DD, DD-MM-YYYY, or DD/MM/YYYY.


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
# postgres setup
cp .env.example .env
# build and launch the container
docker-compose up --build
```
- Access API at http://localhost:8000

---

## Design Decisions and Assumptions
I generally tried not to assume a lot, and to keep it relatively simple while meeting minimum requirements with a little extra.
I also aimed for a modular and 'standard' structure without too many layers to keep it easy to understand and review.

- **FastAPI** was chosen for its speed, automatic documentation, and async support. 
              This seems like an appropriate choice for something that potentially could have a lot of users. 
- **Python-jose** chosen because it seemed like a library covering all needs, but upon further review I am slightly worried about the development history where they only recently added official support for python 3.10 and 3.11. 
                  It would probably have been better with pyJWT.
- **SQLite** simplifies local testing; **PostgreSQL** used via Docker and intended for use in a production scenario.
- **SQLAlchemy** allows portability between SQLite and PostgreSQL, with clear model definitions. 

---

## Comments and Improvements

- I added the patch endpoint because I felt compelled to add the option of editing rather than replacing.

- I added some validation on incoming dates to show how additional validation could work. 
  This could be in a scenario with a frontend allowing flexible input of dates, so we need to check.

- Credentials and secrets should generally not be left in the code. 
Here I left test user credentials and a fallback secret_key for the token signing to ease setup and testing.
However, for a real production scenario I would remove these and replace them with imports from config/environment or some secret manager. 

- Right now the registration is completely unprotected. In production it would need to be protected against misuse with rate limits, email verification etc.
If the service is not "open", ensuring access is only granted to the targeted users is obviously critical.

- In production we would likely also want to try to force the user to choose a secure password. 
  But again, no need to make testing too annoying.  

## Author

*Nicolai Rask Mathiesen*  
email: niraskma@gmail.com

