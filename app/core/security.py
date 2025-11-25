"""
Funciones de seguridad para autenticación y autorización.
Incluye hashing de contraseñas y creación/verificación de tokens JWT.
"""
from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from argon2 import PasswordHasher

from app.core.config import settings

# Contexto para hashing de contraseñas con argon2
# Argon2 es el algoritmo recomendado actualmente y no tiene limitaciones de longitud
hasher = PasswordHasher()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica que una contraseña en texto plano coincida con el hash"""
    return hasher.verify(hashed_password, plain_password)


def get_password_hash(password: str) -> str:
    """
    Genera el hash de una contraseña usando Argon2.
    Argon2 es el algoritmo ganador de la Password Hashing Competition.
    """
    return hasher.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crea un token JWT con los datos proporcionados.
    
    Args:
        data: Diccionario con los datos a incluir en el token (ej: {"sub": user_id})
        expires_delta: Tiempo de expiración personalizado (opcional)
    
    Returns:
        Token JWT codificado como string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Decodifica y verifica un token JWT.
    
    Args:
        token: Token JWT a decodificar
    
    Returns:
        Diccionario con los datos del token o None si es inválido
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None
