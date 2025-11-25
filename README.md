TaskFlow API 🚀
API REST production-ready para gestión de tareas con arquitectura enterprise, autenticación JWT y stack tecnológico moderno. Construida con FastAPI, SQLAlchemy 2.x async y PostgreSQL.

🎯 Características Técnicas Destacadas
🏗️ Arquitectura & Patrones
Clean Architecture - Separación clara en capas (API → Services → Repositories → Models)

Repository Pattern - Abstracción del acceso a datos para máxima testabilidad

Async/Await - SQLAlchemy 2.x asíncrono para alto rendimiento

Dependency Injection - Gestión automática de dependencias con FastAPI

🛡️ Seguridad & Autenticación
JWT Tokens - Autenticación stateless con tiempos de expiración

Argon2 Password Hashing - Hashing seguro de contraseñas

Middleware de Autenticación - Protección automática de endpoints

Variables de Entorno - Configuración segura fuera del código

📦 DevOps & Deployment
Docker & Docker Compose - Containerización completa

Alembic Migrations - Control de versiones de base de datos

PostgreSQL - Base de datos production-ready

Configuración por Ambiente - Dev/Staging/Production

🚀 Quick Start
Con Docker (Recomendado - 3 comandos)
bash
git clone https://github.com/dalmirorivaderacreator/taskflow.git
cd taskflow
docker-compose up -d
¡Listo! La API estará disponible en:

📚 Swagger UI: http://localhost:8000/docs

📖 ReDoc: http://localhost:8000/redoc

Sin Docker
bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
🏗️ Estructura del Proyecto
text
taskflow/
├── app/
│   ├── api/v1/          # → Endpoints REST
│   │   ├── auth.py      # 🔐 Autenticación
│   │   ├── tasks.py     # ✅ Gestión de tareas  
│   │   ├── users.py     # 👥 Gestión de usuarios
│   │   └── tags.py      # 🏷️ Gestión de etiquetas
│   ├── services/        # → Lógica de negocio
│   ├── repositories/    # → Acceso a datos (Repository Pattern)
│   ├── models/          # → Modelos SQLAlchemy
│   ├── schemas/         # → Schemas Pydantic
│   └── core/            # → Configuración y seguridad
├── migrations/          # 📊 Migraciones de Alembic
├── docker-compose.yml   # 🐳 Orquestación de containers
└── requirements.txt     # 📦 Dependencias
💡 Casos de Uso Implementados
1. Gestión Completa de Tareas
python
# Crear tarea con prioridad y etiquetas
POST /api/v1/tasks/
{
  "title": "Implementar feature XYZ",
  "description": "Desarrollar sistema de notificaciones",
  "priority": 2,
  "tag_ids": [1, 3]
}
2. Sistema de Etiquetas y Categorización
python
# Organizar tareas por categorías
POST /api/v1/tags/
{
  "name": "Urgente",
  "color": "#FF6B6B"
}
3. Autenticación Segura
python
# Login con credenciales seguras
POST /api/v1/auth/login
username=usuario&password=contraseña
→ Retorna JWT token para requests autenticados
🔧 Stack Tecnológico
Categoría	Tecnologías
Framework	FastAPI, Pydantic
Database	PostgreSQL, SQLAlchemy 2.x Async
ORM	SQLAlchemy, Alembic
Seguridad	JWT, Argon2, Python-jose
DevOps	Docker, Docker Compose
Arquitectura	Repository Pattern, Clean Architecture
📊 Endpoints Principales
Método	Endpoint	Función	Autenticación
POST	/auth/register	Registro de usuario	❌
POST	/auth/login	Login y obtención de JWT	❌
GET	/tasks/	Listar tareas del usuario	✅
POST	/tasks/	Crear nueva tarea	✅
PUT	/tasks/{id}	Actualizar tarea	✅
DELETE	/tasks/{id}	Eliminar tarea	✅
GET	/tags/	Listar etiquetas	✅
🐳 Comandos Docker Esenciales
bash
# Desarrollo
docker-compose up -d          # Levantar servicios
docker-compose logs -f api    # Ver logs en tiempo real
docker-compose exec api bash  # Acceder al container

# Base de datos  
docker-compose exec db psql -U taskflow_user -d taskflow_db

# Migraciones
docker-compose exec api alembic upgrade head
docker-compose exec api alembic revision --autogenerate -m "descripción"
🎯 Características para Reclutadores
Habilidades Demostradas:
✅ Arquitectura de Software - Patrones enterprise (Repository, Clean Architecture)

✅ APIs REST - Diseño de endpoints RESTful con FastAPI

✅ Base de Datos - PostgreSQL con ORM asíncrono

✅ Seguridad - JWT, hashing de contraseñas, middleware

✅ DevOps - Docker, containerización, despliegue

✅ Code Quality - Type hints, estructura modular, documentación

Diferenciales Técnicos:
Async/Await - Uso de SQLAlchemy 2.x asíncrono para performance

Repository Pattern - Abstracción que facilita testing y mantenibilidad

Configuración por Ambiente - Preparado para diferentes entornos

Migraciones Automatizadas - Alembic para evolución de schema

🔄 Flujo de Desarrollo
Modificar modelos en app/models/

Generar migración: alembic revision --autogenerate -m "desc"

Aplicar migración: alembic upgrade head

Desarrollar endpoints en app/api/v1/

Probar en Swagger: http://localhost:8000/docs

👨‍💻 Autor
Dalmiro Rivadera - GitHub

"Este proyecto demuestra capacidad para construir APIs production-ready con arquitecturas escalables y mejores prácticas de desarrollo."

📄 Licencia
MIT License - ver archivo LICENSE para detalles.
Este proyecto está bajo licencia MIT.

👨‍💻 Autor
Dalmiro Rivadera
Desarrollado como proyecto base para aplicaciones FastAPI con SQLAlchemy async.
