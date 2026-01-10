import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session, sessionmaker, SessionTransaction
from Backend.App.Core.database import Base
from Backend.App.Core.security import Hash_String
from Backend.App.Models.user_schema import User_Model  # noqa: F401
from Backend.App.Models.message_schema import (
    Offline_Message_Model,  # noqa: F401
    Chat_Log_Model,  # noqa: F401
)
from Backend.App.Models.refresh_token_schema import Refresh_Token_Model  # noqa: F401

TEST_URL = "sqlite:///./test.db"
engine = create_engine(TEST_URL)
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal(bind=engine)

    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def mock_user(db):
    User = User_Model()
    User.username = "that1Kid"
    User.hashed_password = Hash_String("Akidanaqi10")
    User.email = "a.anaqi2010@gmail.com"

    db.add(User)
    db.commit()
    db.refresh(User)
    return User
