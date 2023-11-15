#main server file that serves the db connection and handles routing
from fastapi import FastAPI, HTTPException, Depends, status
from typing import List, Optional, Annotated
from pydantic import BaseModel
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

#app initialization
app = FastAPI()
models.Base.metadata.create_all(bind=engine)

#helper function to prepopulate statuses table if empty for whatever reason
def prepopulate_status():
  db = next(get_db()) #next or __next__ is used to get the next yieldable value in a generative function
  #in this case, next() will provide the next database session
  statuses = db.query(models.Status).first() #db.query returns Query object, to retrieve results
                                           # we use .all() or .first() to execute the query
                                           # kind of like processing a promise 
  if statuses is None:
    not_started = models.Status(status='Not Started')
    in_progress = models.Status(status='In Progress')
    under_review = models.Status(status='Under Review')
    completed = models.Status(status='Completed')

    db.add_all([not_started, in_progress, under_review, completed])
    db.commit()
  

#database dependency
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

prepopulate_status()

#CLASS MODELS
class TaskBase(BaseModel):
  name: str
  project_id: int
  status: Optional[int] = None
  notes: str


class UserBase(BaseModel):
  name: Optional[str] = None
  username: Optional[str] = None
  email: str
  password: str


class ProjectBase(BaseModel):
  name: str
  owner_id: int
  editors: List[int]
  description: Optional[str] = None


#EDITTING MODELS
class EditedTask(BaseModel):
  name: Optional[str] = None
  status: Optional[int] = None
  notes: Optional[int] = None


class EditedUser(BaseModel):
  name: Optional[str] = None
  username: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None


class EditedProject(BaseModel):
  name: Optional[str] = None
  owner_id: Optional[int]
  editors: Optional[List[int]] = None
  description: Optional[str] = None



#ROUTES
@app.get('/')
def home():
  return {"Server": "Successfully started"}

#USER ROUTES
#login
@app.get('/user', status_code=status.HTTP_200_OK)
async def login_user(email: str, password: str, db: db_dependency):
  user = db.query(models.User).filter(models.User.email == email).first()
  if user is not None:
    if user.password == password:
      return user
    else:
      raise HTTPException(status_code=401, detail='Incorrect Email or Password')
  else:
    raise HTTPException(status_code=404, detail='email not registered')


#registration
@app.post('/user', status_code=status.HTTP_201_CREATED)
async def register_user(user: UserBase, db: db_dependency):
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()
  

#edit user
@app.put('/user/{user_id}', status_code=status.HTTP_200_OK)
async def edit_user(user_id: int, user: EditedUser, db: db_dependency):
  db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
  return {}


#TASKS
@app.get('/task/{project_id}', status_code=status.HTTP_200_OK)
async def get_tasks(project_id: int, db: db_dependency):
  tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()
  return tasks


@app.post('/task/{project_id}', status_code=status.HTTP_201_CREATED)
async def add_task(project_id: int, task: TaskBase):
  return {"Task": "Posted"}


@app.delete('/task/{project_id}/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(project_id: int, task_id: int):
  return {"Task": "Deleted"}


@app.put('/task/{project_id}/{task_id}', status_code=status.HTTP_200_OK)
async def edit_task(project_id: int, task_id: int, task: EditedTask):
  return {"Task": "Edited"}


#PROJECTS
@app.get('/project/{user_id}', status_code=status.HTTP_200_OK)
async def get_projects(user_id: int):
  return{"got": "projects"}


@app.post('/project/{user_id}', status_code=status.HTTP_201_CREATED)
async def add_project(user_id: int, project: ProjectBase):
  return{"posted": "projects"}


@app.put('/project/{user_id}', status_code=status.HTTP_200_OK)
async def edit_project(user_id: int, project: EditedProject):
  return{"edited": "projects"}


@app.delete('/project/{project_id}/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: int, user_id: int):
  return{"deleted": "project"}