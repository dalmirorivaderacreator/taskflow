"""
Servicio de tareas.
Maneja la lógica de negocio relacionada con tareas.
"""
from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import Task
from app.repositories.tag_repo import TagRepository
from app.repositories.task_repo import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Servicio para gestionar la lógica de negocio de tareas"""
    
    def __init__(self, db: AsyncSession):
        self.task_repo = TaskRepository(db)
        self.tag_repo = TagRepository(db)
    
    async def get_task_by_id(self, task_id: int, owner_id: int) -> Optional[Task]:
        """Obtiene una tarea por su ID verificando que pertenezca al usuario"""
        return await self.task_repo.get_by_id(task_id, owner_id)
    
    async def get_user_tasks(self, owner_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        """Obtiene todas las tareas de un usuario"""
        return await self.task_repo.get_all_by_owner(owner_id, skip, limit)
    
    async def create_task(self, task_data: TaskCreate, owner_id: int) -> Task:
        """Crea una nueva tarea"""
        # Crear la tarea
        task = Task(
            title=task_data.title,
            description=task_data.description,
            priority=task_data.priority,
            is_completed=task_data.is_completed,
            owner_id=owner_id,
        )
        
        # Asociar tags si se proporcionaron
        if task_data.tag_ids:
            tags = await self.tag_repo.get_by_ids(task_data.tag_ids)
            task.tags = tags
        
        return await self.task_repo.create(task)
    
    async def update_task(self, task_id: int, task_data: TaskUpdate, owner_id: int) -> Task:
        """Actualiza una tarea existente"""
        task = await self.task_repo.get_by_id(task_id, owner_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tarea no encontrada"
            )
        
        # Actualizar campos si se proporcionan
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.priority is not None:
            task.priority = task_data.priority
        if task_data.is_completed is not None:
            task.is_completed = task_data.is_completed
        
        # Actualizar tags si se proporcionaron
        if task_data.tag_ids is not None:
            tags = await self.tag_repo.get_by_ids(task_data.tag_ids)
            task.tags = tags
        
        return await self.task_repo.update(task)
    
    async def delete_task(self, task_id: int, owner_id: int) -> None:
        """Elimina una tarea"""
        task = await self.task_repo.get_by_id(task_id, owner_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tarea no encontrada"
            )
        
        await self.task_repo.delete(task)
