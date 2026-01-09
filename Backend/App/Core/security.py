from .exceptions import Invalid_Access_Token, Expired_Access_Token
from datetime import timedelta, datetime, timezone
from jose import jwt, ExpiredSignatureError, JWTError
from uuid import UUID
from .config import REFRESH_TOKEN_PEPPER, ACCESS_SECRET_KEY
import secrets
import hmac
import hashlib
import bcrypt

Access_Token_Hashing_Algorithm = "HS256"


def Hash_String(String: str) -> str:
    return bcrypt.hashpw(String.encode(), bcrypt.gensalt()).decode()


def Compare_Hash_With_String(String: str, Hash: str) -> True:
    return bcrypt.checkpw(String.encode(), Hash.encode())


def Generate_Refresh_Token(Token_id: UUID) -> str:
    Secret = secrets.token_urlsafe()
    return f"{Token_id}.{Secret}"


def Hash_Refresh_Token(Token: str) -> str:
    New_Token = hmac.new(
        REFRESH_TOKEN_PEPPER.encode(), Token.encode(), hashlib.sha256
    ).digest()
    return New_Token.hex()


def Create_New_Acces_Token(Username: str, User_ID: UUID, ExpireDelta: timedelta) -> str:
    ExpiryDate = datetime.now(timezone.utc) + ExpireDelta
    Token_Data = {"sub": Username, "id": User_ID, "exp": ExpiryDate}
    return jwt.encode(
        Token_Data, ACCESS_SECRET_KEY, algorithm=Access_Token_Hashing_Algorithm
    )


def Decode_Access_Token(Token: str):
    try:
        payload = jwt.decode(
            Token, ACCESS_SECRET_KEY, algorithms=[Access_Token_Hashing_Algorithm]
        )
    except ExpiredSignatureError:
        raise Expired_Access_Token
    except JWTError:
        raise Invalid_Access_Token

    return payload
