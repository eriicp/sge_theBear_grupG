from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User

def get_all_users(db:Session):
    sql_read = select(User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email:str, db:Session):
    db_user = User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user succesfully"}

def update_user_email(id: int, nou_email: str, db: Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    print("user:",user)
    user.email = nou_email
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"UPDATED": "Correu actualizat", "user": user}

def delete(id: int, db:Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    db.delete(user)
    db.commit()
    db.refresh(user)
    return {"Updated user succesfully"}