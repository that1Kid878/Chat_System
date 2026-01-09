from datetime import timedelta, datetime
from Backend.App.Models.refresh_token_schema import Refresh_Token_Model
from Backend.App.Core.security import Generate_Refresh_Token, Hash_Refresh_Token
from Backend.App.Core.exceptions import (
    Invalid_Parameters,
    Integrity_Error_Handler,
)
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID, uuid4


def Get_Refresh_Token_By_Hash(
    db: Session, token_hash: str
) -> Refresh_Token_Model | None:
    Token = (
        db.query(Refresh_Token_Model)
        .filter(Refresh_Token_Model.token_hash == token_hash)
        .first()
    )
    return Token


def Get_Refresh_Token_By_User_Id(
    db: Session, user_id: UUID
) -> list[Refresh_Token_Model] | None:
    Token = (
        db.query(Refresh_Token_Model)
        .filter(Refresh_Token_Model.user_id == user_id)
        .all()
    )
    return Token


def Get_Refresh_Token_By_Token_Id(
    db: Session, token_id: UUID
) -> list[Refresh_Token_Model] | None:
    Token = (
        db.query(Refresh_Token_Model)
        .filter(Refresh_Token_Model.token_id == token_id)
        .all()
    )
    return Token


def Create_Refresh_Token(db: Session, User_Id: int, ExpireDelta: timedelta):
    Token_Id = uuid4()
    Token_Content = Generate_Refresh_Token(Token_Id)

    Token = Refresh_Token_Model()
    Token.token_id = Token_Id
    Token.user_id = User_Id
    Token.token_hash = Hash_Refresh_Token(Token_Content)
    Token.expire_at = datetime.now() + ExpireDelta

    try:
        db.add(Token)
        db.commit()
        db.refresh(Token)
    except IntegrityError as error:
        db.rollback()
        pg_error = error.orig
        pg_code = getattr(pg_error, "pgcode")
        raise Integrity_Error_Handler(pg_code)

    return Token_Content


def Delete_Refresh_Token(db: Session, token_id: UUID):
    Token = Get_Refresh_Token_By_Token_Id(db, token_id)
    if Token:
        db.delete(Token)
        db.commit()
    else:
        db.rollback()
        raise Invalid_Parameters()
