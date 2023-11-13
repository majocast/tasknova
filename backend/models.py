#file that creates the tables if they do not already exist
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# a junction table that creates the many-to-many relationship between projects and users/editors
# many to many relationship implicitly handled by sqlalchemy
  # no need to define a relationship in table
project_editors = Table(
  'project_editors', Base.metadata,
  Column('user_id', Integer, ForeignKey('users.id')),
  Column('project_id', Integer, ForeignKey('projects.id'))
)
# ^ many editors can be editors to many projects
#back populates are used to handle the navigate and manage the relationship

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(100), nullable=True)
  username = Column(String(50), unique=True, nullable=True)
  email = Column(String(100), unique=True, nullable=False)
  password = Column(String(100), nullable=False)

  #USER RELATIONSHIPS
  projects = relationship('Project', back_populates='owner') #a user can own many projects
  editor_to_project = relationship('Project', secondary=project_editors, back_populates='editors')
  # a user can be an editor to many projects

class Project(Base):
  __tablename__ = 'projects'
  id = Column(Integer, primary_key=True, index=True)
  owner_id = Column(Integer, ForeignKey('users.id'))
  name = Column(String(50))
  description = Column(String(999), nullable=True)
  
  #PROJECT RELATIONSHIPS
  owner = relationship('User', back_populates='projects') #a project belongs to a user
  tasks = relationship('Task', back_populates='project')  #a project can own many tasks
  editors = relationship('User', secondary=project_editors, back_populates='editor_to_project')
  # ^ a project can have many editors of user_ids

class Task(Base):
  __tablename__ = 'tasks'
  id = Column(Integer, primary_key=True, index=True)
  project_id = Column(Integer, ForeignKey('projects.id'))
  name = Column(String(50))
  description = Column(String(999), nullable=True)
  status = Column(Integer, ForeignKey('statuses.id'))

  #TASK RELATIONSHIPS
  project = relationship('Project', back_populates='tasks') # a task belongs to a project


class Status(Base):
  __tablename__ = 'statuses'
  id = Column(Integer, primary_key=True, index=True)
  status = Column(String(15))