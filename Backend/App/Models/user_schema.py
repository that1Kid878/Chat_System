from sqlalchemy import Column, UUID, Text, DateTime, VARCHAR, text
from Backend.App.Core.database import Base


class User_Model(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    username = Column(VARCHAR(50), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    email = Column(Text, unique=True, nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )
