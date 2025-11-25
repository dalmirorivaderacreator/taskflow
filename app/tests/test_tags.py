"""
Tests para los endpoints de etiquetas.
"""
import pytest
from httpx import AsyncClient


async def create_user_and_login(client: AsyncClient) -> str:
    """Helper para crear un usuario y obtener su token"""
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "username": "testuser",
            "password": "testpassword123",
            "full_name": "Test User"
        }
    )
    
    response = await client.post(
        "/api/v1/auth/login",
        data={
            "username": "testuser",
            "password": "testpassword123"
        }
    )
    
    return response.json()["access_token"]


@pytest.mark.asyncio
async def test_create_tag(client: AsyncClient):
    """Test de creación de etiqueta"""
    token = await create_user_and_login(client)
    
    response = await client.post(
        "/api/v1/tags/",
        json={
            "name": "Urgente",
            "color": "#FF0000"
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Urgente"
    assert data["color"] == "#FF0000"


@pytest.mark.asyncio
async def test_get_tags(client: AsyncClient):
    """Test de obtención de etiquetas"""
    token = await create_user_and_login(client)
    
    # Crear algunas etiquetas
    await client.post(
        "/api/v1/tags/",
        json={"name": "Tag 1", "color": "#FF0000"},
        headers={"Authorization": f"Bearer {token}"}
    )
    await client.post(
        "/api/v1/tags/",
        json={"name": "Tag 2", "color": "#00FF00"},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Obtener todas las etiquetas
    response = await client.get(
        "/api/v1/tags/",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


@pytest.mark.asyncio
async def test_create_duplicate_tag(client: AsyncClient):
    """Test de creación de etiqueta duplicada"""
    token = await create_user_and_login(client)
    
    tag_data = {"name": "Duplicate", "color": "#FF0000"}
    
    # Primera creación
    await client.post(
        "/api/v1/tags/",
        json=tag_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Segunda creación con mismo nombre
    response = await client.post(
        "/api/v1/tags/",
        json=tag_data,
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 400
