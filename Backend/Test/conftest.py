import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from Backend.App.Core.database import SessionLocal, Base, engine
from Backend.App.Models.user_schema import User_Model
from Backend.App.Models.message_schema import Offline_Message_Model, Chat_Log_Model
from Backend.App.Models.refresh_token_schema import Refresh_Token_Model


@pytest.fixture
def db():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
