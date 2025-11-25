# TaskFlow API

**TaskFlow** es una API REST para la gestión eficiente de tareas, con soporte para autenticación segura mediante JWT, etiquetas, prioridades y arquitectura moderna basada en FastAPI y SQLAlchemy asíncrono.

---

## 🚀 Características Principales

- **FastAPI**: Framework moderno y ultra rápido para APIs.
- **SQLAlchemy 2.x async**: ORM asíncrono para mejor rendimiento.
- **PostgreSQL**: Base de datos relacional robusta.
- **Alembic**: Migraciones automáticas de base de datos.
- **JWT Authentication**: Seguridad con tokens.
- **Docker & Docker Compose**: Fácil despliegue containerizado.
- **Arquitectura limpia**: Separación clara en capas (API, servicios, repositorios, modelos).

---

## 📦 Requisitos Previos

- Docker y Docker Compose (recomendado)
- O bien, Python 3.11+ y PostgreSQL 15+ instalados localmente

---

## ⚙️ Instalación y Configuración

### Opción 1: Usando Docker (Recomendado)

1. Clonar el repositorio y entrar al directorio:
   ```bash
   git clone https://github.com/tu_usuario/taskflow.git
   cd taskflow
Levantar servicios con Docker Compose:

bash
Copiar código
docker-compose up -d
Crear y aplicar migraciones:

bash
Copiar código
docker-compose exec api alembic revision --autogenerate -m "Initial migration"
docker-compose exec api alembic upgrade head
Acceder a la API en:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

Opción 2: Desarrollo Local (sin Docker)
Crear y activar un entorno virtual:

bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Configurar PostgreSQL:

Crear base de datos taskflow_db

Crear usuario taskflow_user con contraseña taskflow_password

## Configuración del entorno

Para correr el proyecto, copia el archivo `.env.example` y renómbralo a `.env`, luego edita las variables con los valores correspondientes:

```bash
cp .env.example .env

Crear y aplicar migraciones:

bash
Copiar código
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
Ejecutar la aplicación:

bash
Copiar código
uvicorn app.main:app --reload
🌐 Uso de la API
Registrar un usuario
bash
Copiar código
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "username": "usuario",
    "password": "password123",
    "full_name": "Usuario Ejemplo"
  }'
Iniciar sesión
bash
Copiar código
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=usuario&password=password123"
Respuesta:

json
Copiar código
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
Crear una tarea (requiere autenticación)
bash
Copiar código
curl -X POST "http://localhost:8000/api/v1/tasks/" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi primera tarea",
    "description": "Descripción de la tarea",
    "priority": 1,
    "tag_ids": []
  }'
Obtener todas las tareas (requiere autenticación)
bash
Copiar código
curl -X GET "http://localhost:8000/api/v1/tasks/" \
  -H "Authorization: Bearer TU_TOKEN_AQUI"
Crear una etiqueta (requiere autenticación)
bash
Copiar código
curl -X POST "http://localhost:8000/api/v1/tags/" \
  -H "Authorization: Bearer TU_TOKEN_AQUI" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Urgente",
    "color": "#FF0000"
  }'
🧪 Testing
Ejecutar tests (cuando estén implementados):

bash
Copiar código
pytest
Con reporte de cobertura:

bash
Copiar código
pytest --cov=app --cov-report=html
🔐 Seguridad
Contraseñas con hashing Argon2

Tokens JWT con expiración configurable (por defecto 30 minutos)

IMPORTANTE: Cambiar SECRET_KEY en producción para mayor seguridad

🗄️ Migraciones de Base de Datos
Crear nueva migración:

bash
Copiar código
alembic revision --autogenerate -m "Descripción del cambio"
Aplicar migraciones:

bash
Copiar código
alembic upgrade head
Revertir última migración:

bash
Copiar código
alembic downgrade -1
Ver historial:

bash
Copiar código
alembic history
🐳 Comandos Docker útiles
bash
Copiar código
# Levantar servicios
docker-compose up -d

# Ver logs del API
docker-compose logs -f api

# Detener servicios
docker-compose down

# Reconstruir imagen
docker-compose build

# Acceder al contenedor API
docker-compose exec api bash

# Acceder a PostgreSQL
docker-compose exec db psql -U taskflow_user -d taskflow_db
🏗️ Arquitectura
El proyecto está organizado en capas:

API Layer (app/api/): Endpoints y validación

Service Layer (app/services/): Lógica de negocio

Repository Layer (app/repositories/): Acceso a datos

Model Layer (app/models/): Modelos ORM

Schema Layer (app/schemas/): Validación con Pydantic

🤝 Contribuir
Haz fork del proyecto

Crea una rama para tu feature (git checkout -b feature/nombre)

Realiza commits claros y descriptivos

Envía un pull request para revisión

📄 Licencia
Este proyecto está bajo licencia MIT.

👨‍💻 Autor - Dalmiro Rivadera
Desarrollado como proyecto base para aplicaciones FastAPI con SQLAlchemy async.

¡Gracias por usar TaskFlow! 🚀