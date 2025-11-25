"""
Repositorio para operaciones de base de datos relacionadas con etiquetas.
Abstrae las queries de SQLAlchemy.
"""
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.tag import Tag


class TagRepository:
    """Repositorio para gestionar operaciones CRUD de etiquetas"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_by_id(self, tag_id: int) -> Optional[Tag]:
        """Obtiene una etiqueta por su ID"""
        result = await self.db.execute(select(Tag).where(Tag.id == tag_id))
        return result.scalar_one_or_none()
    
    async def get_by_name(self, name: str) -> Optional[Tag]:
        """Obtiene una etiqueta por su nombre"""
        result = await self.db.execute(select(Tag).where(Tag.name == name))
        return result.scalar_one_or_none()
    
    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Tag]:
        """Obtiene todas las etiquetas con paginación"""
        result = await self.db.execute(
            select(Tag).offset(skip).limit(limit)
        )
        return result.scalars().all()
    
    async def get_by_ids(self, tag_ids: List[int]) -> List[Tag]:
        """Obtiene múltiples etiquetas por sus IDs"""
        result = await self.db.execute(
            select(Tag).where(Tag.id.in_(tag_ids))
        )
        return result.scalars().all()
    
    async def create(self, tag: Tag) -> Tag:
        """Crea una nueva etiqueta"""
        self.db.add(tag)
        await self.db.commit()
        await self.db.refresh(tag)
        return tag
    
    async def update(self, tag: Tag) -> Tag:
        """Actualiza una etiqueta existente"""
        await self.db.commit()
        await self.db.refresh(tag)
        return tag
    
    async def delete(self, tag: Tag) -> None:
        """Elimina una etiqueta"""
        await self.db.delete(tag)
        await self.db.commit()
