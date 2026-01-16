FastAPI + SQLModel + PostgreSQL Setup Guide

This project demonstrates how to set up FastAPI with SQLModel, PostgreSQL, and Alembic migrations, using pyenv and virtual environments.

Prerequisites

macOS / Linux

Python managed via pyenv

PostgreSQL installed and running

Git

1. Python Version Setup (pyenv)
pyenv versions
pyenv local 3.14.2


Verify:

python --version

2. Virtual Environment Setup
python -m venv venv
source venv/bin/activate

3. Project Files Initialization
touch .env
touch .gitignore

.gitignore (minimum required)
venv/
.env
.env*
__pycache__/
*.py[cod]
.DS_Store

4. Install Dependencies
pip install fastapi
pip install "uvicorn[standard]"
pip install "fastapi[standard]"
pip install sqlmodel
pip install psycopg2-binary
pip install alembic

5. Save Dependencies
pip freeze > requirements.txt

6. Run FastAPI Application
Using Uvicorn (Recommended)
uvicorn app.main:app --reload


Application will be available at:

API → http://127.0.0.1:8000

Docs → http://127.0.0.1:8000/docs

7. Alembic Setup (Database Migrations)
7.1 Initialize Alembic

Run from project root (where main.py exists):

alembic init alembic


This creates:

alembic/
alembic.ini

7.2 Configure Alembic for SQLModel
1️⃣ Update alembic/env.py

Add the following imports at the top:

from sqlmodel import SQLModel
from app.db import engine
from app import models


Set metadata:

target_metadata = SQLModel.metadata


Ensure all models are imported, otherwise autogenerate will not work.

2️⃣ Update Database URL

Edit alembic.ini:

sqlalchemy.url = postgresql://<user>:<password>@localhost:5432/<database_name>


Example:

sqlalchemy.url = postgresql://fastapi_user:fastapi_pass@localhost:5432/library_db

7.3 Create Initial Migration
alembic revision --autogenerate -m "initial migration"


This generates a migration file inside:

alembic/versions/

7.4 Apply Migration
alembic upgrade head


This creates tables in the database.

8. (Optional) Run Using FastAPI CLI
fastapi dev main.py


⚠️ Recommended only for development/testing.

Important Notes

Do NOT use SQLModel.metadata.create_all() once Alembic is enabled

Always run Alembic commands from the folder containing alembic.ini

Never commit .env or venv to Git

Use query parameters for optional filters in routes

Let PostgreSQL auto-generate primary keys

Recommended Project Structure
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

Summary

FastAPI handles HTTP requests

SQLModel handles ORM & validation

Alembic handles schema migrations

PostgreSQL stores data

Uvicorn runs the application