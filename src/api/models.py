from pydantic import BaseModel

from datetime import datetime



class TaskCreate(BaseModel):
    name: str 
    description: str


class TaskResponse(BaseModel):
    id: int 
    name: str 
    description: str 
    created_at: datetime