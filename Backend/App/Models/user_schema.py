from sqlalchemy import (
    Column,
    UUID,
    Text,
    DateTime,
    VARCHAR,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User_Model(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True)
    username = Column(VARCHAR(50), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True))
