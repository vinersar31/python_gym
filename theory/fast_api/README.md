# 🚀 FastAPI — Asynchronous Web APIs & Microservices

Welcome to the **FastAPI** module of Python Gym! This section covers building high-performance, asynchronous RESTful APIs using the **FastAPI** framework, **Pydantic** data validation schemas, and **Uvicorn** ASGI server integration.

---

## 📌 Module Overview

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.10+ based on standard Python type hints.

### Key Features Covered:
- **Asynchronous Architecture**: Built on Starlette and ASGI for native `async`/`await` non-blocking request handling.
- **Data Validation & Serialization**: Powered by Pydantic models for strict type checking and automatic JSON parsing.
- **Automatic Interactive Documentation**: Auto-generated **Swagger UI** (`/docs`) and **ReDoc** (`/redoc`) powered by OpenAPI standard.
- **Dependency Injection**: Powerful `Depends()` system for authentication, security, database sessions, and configuration management.

---

## 📚 Curriculum & Planned Notebook Roadmap

| # | Planned Notebook | Topic | Key Concepts to be Covered |
|---|------------------|-------|----------------------------|
| 1 | `basic_api.ipynb` | First Steps with FastAPI | App initialization, GET/POST endpoints, Path vs Query parameters, status codes, running Uvicorn server |
| 2 | `pydantic_schemas.ipynb` | Data Validation with Pydantic | `BaseModel`, field validation, nested schemas, custom validators, ORM mode, serialization |
| 3 | `dependency_injection.ipynb` | Dependency Injection | `Depends()`, request context, database session management, authentication & bearer token verification |
| 4 | `async_fastapi.ipynb` | Async Routes & Database ORM | Non-blocking async endpoints, Async SQLAlchemy / Tortoise ORM, BackgroundTasks, WebSocket connections |

---

## 🛠️ Prerequisites & Installation

To run the upcoming FastAPI interactive notebooks:
```bash
pip install fastapi "uvicorn[standard]" pydantic
```
