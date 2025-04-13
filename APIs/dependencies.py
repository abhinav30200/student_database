from sqlalchemy.orm import Session
from APIs.databaseconnection import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
