"""
Schemas de Pydantic para validación de datos de Tarea.
Define los modelos de entrada y salida de la API.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.tag import TagResponse


class TaskBase(BaseModel):
    """Schema base con campos comunes"""
    title: str
    description: Optional[str] = None
    priority: int = 0
    is_completed: bool = False


class TaskCreate(TaskBase):
    """Schema para crear una nueva tarea"""
    tag_ids: Optional[List[int]] = []


class TaskUpdate(BaseModel):
    """Schema para actualizar una tarea (todos los campos opcionales)"""
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None
    is_completed: Optional[bool] = None
    tag_ids: Optional[List[int]] = None


class TaskInDB(TaskBase):
    """Schema que representa una tarea en la base de datos"""
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class TaskResponse(TaskInDB):
    """Schema de respuesta con tags incluidos"""
    tags: List[TagResponse] = []
    
    class Config:
        orm_mode = True
