import pytest
from sqlalchemy.orm import Session
from Backend.App.Core.database import SessionLocal, Base, engine
from Backend.App.Core.security import Hash_String
from Backend.App.Models.user_schema import User_Model  # noqa: F401
from Backend.App.Models.message_schema import (
    Offline_Message_Model,  # noqa: F401
    Chat_Log_Model,  # noqa: F401
)
from Backend.App.Models.refresh_token_schema import Refresh_Token_Model  # noqa: F401


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def mock_user(db: Session):
    User = User_Model()
    User.username = "that1Kid"
    User.hashed_password = Hash_String("Akidanaqi10")
    User.email = "a.anaqi2010"

    db.add(User)
    db.commit()
    db.refresh()
    return User
