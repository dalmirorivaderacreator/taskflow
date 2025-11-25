# TaskFlow API

**TaskFlow** es una API REST moderna para la gestión eficiente de tareas, con soporte para autenticación segura mediante JWT, etiquetas, prioridades y una arquitectura limpia basada en FastAPI y SQLAlchemy asíncrono.

---

## 🚀 Características principales

* **FastAPI**: Framework rápido y moderno para APIs.
* **SQLAlchemy 2.x async**: ORM asíncrono para mejor rendimiento.
* **PostgreSQL**: Base de datos relacional robusta y escalable.
* **Alembic**: Migraciones automáticas de base de datos.
* **JWT Authentication**: Seguridad basada en tokens con expiración configurable.
* **Docker & Docker Compose**: Despliegue containerizado fácil y reproducible.
* **Arquitectura limpia**: Separación clara en capas (API, servicios, repositorios, modelos).
* **Seguridad**: Hashing de contraseñas con Argon2.

---

## 📦 Requisitos previos

* **Opción recomendada:** Docker y Docker Compose instalados.
* **Alternativa:** Python 3.11+ y PostgreSQL 15+ instalados localmente.

---

## ⚙️ Instalación y configuración

### Opción 1: Usando Docker (Recomendado)

```bash
# Clonar repositorio
git clone https://github.com/tu_usuario/taskflow.git
cd taskflow

# Levantar servicios en segundo plano
docker-compose up -d

# Crear y aplicar migraciones
docker-compose exec api alembic revision --autogenerate -m "Initial migration"
docker-compose exec api alembic upgrade head
```

* Accede a la documentación interactiva en:

  * Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
  * ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### Opción 2: Desarrollo local (sin Docker)

```bash
# Crear y activar entorno virtual
python -m venv venv

# Windows (PowerShell)
venv\Scripts\activate

# Linux/macOS (bash)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

* Configura PostgreSQL creando base de datos y usuario:

```sql
CREATE DATABASE taskflow_db;
CREATE USER taskflow_user WITH PASSWORD 'taskflow_password';
GRANT ALL PRIVILEGES ON DATABASE taskflow_db TO taskflow_user;
```

* Copia y edita variables de entorno:

```bash
cp .env.example .env
# Edita .env con tus valores
```

* Ejecuta migraciones:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

* Ejecuta la aplicación:

```bash
uvicorn app.main:app --reload
```

---

## 🌐 Uso básico de la API

### Registrar usuario

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
-H "Content-Type: application/json" \
-d '{ "email": "usuario@example.com", "username": "usuario", "password": "password123", "full_name": "Usuario Ejemplo" }'
```

### Iniciar sesión

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=usuario&password=password123"
```

Respuesta esperada:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Crear tarea (requiere token)

```bash
curl -X POST "http://localhost:8000/api/v1/tasks/" \
-H "Authorization: Bearer TU_TOKEN_AQUI" \
-H "Content-Type: application/json" \
-d '{ "title": "Mi primera tarea", "description": "Descripción de la tarea", "priority": 1, "tag_ids": [] }'
```

### Listar tareas (requiere token)

```bash
curl -X GET "http://localhost:8000/api/v1/tasks/" \
-H "Authorization: Bearer TU_TOKEN_AQUI"
```

### Crear etiqueta (requiere token)

```bash
curl -X POST "http://localhost:8000/api/v1/tags/" \
-H "Authorization: Bearer TU_TOKEN_AQUI" \
-H "Content-Type: application/json" \
-d '{ "name": "Urgente", "color": "#FF0000" }'
```

---

## 🧪 Testing

* Ejecutar tests:

```bash
pytest
```

* Ejecutar tests con reporte de cobertura:

```bash
pytest --cov=app --cov-report=html
```

---

## 🔐 Seguridad

* Hashing de contraseñas con **Argon2**.
* Tokens JWT con expiración configurable (por defecto 30 minutos).
* **IMPORTANTE:** Cambiar `SECRET_KEY` en producción para mayor seguridad.

---

## 🗄️ Migraciones de base de datos

* Crear migración:

```bash
alembic revision --autogenerate -m "Descripción del cambio"
```

* Aplicar migraciones:

```bash
alembic upgrade head
```

* Revertir última migración:

```bash
alembic downgrade -1
```

* Ver historial de migraciones:

```bash
alembic history
```

---

## 🐳 Comandos Docker útiles

```bash
# Levantar servicios
docker-compose up -d

# Ver logs de la API
docker-compose logs -f api

# Detener servicios
docker-compose down

# Reconstruir imagen
docker-compose build

# Acceder al contenedor API
docker-compose exec api bash

# Acceder a PostgreSQL
docker-compose exec db psql -U taskflow_user -d taskflow_db
```

---

## 🏗️ Arquitectura

* **API Layer:** Endpoints y validación (`app/api/`)
* **Service Layer:** Lógica de negocio (`app/services/`)
* **Repository Layer:** Acceso a datos (`app/repositories/`)
* **Model Layer:** Modelos ORM (`app/models/`)
* **Schema Layer:** Validación con Pydantic (`app/schemas/`)

---

## 🤝 Contribuir

1. Haz fork del proyecto.
2. Crea una rama para tu feature: `git checkout -b feature/nombre`.
3. Realiza commits claros y descriptivos.
4. Envía un pull request para revisión.

---

## 📄 Licencia

Este proyecto está bajo licencia **MIT**.

---

## 👨‍💻 Autor

Dalmiro Rivadera
Desarrollado como proyecto base para aplicaciones FastAPI con SQLAlchemy async.

---

¡Gracias por usar **TaskFlow**! 🚀
