from sqlalchemy import Text, DateTime, Boolean, ForeignKey, text
from sqlalchemy.orm import mapped_column
from Backend.App.Core.database import Base
from Backend.App.Core.types import GUID
import uuid


class Refresh_Token_Model(Base):
    __tablename__ = "refresh_tokens"

    token_id = mapped_column(
        GUID(),
        primary_key=True,
        default=uuid.uuid4(),
        server_default=text("gen_random_uuid()"),
    )
    user_id = mapped_column(
        GUID(),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    token_hash = mapped_column(Text, nullable=False)
    expire_at = mapped_column(DateTime(timezone=True), nullable=False)
    revoked = mapped_column(Boolean, server_default="FALSE")
    created_at = mapped_column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )
