from database import *

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from api.crud import get_db
from api.schemas import (
    TaskCreate, 
    TaskResponse, 
    Task, 
    TaskUpdate
)

from sqlalchemy.orm import Session


router = APIRouter()


@router.get('/api/tasks')
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@router.get('/api/task/{id}', response_model=TaskResponse)
def get_task_by_id(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()

    if task == None:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Task with such id wasn't found"
            }
        )
    
    return task


@router.post('/api/tasks', response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(**task.dict())
    
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.put('/api/tasks/{id}', response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    db_task.name = task.name
    db_task.description = task.description

    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete('/api/tasks/{id}', response_class=JSONResponse)
def delete_task(id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    db.delete(db_task)
    db.commit()

    return JSONResponse(
        status_code=204, 
        detail = {
        "message": "Task deleted successfully"
    })