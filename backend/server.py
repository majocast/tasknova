#main server file that serves the db connection and handles routing
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Annotated
from pydantic import BaseModel
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models

#app initialization
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with frontend's URL(s)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
  description: str


class UserBase(BaseModel):
  name: Optional[str] = None
  username: Optional[str] = None
  email: str
  password: str


class ProjectBase(BaseModel):
  name: str
  owner_id: int
  description: Optional[str] = None


#EDITTING MODELS
class EditedTask(BaseModel):
  name: Optional[str] = None
  status: Optional[int] = None
  description: Optional[int] = None


class EditedUser(BaseModel):
  name: Optional[str] = None
  username: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None


class EditedProject(BaseModel):
  name: Optional[str] = None
  owner_id: Optional[int] = None
  description: Optional[str] = None



#ROUTES
@app.get('/')
def home():
  return {"Server": "Successfully started"}

#USER ROUTES
#login
@app.get('/user', status_code=status.HTTP_200_OK) #done
async def login_user(email: str, password: str, db: db_dependency):
  user = db.query(models.User).filter(models.User.email == email).first()
  if user is not None:
    if user.password == password:
      return user
    else:
      raise HTTPException(status_code=401, detail='Incorrect Email or Password')
  else:
    raise HTTPException(status_code=404, detail='Email Not Registered')


#registration
@app.post('/user', status_code=status.HTTP_201_CREATED) #done
async def register_user(user: UserBase, db: db_dependency):
  print('in post')
  print(user)
  db_user = models.User(**user.model_dump())
  db.add(db_user)
  db.commit()
  registered_user = db.query(models.User).filter(models.User.email == user.email).first()
  return registered_user
  

#edit user
@app.put('/user/{user_id}', status_code=status.HTTP_200_OK) #done
async def edit_user(user_id: int, user: EditedUser, db: db_dependency):
  update_values = {}
  if user.username:
      update_values['username'] = user.username
  if user.password:
      update_values['password'] = user.password
  
  if not update_values:
      raise HTTPException(status_code=400, detail="No fields to update")

  db_user = db.query(models.User).filter(models.User.id == user_id).first()
  if db_user is None:
      raise HTTPException(status_code=404, detail='User Not Found')

  db.query(models.User).filter(models.User.id == user_id).update(update_values)
  db.commit()

  return db_user


#TASKS
@app.get('/task/{project_id}', status_code=status.HTTP_200_OK) #done
async def get_tasks(project_id: int, db: db_dependency):
  tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()
  #we do not do error handling for empty tasks because the array can be empty on return
  return tasks


@app.post('/task', status_code=status.HTTP_201_CREATED) #done
async def add_task(task: TaskBase, db: db_dependency):
  db_task = models.Task(**task.model_dump())
  db.add(db_task)
  db.commit()
  return db_task


@app.delete('/task/{project_id}/{task_id}', status_code=status.HTTP_204_NO_CONTENT) #done
async def delete_task(project_id: int, task_id: int, db: db_dependency):
  db_task = db.query(models.Task).filter(models.Task.id == task_id and models.Task.project_id == project_id).first()
  if db_task is None:
    raise HTTPException(status_code=404, detail='Task Not Found')
  db.delete(db_task)
  db.commit()
  

@app.put('/task/{task_id}', status_code=status.HTTP_200_OK) #done
async def edit_task(task_id: int, task: EditedTask, db: db_dependency):
  update_values = {}
  if task.username:
      update_values['username'] = task.username
  if task.status:
      update_values['status'] = task.status
  if task.description:
      update_values['description'] = task.description
  
  if not update_values:
      raise HTTPException(status_code=400, detail="No fields to update")

  db_user = db.query(models.Task).filter(models.Task.id == task_id).first()
  if db_user is None:
      raise HTTPException(status_code=404, detail='User Not Found')

  db_task = db.query(models.Task).filter(models.Task.id == task_id).update(update_values)
  db.commit()

  return db_task


#PROJECTS
@app.get('/project/{project_id}/{user_id}', status_code=status.HTTP_200_OK) #done
async def get_projects(project_id: int, user_id: int, db: db_dependency):
  projects = db.query(models.Project).filter(models.Project.owner_id == user_id).all()
  #empty projects arrays can be returned as well
  return projects

@app.post('/project', status_code=status.HTTP_201_CREATED) #done
async def add_project(project: ProjectBase, db: db_dependency):
  db_project = models.Project(**project.model_dump())
  db.add(db_project)
  db.commit()
  return db_project


@app.put('/project/{project_id}', status_code=status.HTTP_200_OK) #done
async def edit_project(project_id: int, project: EditedProject, db: db_dependency):
  update_values = {}
  if project.name:
    update_values['name'] = project.name
  if project.owner_id:
    update_values['owner_id'] = project.owner_id
  if project.description:
    update_values['description'] = project.description
  
  if not update_values:
    raise HTTPException(status_code=400, detail='No fields to update')

  db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
  if db_project is None:
    raise HTTPException(status_code=404, detail='Project Not Found')
  
  db.query(models.Project).filter(models.Project.id == project_id).update(update_values)
  db.commit()
  return db_project


@app.delete('/project/{project_id}', status_code=status.HTTP_204_NO_CONTENT) #done
async def delete_project(project_id: int, db: db_dependency):
  db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
  if db_project is None:
    raise HTTPException(status_code=404, detail='Project Not Found')
  
  #cleaning up project editors in project_editors relation table
  db_editors = db.query(models.project_editors).filter(models.project_editors.c.project_id == project_id).all()
  if db_editors:
    for editor in db_editors:
      db.delete(editor)
  
  #cleaning up tasks if they exist
  db_tasks = db.query(models.Task).filter(models.Task.project_id == project_id).all()
  if db_tasks:
    for task in db_tasks:
      db.delete(task)

  #deleting project, and (if they exist) editors and tasks associated
  db.delete(db_project)
  db.commit()


#EDITORS
@app.get('/editors/{project_id}', status_code=status.HTTP_200_OK)
async def get_editors(project_id: int, db: db_dependency):
  db_editors = db.query(models.project_editors).filter(models.project_editors.c.project_id == project_id).all()
  #okay to return empty array
  return db_editors


@app.post('/editors/{project_id}/{user_id}', status_code=status.HTTP_201_CREATED)
async def add_editor(project_id: int, user_id: int, db: db_dependency):
  new_editor = {
    "user_id": user_id,
    "project_id": project_id
  }

  db.execute(models.project_editors.insert().values(new_editor))
  db.commit()
  return new_editor


#deleting individual user from editors on project
@app.delete('/editors/{project_id}/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def get_editors(project_id: int, user_id: int, db: db_dependency):
  db_editor = (db.query(models.project_editors)
                .filter(
                  models.project_editors.c.project_id == project_id,
                  models.project_editors.c.user_id == user_id,
                )
                .all()
              )
  if not db_editor:
    raise HTTPException(status_code=404, detail="Editor Not Found")
  db.delete(db_editor)
  db.commit()
  #okay to return empty array
  return db_editor