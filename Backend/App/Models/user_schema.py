from sqlalchemy import Text, DateTime, VARCHAR, Boolean, text
from sqlalchemy.orm import mapped_column
from Backend.App.Core.database import Base
from Backend.App.Core.types import GUID
import uuid


class User_Model(Base):
    __tablename__ = "users"

    user_id = mapped_column(
        GUID(),
        primary_key=True,
        default=uuid.uuid4(),
        server_default=text("gen_random_uuid()"),
    )
    username = mapped_column(VARCHAR(50), unique=True, nullable=False)
    hashed_password = mapped_column(Text, nullable=False)
    email = mapped_column(Text, unique=True, nullable=False)
    created_at = mapped_column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )
    verified = mapped_column(Boolean, server_default=text("false"))
