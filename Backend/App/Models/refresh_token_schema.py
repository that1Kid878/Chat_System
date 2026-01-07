from sqlalchemy import Column, UUID, Text, DateTime, Boolean, ForeignKey, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Refresh_Token_Model(Base):
    __tablename__ = "refresh_tokens"

    token_id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    token_hash = Column(Text, nullable=False)
    expire_at = Column(DateTime(timezone=True), nullable=False)
    revoked = Column(Boolean, server_default="FALSE")
    created_at = Column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )
