from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(255))
    initVector = Column(String(255))

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    owner_id = Column(Integer)
    description = Column(String(255)) #foreign key from User table

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    status = Column(Integer)
    notes = Column(String(255)) #foreign key from User table

class Status(Base):
    __tablename__ = 'statuses'
    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String(50))
