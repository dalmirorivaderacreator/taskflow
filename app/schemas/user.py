"""
Schemas de Pydantic para validación de datos de Usuario.
Define los modelos de entrada y salida de la API.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Schema base con campos comunes"""
    email: EmailStr
    username: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """Schema para crear un nuevo usuario"""
    password: str


class UserUpdate(BaseModel):
    """Schema para actualizar un usuario (todos los campos opcionales)"""
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """Schema que representa un usuario en la base de datos"""
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True  # Permite crear desde objetos SQLAlchemy


class UserResponse(UserInDB):
    """Schema de respuesta para el cliente (sin datos sensibles)"""
    pass


class Token(BaseModel):
    """Schema para respuesta de autenticación"""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema para datos decodificados del token"""
    user_id: Optional[int] = None
