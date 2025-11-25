"""
Tests para los endpoints de tareas.
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
async def test_create_task(client: AsyncClient):
    """Test de creación de tarea"""
    token = await create_user_and_login(client)
    
    response = await client.post(
        "/api/v1/tasks/",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "priority": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["priority"] == 1
    assert data["is_completed"] is False


@pytest.mark.asyncio
async def test_get_tasks(client: AsyncClient):
    """Test de obtención de tareas"""
    token = await create_user_and_login(client)
    
    # Crear algunas tareas
    await client.post(
        "/api/v1/tasks/",
        json={"title": "Task 1", "priority": 0},
        headers={"Authorization": f"Bearer {token}"}
    )
    await client.post(
        "/api/v1/tasks/",
        json={"title": "Task 2", "priority": 1},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    # Obtener todas las tareas
    response = await client.get(
        "/api/v1/tasks/",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


@pytest.mark.asyncio
async def test_update_task(client: AsyncClient):
    """Test de actualización de tarea"""
    token = await create_user_and_login(client)
    
    # Crear tarea
    create_response = await client.post(
        "/api/v1/tasks/",
        json={"title": "Original Title", "priority": 0},
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = create_response.json()["id"]
    
    # Actualizar tarea
    response = await client.put(
        f"/api/v1/tasks/{task_id}",
        json={"title": "Updated Title", "is_completed": True},
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["is_completed"] is True


@pytest.mark.asyncio
async def test_delete_task(client: AsyncClient):
    """Test de eliminación de tarea"""
    token = await create_user_and_login(client)
    
    # Crear tarea
    create_response = await client.post(
        "/api/v1/tasks/",
        json={"title": "Task to Delete", "priority": 0},
        headers={"Authorization": f"Bearer {token}"}
    )
    task_id = create_response.json()["id"]
    
    # Eliminar tarea
    response = await client.delete(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == 204
    
    # Verificar que no existe
    get_response = await client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert get_response.status_code == 404
