"""
Modelo de Tarea para SQLAlchemy.
Define la tabla 'tasks' con sus campos y relaciones.
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship

from app.db.base import Base, BaseModel

# Tabla de asociación muchos-a-muchos entre Task y Tag
task_tags = Table(
    "task_tags",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class Task(BaseModel):
    """Modelo de tarea del sistema"""
    __tablename__ = "tasks"
    
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False, nullable=False)
    priority = Column(Integer, default=0, nullable=False)  # 0=baja, 1=media, 2=alta
    
    # Foreign key al usuario propietario
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    # Relaciones
    owner = relationship("User", back_populates="tasks")
    tags = relationship("Tag", secondary=task_tags, back_populates="tasks")
    
    def __repr__(self):
        return f"<Task(id={self.id}, title={self.title}, completed={self.is_completed})>"
