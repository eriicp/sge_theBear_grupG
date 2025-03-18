from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
from models.User import User

import os

app = FastAPI()

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model= list[dict])
def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.post("/users/", response_model=dict)
def create_user(name: str,email:str, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, db)
    return result


@app.put("/users/", response_model=dict)
def update_users(id: int, name: str, db:Session = Depends(get_db)):
    statement = db.select(User).where(User.id == id)
    result = db.exec(statement)
    user = result.one()

    user.name = "Oriol"
    db.add(user)
    db.commit()
    return("Updated user sucsefully")


