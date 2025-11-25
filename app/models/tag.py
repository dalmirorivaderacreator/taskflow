"""
Modelo de Etiqueta (Tag) para SQLAlchemy.
Define la tabla 'tags' con sus campos y relaciones.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.db.base import BaseModel
from app.models.task import task_tags


class Tag(BaseModel):
    """Modelo de etiqueta para categorizar tareas"""
    __tablename__ = "tags"
    
    name = Column(String(100), unique=True, index=True, nullable=False)
    color = Column(String(7), default="#3B82F6", nullable=False)  # Color en formato hex
    
    # Relación muchos-a-muchos con tareas
    tasks = relationship("Task", secondary=task_tags, back_populates="tags")
    
    def __repr__(self):
        return f"<Tag(id={self.id}, name={self.name})>"
