"""
Router principal de la API v1.
Agrupa todos los routers de los diferentes módulos.
"""
from fastapi import APIRouter

from app.api.v1 import auth, tags, tasks, users

# Router principal de la API v1
api_router = APIRouter()

# Incluir routers de cada módulo
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(tags.router, prefix="/tags", tags=["tags"])
