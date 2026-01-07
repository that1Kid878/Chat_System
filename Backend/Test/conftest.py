import pytest
from Backend.App.Core.database import SessionLocal, Base, engine
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
