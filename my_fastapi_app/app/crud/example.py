from sqlalchemy.orm import Session
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
