from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(255), nullable=True)
  username = Column(String(50), unique=True, nullable=True)
  email = Column(String(50), unique=True)
  password = Column(String(255))
  initVector = Column(String(255))

class Project(Base):
  __tablename__ = 'projects'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(50))
  owner_id = Column(Integer, ForeignKey('users.id'))
  description = Column(String(255))
  editors = relationship("User", secondary='project_editors', back_populates='projects')

class Task(Base):
  __tablename__ = 'tasks'
  id = Column(Integer, primary_key=True, index=True)
  project_id = Column(Integer, ForeignKey('projects.id'))
  name = Column(String(50))
  status = Column(Integer, ForeignKey('statuses.id'), nullable=True)
  notes = Column(String(255)) 
  project = relationship("Project", back_populates="tasks")
  task_status = relationship("Status", back_populates="tasks")

class Status(Base):
  __tablename__ = 'statuses'
  id = Column(Integer, primary_key=True, index=True)
  status_name = Column(String(50))
  tasks = relationship("Task", back_populates="task_status")

#this table servers as the link between user and project tables, providing a many-to-many relationship
#one user can be editor of many projects, and one project can have many editors
#therefore, many users can be editor to many projects -> many-to-many
class ProjectEditors(Base):
  __tablename__ = 'project_editors'
  project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)
  editor_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

User.projects = relationship("Project", back_populates="owner")
User.edited_projects = relationship("Project", secondary="project_editors", back_populates="editors")
Project.tasks = relationship("Task", back_populates="project")
Status.tasks = relationship("Task", back_populates="task_status")
