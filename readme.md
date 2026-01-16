# FastAPI + SQLModel + PostgreSQL Setup Guide

This project demonstrates how to set up **FastAPI** with **SQLModel**, **PostgreSQL**, and **Alembic migrations**, using **pyenv** and **virtual environments**.

---

## Prerequisites

- macOS / Linux
- Python managed via **pyenv**
- PostgreSQL installed and running
- Git

---

## 1. Python Version Setup (pyenv)

```bash
pyenv versions
pyenv local 3.14.2
```

Verify:

```bash
python --version
```

---

## 2. Virtual Environment Setup

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Project Files Initialization

```bash
touch .env
touch .gitignore
```

### `.gitignore` (minimum required)

```gitignore
venv/
.env
.env*
__pycache__/
*.py[cod]
.DS_Store
```

---

## 4. Install Dependencies

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install "fastapi[standard]"
pip install sqlmodel
pip install psycopg2-binary
pip install alembic
```

---

## 5. Save Dependencies

```bash
pip freeze > requirements.txt
```

---

## 6. Run FastAPI Application

### Using Uvicorn (Recommended)

```bash
uvicorn app.main:app --reload
```

Application URLs:

- API → http://127.0.0.1:8000
- Docs → http://127.0.0.1:8000/docs

---

## 7. Alembic Setup (Database Migrations)

### 7.1 Initialize Alembic

Run from the **project root**:

```bash
alembic init alembic
```

---

### 7.2 Configure Alembic for SQLModel

Edit `alembic/env.py`:

```python
from sqlmodel import SQLModel
from app.db import engine
from app import models

target_metadata = SQLModel.metadata
```

---

### 7.3 Configure Database URL

Edit `alembic.ini`:

```ini
sqlalchemy.url = postgresql://<user>:<password>@localhost:5432/<database_name>
```

---

### 7.4 Create Initial Migration

```bash
alembic revision --autogenerate -m "initial migration"
```

---

### 7.5 Apply Migration

```bash
alembic upgrade head
```

---

## 8. Optional: Run Using FastAPI CLI

```bash
fastapi dev main.py
```

---

## Important Notes

- Do NOT use `SQLModel.metadata.create_all()` once Alembic is enabled
- Always run Alembic commands from the folder containing `alembic.ini`
- Never commit `.env` or `venv` to Git
- Let PostgreSQL auto-generate primary keys

---

## Recommended Project Structure

```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   └── routes/
├── alembic/
├── alembic.ini
├── .env
├── .gitignore
├── requirements.txt
└── venv/
```

---

## Summary

- FastAPI handles HTTP requests
- SQLModel handles ORM & validation
- Alembic handles schema migrations
- PostgreSQL stores data
- Uvicorn runs the application
