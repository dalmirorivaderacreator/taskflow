"""
Configuración de la sesión asíncrona de SQLAlchemy.
Crea el engine async y el session maker.
"""
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Motor asíncrono de SQLAlchemy con asyncpg
engine = create_async_engine(
    settings.database_url,
    echo=settings.DEBUG,  # Log de queries SQL en modo debug
    future=True,
    pool_pre_ping=True,  # Verifica conexiones antes de usarlas
)

# Session maker asíncrono
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncSession:
    """
    Dependency para obtener una sesión de base de datos.
    Se usa en FastAPI con Depends(get_db).
    
    Yields:
        AsyncSession: Sesión de base de datos asíncrona
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
