from Backend.App.Models.refresh_token_schema import Refresh_Token_Model
from Backend.App.Core.exceptions import (
    Invalid_Parameters,
    Integrity_Error_Handler,
)
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from uuid import UUID


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


def Create_Database_Refresh_Token(db: Session, Token: Refresh_Token_Model):
    try:
        db.add(Token)
        db.commit()
        db.refresh(Token)
    except IntegrityError as error:
        pg_error = error.orig
        pg_code = getattr(pg_error, "pgcode")
        raise Integrity_Error_Handler(pg_code)


def Delete_Refresh_Token(db: Session, token_id: UUID):
    Token = Get_Refresh_Token_By_Token_Id(db, token_id)
    if Token:
        db.delete(Token)
        db.commit()
    else:
        raise Invalid_Parameters()
