"""
Modelo de Usuario para SQLAlchemy.
Define la tabla 'users' con sus campos y relaciones.
"""
from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.db.base import BaseModel


class User(BaseModel):
    """Modelo de usuario del sistema"""
    __tablename__ = "users"
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    
    # Relación con tareas (un usuario tiene muchas tareas)
    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
