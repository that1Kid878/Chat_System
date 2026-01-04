from Backend.App.Models.user_schema import User_Model
from Backend.App.Core.exceptions import (
    Missing_Parameters,
    Invalid_Parameters,
    Integrity_Error_Handler,
)
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID


def Get_User(
    db: Session, user_id: UUID = None, username: str = None
) -> User_Model | None:
    if user_id and username is None:
        raise Missing_Parameters()
    if user_id:
        User = db.query(User_Model).filter(User_Model.user_id == user_id).first()
    elif username:
        User = db.query(User_Model).filter(User_Model.username == username).first()

    return User


def Create_User(db: Session, User: User_Model):
    try:
        db.add(User)
        db.commit()
        db.refresh(User)
    except IntegrityError as error:
        pg_error = error.orig
        pg_code = getattr(pg_error, "pgcode")
        raise Integrity_Error_Handler(pg_code)


def Delete_User(db: Session, user_id: UUID = None, username: str = None):
    User = Get_User(db, user_id, username)
    if User:
        db.delete(User)
        db.commit()
    else:
        raise Invalid_Parameters()
