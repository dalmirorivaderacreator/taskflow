# 🚀 Guía Rápida de Inicio - TaskFlow API

## Comandos para Levantar el Proyecto

### Opción 1: Con Docker (Más Fácil) 🐳

```bash
# 1. Navegar a la carpeta del proyecto
cd "c:\Users\Noxi-PC\Desktop\CARRERA EN TECNOLOGIA\PROYECTO COMODIN PARA JOBS\taskflow"

# 2. Levantar los contenedores (PostgreSQL + API)
docker-compose up -d

# 3. Esperar unos segundos y crear la migración inicial
docker-compose exec api alembic revision --autogenerate -m "Initial migration"

# 4. Aplicar las migraciones a la base de datos
docker-compose exec api alembic upgrade head

# 5. ¡Listo! La API está corriendo en http://localhost:8000
# Documentación: http://localhost:8000/docs
```

### Opción 2: Sin Docker (Desarrollo Local) 💻

```bash
# 1. Navegar a la carpeta del proyecto
cd "c:\Users\Noxi-PC\Desktop\CARRERA EN TECNOLOGIA\PROYECTO COMODIN PARA JOBS\taskflow"

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual (Windows)
venv\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Asegurarse de que PostgreSQL esté corriendo y crear la base de datos
# Puedes usar pgAdmin o psql:
# psql -U postgres
# CREATE DATABASE taskflow_db;
# CREATE USER taskflow_user WITH PASSWORD 'taskflow_password';
# GRANT ALL PRIVILEGES ON DATABASE taskflow_db TO taskflow_user;

# 6. Crear la migración inicial
alembic revision --autogenerate -m "Initial migration"

# 7. Aplicar las migraciones
alembic upgrade head

# 8. Ejecutar la aplicación
uvicorn app.main:app --reload

# 9. ¡Listo! La API está corriendo en http://localhost:8000
# Documentación: http://localhost:8000/docs
```

## Probar la API

### 1. Registrar un usuario

Ir a http://localhost:8000/docs y usar el endpoint `POST /api/v1/auth/register`:

```json
{
  "email": "admin@taskflow.com",
  "username": "admin",
  "password": "admin123",
  "full_name": "Administrador"
}
```

### 2. Iniciar sesión

Usar el endpoint `POST /api/v1/auth/login`:

```
username: admin
password: admin123
```

Copiar el `access_token` de la respuesta.

### 3. Autorizar en Swagger

Hacer clic en el botón "Authorize" en la esquina superior derecha de Swagger UI y pegar el token.

### 4. Crear una tarea

Usar el endpoint `POST /api/v1/tasks/`:

```json
{
  "title": "Mi primera tarea",
  "description": "Aprender FastAPI y SQLAlchemy",
  "priority": 2,
  "tag_ids": []
}
```

### 5. Crear una etiqueta

Usar el endpoint `POST /api/v1/tags/`:

```json
{
  "name": "Urgente",
  "color": "#FF0000"
}
```

## Comandos Útiles

### Docker

```bash
# Ver logs de la API
docker-compose logs -f api

# Ver logs de PostgreSQL
docker-compose logs -f db

# Reiniciar servicios
docker-compose restart

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (CUIDADO: borra la BD)
docker-compose down -v

# Reconstruir la imagen
docker-compose build --no-cache
```

### Alembic (Migraciones)

```bash
# Ver historial de migraciones
alembic history

# Ver migración actual
alembic current

# Crear nueva migración
alembic revision --autogenerate -m "Descripción del cambio"

# Aplicar todas las migraciones
alembic upgrade head

# Revertir última migración
alembic downgrade -1

# Revertir a una migración específica
alembic downgrade <revision_id>
```

### Testing

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con verbose
pytest -v

# Ejecutar un archivo específico
pytest app/tests/test_auth.py

# Ejecutar con cobertura
pytest --cov=app --cov-report=html

# Ver reporte de cobertura
# Abrir: htmlcov/index.html
```

## Estructura de Archivos Creados

```
taskflow/
├── .env                          ✅ Variables de entorno
├── .gitignore                    ✅ Archivos ignorados por Git
├── README.md                     ✅ Documentación principal
├── requirements.txt              ✅ Dependencias Python
├── alembic.ini                   ✅ Configuración de Alembic
├── Dockerfile                    ✅ Imagen Docker de la API
├── docker-compose.yml            ✅ Orquestación de servicios
├── migrations/                   ✅ Carpeta de migraciones
│   ├── env.py                    ✅ Configuración async de Alembic
│   ├── script.py.mako            ✅ Template de migraciones
│   └── versions/                 ✅ Versiones de migraciones
├── app/
│   ├── __init__.py               ✅
│   ├── main.py                   ✅ Aplicación FastAPI
│   ├── core/
│   │   ├── config.py             ✅ Configuración
│   │   └── security.py           ✅ JWT y hashing
│   ├── db/
│   │   ├── base.py               ✅ Base declarativa
│   │   └── session.py            ✅ Sesión async
│   ├── models/
│   │   ├── user.py               ✅ Modelo Usuario
│   │   ├── task.py               ✅ Modelo Tarea
│   │   └── tag.py                ✅ Modelo Etiqueta
│   ├── schemas/
│   │   ├── user.py               ✅ Schemas Usuario
│   │   ├── task.py               ✅ Schemas Tarea
│   │   └── tag.py                ✅ Schemas Etiqueta
│   ├── repositories/
│   │   ├── user_repo.py          ✅ Repositorio Usuario
│   │   ├── task_repo.py          ✅ Repositorio Tarea
│   │   └── tag_repo.py           ✅ Repositorio Etiqueta
│   ├── services/
│   │   ├── auth_service.py       ✅ Servicio Auth
│   │   ├── user_service.py       ✅ Servicio Usuario
│   │   └── task_service.py       ✅ Servicio Tarea
│   ├── api/
│   │   ├── deps.py               ✅ Dependencias
│   │   └── v1/
│   │       ├── __init__.py       ✅
│   │       ├── auth.py           ✅ Endpoints Auth
│   │       ├── users.py          ✅ Endpoints Usuario
│   │       ├── tasks.py          ✅ Endpoints Tarea
│   │       └── tags.py           ✅ Endpoints Etiqueta
│   └── tests/
│       ├── __init__.py           ✅
│       ├── conftest.py           ✅ Configuración pytest
│       ├── test_auth.py          ✅ Tests Auth
│       ├── test_tasks.py         ✅ Tests Tareas
│       └── test_tags.py          ✅ Tests Etiquetas
```

## Próximos Pasos

1. ✅ Levantar el proyecto con Docker o localmente
2. ✅ Probar los endpoints en Swagger UI
3. ✅ Crear usuarios, tareas y etiquetas
4. 📝 Personalizar el código según tus necesidades
5. 🚀 Desplegar en producción (Railway, Render, AWS, etc.)

## Notas Importantes

- **SECRET_KEY**: Cambiar en producción a un valor seguro
- **CORS**: En producción, especificar los dominios permitidos en `app/main.py`
- **Base de datos**: Usar variables de entorno para las credenciales
- **Tests**: Crear una base de datos separada para testing (`taskflow_test_db`)

---

**¡Todo listo para empezar a desarrollar! 🎉**
