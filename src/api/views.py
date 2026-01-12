from database import *

from fastapi import APIRouter, Depends, Body
from fastapi.responses import JSONResponse

from api.crud import get_db
from api.schemas import Task

from sqlalchemy.orm import Session


router = APIRouter()


@router.get('/api/tasks')
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@router.get('/api/task')
def get_task_by_id(id, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()

    if task == None:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Task with such id wasn't found"
            }
        )
    
    return task


@router.post('/api/tasks')
def create_task(data = Body(), db: Session = Depends(get_db)):
    task = Task()