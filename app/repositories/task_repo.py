"""
Repositorio para operaciones de base de datos relacionadas con tareas.
Abstrae las queries de SQLAlchemy.
"""
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.task import Task


class TaskRepository:
    """Repositorio para gestionar operaciones CRUD de tareas"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, task_id: int, owner_id: int) -> Optional[Task]:
        """Obtiene una tarea por su ID y propietario"""
        result = await self.db.execute(
            select(Task)
            .options(selectinload(Task.tags))  # Carga eager de tags
            .where(Task.id == task_id, Task.owner_id == owner_id)
        )
        return result.scalar_one_or_none()
    
    async def get_all_by_owner(self, owner_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        """Obtiene todas las tareas de un usuario con paginación"""
        result = await self.db.execute(
            select(Task)
            .options(selectinload(Task.tags))
            .where(Task.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()
    
    async def create(self, task: Task) -> Task:
        """Crea una nueva tarea"""
        self.db.add(task)
        await self.db.commit()
        await self.db.refresh(task)
        # Re-fetch to ensure tags are loaded (avoid MissingGreenlet)
        return await self.get_by_id(task.id, task.owner_id)
    
    async def update(self, task: Task) -> Task:
        """Actualiza una tarea existente"""
        await self.db.commit()
        await self.db.refresh(task)
        # Re-fetch to ensure tags are loaded
        return await self.get_by_id(task.id, task.owner_id)
    
    async def delete(self, task: Task) -> None:
        """Elimina una tarea"""
        await self.db.delete(task)
        await self.db.commit()
