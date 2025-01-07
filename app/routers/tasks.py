
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services
from app.database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("/" , response_model=list[schemas.Task]) 
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = services.get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/{task_id}" , response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = services.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/" , response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return services.create_tasks(db, task)


@router.put("/{task_id}" , response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = services.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}" , response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = services.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task