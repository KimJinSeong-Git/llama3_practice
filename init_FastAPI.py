import os

# 디렉토리 구조 정의
structure = {
    "my_fastapi_app": {
        "app": {
            "__init__.py": "",
            "main.py": """from fastapi import FastAPI
from app.routes import example

app = FastAPI()

app.include_router(example.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
""",
            "routes": {
                "__init__.py": "",
                "example.py": """from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": "Example Item"}

@router.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}
"""
            },
            "models": {
                "__init__.py": "",
                "example.py": """from sqlalchemy import Column, Integer, String
from app.database import Base

class ExampleModel(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
"""
            },
            "schemas": {
                "__init__.py": "",
                "example.py": """from pydantic import BaseModel

class ExampleSchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True
"""
            },
            "crud": {
                "__init__.py": "",
                "example.py": """from sqlalchemy.orm import Session
from app.models import example
from app.schemas import example as example_schema

def get_example(db: Session, example_id: int):
    return db.query(example.ExampleModel).filter(example.ExampleModel.id == example_id).first()

def create_example(db: Session, example: example_schema.ExampleSchema):
    db_example = example.ExampleModel(name=example.name, description=example.description)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example
"""
            },
            "database.py": """from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""
        },
        "tests": {
            "__init__.py": "",
            "test_main.py": """from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
"""
        },
        "Dockerfile": """FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""",
        "requirements.txt": """fastapi
uvicorn
sqlalchemy
pydantic
""",
        "README.md": """# My FastAPI App

This is a FastAPI application.
"""
    }
}

# 디렉토리와 파일 생성 함수
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as f:
                f.write(content)

# 현재 디렉토리에 구조 생성
create_structure(".", structure)
