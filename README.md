# Task Management API

API RESTful construida con **FastAPI** para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una colección de "tareas". Incluye validaciones robustas, documentación automática y una estructura modular escalable.

## Características
- CRUD completo para `tasks`:
  - **Crear un tarea*: `POST /tasks/`
  - **Leer todos los items**: `GET /tasks/`
  - **Leer un item específico**: `GET /tasks/{item_id}`
  - **Actualizar un tarea*: `PUT /tasks/{item_id}`
  - **Eliminar un tarea*: `DELETE /tasks/{item_id}`
- Validación de datos con **Pydantic**.
- Documentación interactiva generada automáticamente con:
  - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Estructura modular para un desarrollo limpio y escalable.

---

## Requisitos

- **Python** 3.9 o superior
- **FastAPI** 0.85.0 o superior
- **Uvicorn** 0.18.0 o superior
- **SQLAlchemy** 1.4 o superior

---

## Instalación y Ejecución

Sigue estos pasos para instalar y ejecutar la API en tu entorno local:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload