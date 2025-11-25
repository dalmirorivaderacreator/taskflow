"""
Configuración de pytest para los tests.
Define fixtures compartidas y configuración de la base de datos de prueba.
"""
import asyncio
from typing import AsyncGenerator, Generator

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.core.config import settings
from app.db.base import Base
from app.db.session import get_db
from app.main import app

# URL de base de datos de prueba (usar una BD separada)
TEST_DATABASE_URL = settings.database_url.replace("taskflow_db", "taskflow_test_db")

# Motor de prueba
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False, poolclass=NullPool)

# Session maker de prueba
TestSessionLocal = sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


# @pytest.fixture(scope="session")
# def event_loop() -> Generator:
#     """Crea un event loop para toda la sesión de tests"""
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Fixture que proporciona una sesión de base de datos limpia para cada test.
    Crea las tablas antes del test y las elimina después.
    """
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with TestSessionLocal() as session:
        yield session
    
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """
    Fixture que proporciona un cliente HTTP de prueba.
    Sobrescribe la dependencia get_db para usar la sesión de prueba.
    """
    async def override_get_db():
        yield db_session
    
    app.dependency_overrides[get_db] = override_get_db
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    
    app.dependency_overrides.clear()
