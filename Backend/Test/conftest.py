import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from Backend.App.Models.user_schema import User_Model
from Backend.App.Models.message_schema import Offline_Message_Model, Chat_Log_Model
from Backend.App.Models.refresh_token_schema import Refresh_Token_Model

Base = declarative_base()


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite:///./test.db", connect_args={"check_same_threads": False}
    )

    TestingSessionLocal = sessionmaker(bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
