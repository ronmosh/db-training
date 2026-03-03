# DB Training Project

Welcome to the DB Training Project! This repository provides a training environment configured with PostgreSQL, Python, FastAPI, and Alembic. It features a layered architecture (Controller -> Service -> Repository) and includes practical exercises for developers to strengthen their database and API skills.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or Docker Engine (for running PostgreSQL)
- Python 3.10+
- `pip` (Python package installer)

## Setup Instructions

### 1. Launch the Database

Start the PostgreSQL database using Docker Compose:

```bash
docker-compose up -d
```
*This exposes a Postgres instance on `localhost:5432` with user `myuser`, password `mypassword`, and database name `training_db`.*

### 2. Configure Python Environment

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Initialize the Database Schema

Apply the Alembic migrations to create the initial tables (`authors` and `books`):

```bash
alembic upgrade head
```

### 4. Run the API Server

Start the FastAPI development server:

```bash
cd src
uvicorn main:app --reload
```
*The API will be available at `http://localhost:8000`.*
*Interactive documentation (Swagger UI) is available at `http://localhost:8000/docs`.*

## Exercises

Check out the `training_tasks.md` file located in the root directory for a series of bug fixes, feature implementations, and advanced database challenges to complete!
