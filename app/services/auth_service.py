"""
Servicio de autenticación.
Maneja el login y validación de usuarios.
"""
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, verify_password
from app.models.user import User
from app.repositories.user_repo import UserRepository
from app.schemas.user import Token


class AuthService:
    """Servicio para gestionar autenticación de usuarios"""
    
    def __init__(self, db: AsyncSession):
        self.user_repo = UserRepository(db)
    
    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """
        Autentica un usuario verificando sus credenciales.
        
        Args:
            username: Nombre de usuario o email
            password: Contraseña en texto plano
        
        Returns:
            Usuario autenticado o None si las credenciales son inválidas
        """
        # Buscar por username o email
        user = await self.user_repo.get_by_username(username)
        if not user:
            user = await self.user_repo.get_by_email(username)
        
        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None
        
        if not user.is_active:
            return None
        
        return user
    
    async def login(self, username: str, password: str) -> Optional[Token]:
        """
        Realiza el login y genera un token JWT.
        
        Args:
            username: Nombre de usuario o email
            password: Contraseña en texto plano
        
        Returns:
            Token de acceso o None si las credenciales son inválidas
        """
        user = await self.authenticate_user(username, password)
        if not user:
            return None
        
        access_token = create_access_token(data={"sub": str(user.id)})
        return Token(access_token=access_token)
