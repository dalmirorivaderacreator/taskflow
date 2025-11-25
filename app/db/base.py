"""
Clase base para todos los modelos SQLAlchemy.
Define la base declarativa y campos comunes.
"""
from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import declarative_base

# Base declarativa para todos los modelos
Base = declarative_base()


class BaseModel(Base):
    """
    Modelo base abstracto con campos comunes para todas las tablas.
    Incluye id, created_at y updated_at.
    """
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
