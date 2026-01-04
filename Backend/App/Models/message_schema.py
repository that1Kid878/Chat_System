from sqlalchemy import Column, UUID, Text, DateTime, ForeignKey, text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Message:
    message_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    sender_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    reciever_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    body = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True))


class Offline_Message_Model(Message, Base):
    __tablename__ = "offline_messages"


class Chat_Log_Model(Message, Base):
    __tablename__ = "chat_log"
