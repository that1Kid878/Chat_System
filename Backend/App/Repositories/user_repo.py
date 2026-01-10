from Backend.App.Models.user_schema import User_Model
from Backend.App.Core.exceptions import (
    Invalid_Parameters,
    Integrity_Error_Handler,
)
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID


def Get_User_By_Id(db: Session, user_id: UUID) -> User_Model | None:
    User = db.query(User_Model).filter(User_Model.user_id == user_id).first()
    return User


def Get_User_By_Username(db: Session, username: str) -> User_Model | None:
    User = db.query(User_Model).filter(User_Model.username == username).first()
    return User


def Create_Database_User(db: Session, User: User_Model):
    try:
        db.add(User)
        db.commit()
        db.refresh(User)
    except IntegrityError as error:
        db.rollback()
        pg_code = getattr(error.orig, "pgcode", None)
        raise Integrity_Error_Handler(pg_code)


def Delete_Database_User(db: Session, user_id: UUID = None):
    User = Get_User_By_Id(db, user_id)
    if User:
        db.delete(User)
        db.commit()
    else:
        db.rollback()
        raise Invalid_Parameters()
