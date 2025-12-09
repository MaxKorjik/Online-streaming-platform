from database import Base
from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, unique=True)
    