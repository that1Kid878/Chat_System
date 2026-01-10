from Backend.App.Repositories.user_repo import (
    Create_Database_User,
    Get_User_By_Username,
    Delete_Database_User,
)
from Backend.App.Models.user_schema import User_Model


def test_user_creation(db):
    User = User_Model()
    User.username = "that1Kid"
    User.email = "nice@gmail.com"
    User.hashed_password = "psoijsdvkosijdsasjf"

    Create_Database_User(db, User)

    DB_User = Get_User_By_Username(db, username="that1Kid")
    assert DB_User.username == User.username
    assert DB_User.email == User.email
    assert DB_User.hashed_password == User.hashed_password

    Delete_Database_User(db, DB_User.user_id)

    assert Get_User_By_Username(db, username="that1Kid") is None
