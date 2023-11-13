#file that creates the tables if they do not already exist
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=True)
  username = Column(String(50), unique=True, nullable=True)
  email = Column(String(100), unique=True, nullable=False)
  password = Column(String(100), nullable=False)

  #relationship: a user can own many projects
  projects = relationship('Project', back_populates='owner')

class Project(Base):
  __tablename__ = 'projects'
  id = Column(Integer, primary_key=True, index=True)
  owner_id = Column(ForeignKey('users.id'))
  name = Column(String(50))
  description = Column(String(999), nullable=True)
  
  #relationship: a project belongs to a user
  owner = relationship('User', back_populates='projects')
  #relationship: a project can own many tasks
  tasks = relationship('Task', back_populates='project')

class Task(Base):
  __tablename__ = 'tasks'
  id = Column(Integer, primary_key=True, index=True)
  project_id = Column(ForeignKey('projects.id'))
  name = Column(String(50))
  description = Column(String(999), nullable=True)

  #relationship: a task belongs to a project
  project = relationship('Project', back_populates='tasks')
