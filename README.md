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

🎯 ¿Por qué este proyecto destaca?
🚀 Production-Ready - Containerizado y con configuración para diferentes entornos

🏗️ Arquitectura Empresarial - Patrones que escalan en proyectos reales

🔧 Stack Moderno - FastAPI + SQLAlchemy async = alto rendimiento

📚 Documentación Completa - Incluye Swagger UI automática

¡Perfecto para demostrar habilidades de Backend Developer en procesos de reclutamiento!

¿Te gusta esta versión? Puedo ayudarte a:

Agregar una sección de "Logros Técnicos"

Incluir métricas de performance

Agregar diagramas de arquitectura

Preparar el README para subir a GitHub

me quedo muy mal acomodado en github, adaptalo al formato github
TaskFlow API 🚀
API REST production-ready para gestión de tareas con arquitectura enterprise, autenticación JWT y stack tecnológico moderno.

🎯 Características
🏗️ Arquitectura & Patrones
Clean Architecture - Separación clara en capas

Repository Pattern - Abstracción del acceso a datos

Async/Await - SQLAlchemy 2.x asíncrono para alto rendimiento

Dependency Injection - Gestión automática de dependencias

🛡️ Seguridad & Autenticación
JWT Tokens - Autenticación stateless

Argon2 Password Hashing - Hashing seguro de contraseñas

Middleware de Autenticación - Protección automática de endpoints

📦 DevOps & Deployment
Docker & Docker Compose - Containerización completa

Alembic Migrations - Control de versiones de base de datos

PostgreSQL - Base de datos production-ready

🚀 Quick Start
Con Docker (Recomendado)
bash
# 1. Clonar repositorio
git clone https://github.com/dalmirorivaderacreator/taskflow.git
cd taskflow

# 2. Levantar servicios
docker-compose up -d

# 3. Aplicar migraciones
docker-compose exec api alembic upgrade head
¡Listo! La API estará disponible en:

📚 Swagger UI: http://localhost:8000/docs

📖 ReDoc: http://localhost:8000/redoc

Desarrollo Local
bash
# 1. Entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar PostgreSQL y variables de entorno
cp .env.example .env
# Editar .env con tus credenciales

# 4. Migraciones y ejecución
alembic upgrade head
uvicorn app.main:app --reload
🏗️ Estructura del Proyecto
text
taskflow/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py      # 🔐 Autenticación
│   │       ├── tasks.py     # ✅ Gestión de tareas
│   │       ├── users.py     # 👥 Usuarios
│   │       └── tags.py      # 🏷️ Etiquetas
│   ├── core/
│   │   ├── config.py        # ⚙️ Configuración
│   │   └── security.py      # 🔒 Seguridad
│   ├── db/
│   │   ├── base.py          # 🗄️ Base declarativa
│   │   └── session.py       # 🔌 Sesión async
│   ├── models/
│   │   ├── user.py          # 👤 Modelo Usuario
│   │   ├── task.py          # 📝 Modelo Tarea
│   │   └── tag.py           # 🏷️ Modelo Etiqueta
│   ├── repositories/
│   │   ├── user_repo.py     # 📊 Repositorio Users
│   │   ├── task_repo.py     # 📋 Repositorio Tasks
│   │   └── tag_repo.py      # 🏷️ Repositorio Tags
│   ├── schemas/
│   │   ├── user.py          # 📝 Schemas Users
│   │   ├── task.py          # 📋 Schemas Tasks
│   │   └── tag.py           # 🏷️ Schemas Tags
│   ├── services/
│   │   ├── auth_service.py  # 🔐 Servicio Auth
│   │   ├── user_service.py  # 👥 Servicio Users
│   │   └── task_service.py  # ✅ Servicio Tasks
│   └── main.py              # 🎯 App principal
├── migrations/              # 📊 Migraciones Alembic
├── docker-compose.yml       # 🐳 Docker Compose
├── Dockerfile              # 🐳 Docker
├── requirements.txt        # 📦 Dependencias
└── README.md              # 📚 Este archivo
💡 Uso de la API
1. Registrar Usuario
bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@ejemplo.com",
    "username": "usuario",
    "password": "password123",
    "full_name": "Usuario Ejemplo"
  }'
2. Login y Obtener Token
bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=usuario&password=password123"
Respuesta:

json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
3. Crear Tarea (Autenticado)
bash
curl -X POST "http://localhost:8000/api/v1/tasks/" \
  -H "Authorization: Bearer TU_TOKEN_JWT" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implementar feature XYZ",
    "description": "Desarrollar sistema de notificaciones",
    "priority": 2,
    "tag_ids": [1, 3]
  }'
🔧 Stack Tecnológico
Categoría	Tecnologías
Framework	FastAPI, Pydantic
Database	PostgreSQL, SQLAlchemy 2.x Async
ORM	SQLAlchemy, Alembic
Seguridad	JWT, Argon2, Python-jose
DevOps	Docker, Docker Compose
Arquitectura	Repository Pattern, Clean Architecture
📊 Endpoints Principales
Método	Endpoint	Función	Auth
POST	/auth/register	Registro	❌
POST	/auth/login	Login	❌
GET	/tasks/	Listar tareas	✅
POST	/tasks/	Crear tarea	✅
PUT	/tasks/{id}	Actualizar tarea	✅
DELETE	/tasks/{id}	Eliminar tarea	✅
GET	/tags/	Listar etiquetas	✅
🐳 Comandos Docker Útiles
bash
# Desarrollo
docker-compose up -d          # Levantar servicios
docker-compose logs -f api    # Ver logs en tiempo real
docker-compose down           # Detener servicios

# Base de datos
docker-compose exec db psql -U taskflow_user -d taskflow_db

# Migraciones
docker-compose exec api alembic upgrade head
docker-compose exec api alembic revision --autogenerate -m "descripción"

# Contenedores
docker-compose exec api bash  # Acceder al container API
🗄️ Migraciones de Base de Datos
bash
# Crear nueva migración
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar migraciones
alembic upgrade head

# Revertir migración
alembic downgrade -1

# Ver historial
alembic history
🔐 Variables de Entorno
Copia .env.example a .env y configura:

env
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost/taskflow_db

# Security
SECRET_KEY=tu-clave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# App
DEBUG=True
🧪 Testing
bash
# Ejecutar tests
pytest

# Con cobertura
pytest --cov=app --cov-report=html

# Tests específicos
pytest tests/ -v
🎯 Habilidades Demostradas
✅ Arquitectura de Software - Clean Architecture, Repository Pattern

✅ APIs REST - FastAPI, endpoints RESTful, documentación automática

✅ Base de Datos - PostgreSQL, SQLAlchemy Async, migraciones

✅ Seguridad - JWT, Argon2, autenticación stateless

✅ DevOps - Docker, containerización, despliegue

✅ Code Quality - Type hints, estructura modular, async/await

👨‍💻 Autor
Dalmiro Rivadera - GitHub

📄 Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

⭐ ¡Dale una estrella al repositorio!
Si este proyecto te resulta útil, ¡considera darle una estrella en GitHub!

¿Problemas? Abre un issue en GitHub.

¿Mejoras? ¡Los pull requests son bienvenidos!

<div align="center">
¡Construido con ❤️ y FastAPI!

</div>
