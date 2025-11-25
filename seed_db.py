"""
Script para poblar la base de datos con datos de ejemplo.
Útil para desarrollo y testing.
"""
import asyncio

from app.core.security import get_password_hash
from app.db.base import Base
from app.db.session import engine
from app.models.tag import Tag
from app.models.task import Task
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async def create_tables():
    """Crea todas las tablas en la base de datos"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tablas creadas exitosamente")


async def seed_data():
    """Inserta datos de ejemplo en la base de datos"""
    AsyncSessionLocal = sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
    async with AsyncSessionLocal() as session:
        # Crear usuarios de ejemplo
        admin_user = User(
            email="admin@taskflow.com",
            username="admin",
            hashed_password=get_password_hash("admin123"),
            full_name="Administrador",
            is_superuser=True,
        )
        
        demo_user = User(
            email="demo@taskflow.com",
            username="demo",
            hashed_password=get_password_hash("demo123"),
            full_name="Usuario Demo",
        )
        
        session.add(admin_user)
        session.add(demo_user)
        await session.flush()
        
        print("✅ Usuarios creados:")
        print(f"   - admin@taskflow.com (password: admin123)")
        print(f"   - demo@taskflow.com (password: demo123)")
        
        # Crear etiquetas de ejemplo
        tags = [
            Tag(name="Urgente", color="#FF0000"),
            Tag(name="Importante", color="#FFA500"),
            Tag(name="Personal", color="#00FF00"),
            Tag(name="Trabajo", color="#0000FF"),
            Tag(name="Ideas", color="#FF00FF"),
        ]
        
        for tag in tags:
            session.add(tag)
        
        await session.flush()
        print(f"✅ {len(tags)} etiquetas creadas")
        
        # Crear tareas de ejemplo para el usuario admin
        tasks = [
            Task(
                title="Configurar el proyecto",
                description="Instalar dependencias y configurar el entorno de desarrollo",
                priority=2,
                is_completed=True,
                owner_id=admin_user.id,
            ),
            Task(
                title="Implementar autenticación",
                description="Crear endpoints de login y registro con JWT",
                priority=2,
                is_completed=True,
                owner_id=admin_user.id,
            ),
            Task(
                title="Crear API de tareas",
                description="Implementar CRUD completo para tareas",
                priority=1,
                is_completed=False,
                owner_id=admin_user.id,
            ),
            Task(
                title="Escribir tests",
                description="Crear tests unitarios y de integración",
                priority=1,
                is_completed=False,
                owner_id=admin_user.id,
            ),
            Task(
                title="Documentar la API",
                description="Completar la documentación en Swagger",
                priority=0,
                is_completed=False,
                owner_id=admin_user.id,
            ),
        ]
        
        # Asignar etiquetas a las tareas
        tasks[0].tags = [tags[0], tags[3]]  # Urgente, Trabajo
        tasks[1].tags = [tags[0], tags[3]]  # Urgente, Trabajo
        tasks[2].tags = [tags[1], tags[3]]  # Importante, Trabajo
        tasks[3].tags = [tags[1]]           # Importante
        tasks[4].tags = [tags[3]]           # Trabajo
        
        for task in tasks:
            session.add(task)
        
        # Crear tareas para el usuario demo
        demo_tasks = [
            Task(
                title="Aprender FastAPI",
                description="Completar el tutorial oficial de FastAPI",
                priority=1,
                is_completed=False,
                owner_id=demo_user.id,
            ),
            Task(
                title="Estudiar SQLAlchemy async",
                description="Leer la documentación de SQLAlchemy 2.0",
                priority=1,
                is_completed=False,
                owner_id=demo_user.id,
            ),
            Task(
                title="Hacer ejercicio",
                description="30 minutos de cardio",
                priority=0,
                is_completed=False,
                owner_id=demo_user.id,
            ),
        ]
        
        demo_tasks[0].tags = [tags[1], tags[3]]  # Importante, Trabajo
        demo_tasks[1].tags = [tags[3]]           # Trabajo
        demo_tasks[2].tags = [tags[2]]           # Personal
        
        for task in demo_tasks:
            session.add(task)
        
        await session.commit()
        print(f"✅ {len(tasks) + len(demo_tasks)} tareas creadas")


async def main():
    """Función principal"""
    print("🚀 Iniciando población de base de datos...")
    print()
    
    # Crear tablas (opcional, si no usas Alembic)
    # await create_tables()
    
    # Insertar datos de ejemplo
    await seed_data()
    
    print()
    print("✨ ¡Base de datos poblada exitosamente!")
    print()
    print("Puedes iniciar sesión con:")
    print("  - Usuario: admin / Contraseña: admin123")
    print("  - Usuario: demo / Contraseña: demo123")


if __name__ == "__main__":
    asyncio.run(main())
