"""
Schemas de Pydantic para validación de datos de Etiqueta.
Define los modelos de entrada y salida de la API.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TagBase(BaseModel):
    """Schema base con campos comunes"""
    name: str
    color: str = "#3B82F6"


class TagCreate(TagBase):
    """Schema para crear una nueva etiqueta"""
    pass


class TagUpdate(BaseModel):
    """Schema para actualizar una etiqueta (todos los campos opcionales)"""
    name: Optional[str] = None
    color: Optional[str] = None


class TagInDB(TagBase):
    """Schema que representa una etiqueta en la base de datos"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True


class TagResponse(TagInDB):
    """Schema de respuesta para el cliente"""
    pass
