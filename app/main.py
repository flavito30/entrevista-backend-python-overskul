
from fastapi import FastAPI
from app.database import Base,engine
from app.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Management API",
    description="Api para gestionar tareas en FastAPI",
    version="1.0.0"
)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to your task management API!"}


