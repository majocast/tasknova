from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Server": "Successfully started"}