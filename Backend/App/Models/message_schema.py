from sqlalchemy import Text, DateTime, ForeignKey, text
from sqlalchemy.orm import mapped_column
from Backend.App.Core.database import Base
from Backend.App.Core.types import GUID
import uuid


class Message:
    message_id = mapped_column(
        GUID(),
        primary_key=True,
        default=uuid.uuid4(),
        server_default=text("gen_random_uuid()"),
    )
    sender_id = mapped_column(
        GUID(),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    reciever_id = mapped_column(
        GUID(),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    body = mapped_column(Text, nullable=False)
    created_at = mapped_column(
        DateTime(timezone=True), server_default=text("CURRENT_TIMESTAMP")
    )


class Offline_Message_Model(Message, Base):
    __tablename__ = "offline_messages"


class Chat_Log_Model(Message, Base):
    __tablename__ = "chat_log"
