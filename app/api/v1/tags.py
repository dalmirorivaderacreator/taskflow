"""
Endpoints de etiquetas.
Incluye operaciones CRUD para gestionar etiquetas.
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.tag import Tag
from app.models.user import User
from app.repositories.tag_repo import TagRepository
from app.schemas.tag import TagCreate, TagResponse, TagUpdate

router = APIRouter()


@router.get("/", response_model=List[TagResponse])
async def get_tags(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Obtiene todas las etiquetas disponibles.
    """
    tag_repo = TagRepository(db)
    tags = await tag_repo.get_all(skip, limit)
    return tags


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
async def create_tag(
    tag_data: TagCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Crea una nueva etiqueta.
    """
    tag_repo = TagRepository(db)
    
    # Verificar que no exista una etiqueta con el mismo nombre
    existing_tag = await tag_repo.get_by_name(tag_data.name)
    if existing_tag:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una etiqueta con ese nombre"
        )
    
    tag = Tag(name=tag_data.name, color=tag_data.color)
    tag = await tag_repo.create(tag)
    return tag


@router.put("/{tag_id}", response_model=TagResponse)
async def update_tag(
    tag_id: int,
    tag_data: TagUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Actualiza una etiqueta existente.
    """
    tag_repo = TagRepository(db)
    tag = await tag_repo.get_by_id(tag_id)
    
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Etiqueta no encontrada"
        )
    
    if tag_data.name is not None:
        tag.name = tag_data.name
    if tag_data.color is not None:
        tag.color = tag_data.color
    
    tag = await tag_repo.update(tag)
    return tag


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tag(
    tag_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Elimina una etiqueta.
    """
    tag_repo = TagRepository(db)
    tag = await tag_repo.get_by_id(tag_id)
    
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Etiqueta no encontrada"
        )
    
    await tag_repo.delete(tag)
    return None
