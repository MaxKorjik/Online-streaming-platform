from sqlalchemy import Boolean, Column, ForeignKey, String,Text, Integer, DateTime, func
from sqlalchemy.orm import relationship
from database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    password_hash = Column(String, nullable=False)
    email = Column(String(255), unique=True, index=True)
    avatar_url = Column(String)
    role = Column(String(50), index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    streams = relationship(
        "Stream",
        back_populates="streamer",
        cascade="all, delete-orphan"
    )
   
    
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    
class Stream(Base):
    __tablename__ = "streams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)
    is_live = Column(Boolean, default=False)
    started_at = Column(DateTime, server_default=func.now())
    ended_at = Column(DateTime)
    preview_image = Column(String)

    streamer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    streamer = relationship(
        "User",
        back_populates="streams"
    )
    
    
class Follow(Base):
    __tablename__ = "follows"
    
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    following_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
class ChatMessage(Base):
    __tablename__ = "chat_messages"
    
    id = Column(Integer, primary_key=True, index=True)
    stream_id = Column(Integer, ForeignKey("streams.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    
    
class Donation(Base):
    __tablename__ = "donations"
    
    id = Column(Integer, primary_key=True, index=True)
    from_user_id = Column(Integer, ForeignKey("users.id"))
    stream_id = Column(Integer, ForeignKey("streams.id"))
    amount = Column(Integer)
    message = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    
    
class Subscription(Base):
    __tablename__ = "subscriptions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    streamer_id = Column(Integer, ForeignKey("users.id"))
    tier = Column(Integer, index=True)
    expires_at = Column(DateTime)
    
    
class StreamView(Base):
    __tablename__ = "streamviews"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    stream_id = Column(Integer, ForeignKey("streams.id"))
    joined_at = Column(DateTime, server_default=func.now())
    left_at = Column(DateTime)