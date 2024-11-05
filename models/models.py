from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Column, JSON, Boolean
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import DeclarativeBase

Base: DeclarativeMeta = declarative_base()

class Base(DeclarativeBase):
    pass

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String)
    password = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, server_default=func.now())
    role_id = Column(Integer, ForeignKey(Role.id), default=2)
    active = Column(Boolean, default=True, nullable=False)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    deployed_at = Column(TIMESTAMP, server_default=func.now())
    author_id = Column(Integer, ForeignKey(User.id)) 
    title = Column(String(length=32), nullable=False)
    description = Column(String(length=1024), nullable=False)
