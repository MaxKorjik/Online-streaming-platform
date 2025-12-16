import email
from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, String, Text, Integer, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), index=True)
    password = Column(String, unique=True)
    email = Column(String(255), unique=True, nullable=True, index=True)
    avatar_url = Column(String)
    role = Column(String(255), nullable=True, index=True)
    is_active = Column(Boolean)
    created_at = Column(DateTime, server_default=datetime.now())
    
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)
    
class Stream(Base):
    __tablename__ = "streams"
    
    id = Column(Integer, primary_key=True, index=True)
    streamer_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    streamer = relationship(
        "User",
        back_populates="streams"
    )