from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

#Testing JSON Objects
testingUsers = {
  1: {
    'user_id': 1,
    'name': 'Marc',
    'username': 'majocast',
    'email': 'test@mail.com',
    'password': '1234',
    'initVector': 'hfaskdacnsdla',
  },
  2: {
    'user_id': 2,
    'name': 'Abby',
    'username': 'apasghtetti',
    'email': 'test2@mail.com',
    'password': '1234',
    'initVector': 'aahasbvlavasdiu',
  },
  3: {
    'user_id': 2,
    'name': 'Angela',
    'username': 'puffdaddy',
    'email': 'test3@mail.com',
    'password': '1234',
    'initVector': 'jiovhdflia',
  }
}

testingProjects = {
  1: {
    'project_id': 1,
    'name': 'Stuff',
    'owner_id': 2,
    'editors': [1],
    'description': 'get er done'
  },
  2: {
    'project_id': 2,
    'name': 'Stuff2',
    'owner_id': 2,
    'editors': [1, 3],
    'description': 'get er done'
  },
  3: {
    'project_id': 3,
    'name': 'Stuff3',
    'owner_id': 1,
    'editors': [2, 3],
    'description': 'get er done'
  }
}

testingTasks = {
  1: {
    'task_id': 1,
    'project_id': 2,
    'name': 'Hello',
    'status': 2,
    'notes': 'get er done'
  },
  2: {
    'task_id': 2,
    'project_id': 2,
    'name': 'Hello Again',
    'status': 1,
    'notes': 'get er done now'
  },
  3: {
    'task_id': 3,
    'project_id': 1,
    'name': 'Hello',
    'status': 3,
    'notes': 'get er done right now'
  },
  4: {
    'task_id': 4,
    'project_id': 3,
    'name': 'Hello there',
    'status': 1,
    'notes': 'get er done right now now'
  }
}

#CLASS MODELS
class Task(BaseModel):
  name: str
  project_id: int
  status: Optional[int] = None
  notes: str


class User(BaseModel):
  name: Optional[str] = None
  username: Optional[str] = None
  email: str
  password: str
  initVector: str


class Project(BaseModel):
  name: str
  owner_id = int
  editors = Optional[List[int]] = None
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
  initVector: Optional[str] = None


class EditedProject(BaseModel):
  name: Optional[str] = None
  owner_id = Optional[int]
  editors = Optional[List[int]] = None
  description: Optional[str] = None


#ROUTES
@app.get('/')
def home():
  return {"Server": "Successfully started"}

#USER ROUTES
#login
@app.get('/user')
def home(email: str, password: str):
    return {"Login": "Successful"}

#registration
@app.post('/user')
def register(user: User):
  return {"Login": "Successful"}

#edit user
@app.post('/user/{user_id}')
def register(user_id: int, user: EditedUser):
  return {"Login": "Successful"}

#TASKS
@app.get('/task/{project_id}')
def task(project_id: int):
  return {"Task": "Retrieved"}

@app.post('/task/{project_id}')
def task(project_id: int, task: Task):
  return {"Task": "Posted"}

@app.delete('/task/{project_id}/{task_id}')
def task(project_id: int, task_id: int):
  return {"Task": "Deleted"}

@app.put('/task/{project_id}/{task_id}')
def task(project_id: int, task_id: int, task: EditedTask):
  return {"Task": "Edited"}

#PROJECTS
@app.get('/project/{user_id}')
def project(user_id: int):
  return{"got": "projects"}

@app.post('/project/{user_id}')
def project(user_id: int, project: Project):
  return{"posted": "projects"}

@app.put('/project/{user_id}')
def project(user_id: int, project: EditedProject):
  return{"editted": "projects"}

@app.delete('/project/{project_id}/{user_id}')
def project(project_id: int, user_id: int):
  return{"deleted": "project"}