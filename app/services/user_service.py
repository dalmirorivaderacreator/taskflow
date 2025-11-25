"""
Servicio de usuarios.
Maneja la lógica de negocio relacionada con usuarios.
"""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    """Servicio para gestionar la lógica de negocio de usuarios"""
    
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)
    
    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Obtiene un usuario por su ID"""
        return await self.user_repo.get_by_id(user_id)
    
    async def create_user(self, user_data: UserCreate) -> User:
        """
        Crea un nuevo usuario.
        Valida que el email y username sean únicos.
        """
        # Verificar que el email no exista
        existing_user = await self.user_repo.get_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado"
            )
        
        # Verificar que el username no exista
        existing_user = await self.user_repo.get_by_username(user_data.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El username ya está en uso"
            )
        
        # Crear el usuario
        user = User(
            email=user_data.email,
            username=user_data.username,
            full_name=user_data.full_name,
            hashed_password=get_password_hash(user_data.password),
        )
        
        return await self.user_repo.create(user)
    
    async def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        """Actualiza un usuario existente"""
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        # Actualizar campos si se proporcionan
        if user_data.email is not None:
            user.email = user_data.email
        if user_data.username is not None:
            user.username = user_data.username
        if user_data.full_name is not None:
            user.full_name = user_data.full_name
        if user_data.password is not None:
            user.hashed_password = get_password_hash(user_data.password)
        if user_data.is_active is not None:
            user.is_active = user_data.is_active
        
        return await self.user_repo.update(user)
    
    async def delete_user(self, user_id: int) -> None:
        """Elimina un usuario"""
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no encontrado"
            )
        
        await self.user_repo.delete(user)
