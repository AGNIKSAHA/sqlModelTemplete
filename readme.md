pyenv versions
pyenv local 3.14.2
python -m venv venv 
source venv/bin/activate
 touch .env  
touch .gitignore 
pip install fastapi
pip install "uvicorn[standard]"
 pip install "fastapi[standard]"
pip install sqlmodel    
pip install psycopg2-binary
pip install alembic
pip freeze > requirements.txtcx
uvicorn app.main:app --reload

#For alembric setup
pip install alembic                                               
alembic init alembic
    Add     {
              1.  “Import sqlmodel” inside  script.py.mako
                    
              2. add all models and changes inside env.py  
                    “ from sqlmodel import SQLModel”
                    “ from models import Book,Author”
               Change “ target_metadata = SQLModel.metadata"
           3.  Use own db url inside alembic.ini  where sqlalchemy.url
                Present           
      }
alembic revision --autogenerate -m "initial migration"
alembic upgrade head                                  



(Optional)
fastapi dev main.py

