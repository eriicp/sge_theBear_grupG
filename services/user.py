from schema.users_sch import users_schema
from sqlmodel import Session, select
from models.User import User
from sqlmodel import select, Session


def get_all_users(db:Session):
    sql_read = select (User)
    users = db.exec(sql_read).all()
    return users_schema(users)

def add_new_user(name: str, email: str, db: Session):
    db_user = User(nom=name, email=email)  # Use 'nom' instead of 'name'
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"Created user successfully"}

def update_user_email(id: int, nou_email: str, db: Session):
    statement = select(User).where(User.id == id)
    results = db.exec(statement)
    user = results.one()
    user.email = nou_email
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"Updated bien"}