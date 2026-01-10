from datetime import timedelta
from sqlalchemy.orm import Session
from Backend.App.Core.exceptions import Nonexistent_User, Invalid_Credentials
from Backend.App.Core.security import (
    Compare_Hash_With_String,
    Create_New_Acces_Token,
    Hash_String,
)
from Backend.App.Models.user_schema import User_Model
from Backend.App.Repositories.user_repo import (
    Get_User_By_Username,
    Create_Database_User,
)
from Backend.App.Repositories.refresh_token_repo import Create_Refresh_Token

# Login
# Logout
# create user
# Delete user
# Get user


def Login(Username: str, Password: str, db: Session):
    User = Get_User_By_Username(db, Username)
    if User is None:
        raise Nonexistent_User("Username is invalid")

    Hashed_Password = User.hashed_password
    if not Compare_Hash_With_String(Password, Hashed_Password):
        raise Invalid_Credentials("Password invalid")

    Access_Token = Create_New_Acces_Token(
        User.username, User.user_id, timedelta(hours=2)
    )

    Refresh_Token = Create_Refresh_Token(db, User.user_id, timedelta(days=14))

    output = {"access_token": Access_Token, "refresh_token": Refresh_Token}
    return output


def Logout():
    # Check access
    # Remove refresh from db
    ...


def Create_User(Email: str, Username: str, Password: str, db: Session):
    User = User_Model()
    User.username = Username
    User.hashed_password = Hash_String(Password)
    User.email = Email

    Create_Database_User(db, User)


def Get_User(): ...


def Delete_User():
    # Remove user from db
    ...
