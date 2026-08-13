# 📦 Package Management & Environment Isolation

Welcome to the **Package Manager** module of Python Gym! This section covers virtual environment isolation, dependency resolution, project packaging, and modern Python package managers.

---

## 📌 Module Overview

Managing Python environments and dependencies cleanly prevents conflicting package versions across projects and ensures reproducible deployments.

### Key Tools & Topics Covered:
- **Environment Isolation**: Isolating Python interpreters and libraries (`venv`, `virtualenv`, `conda`).
- **Standard Dependency Management**: Managing requirements via `pip` and `requirements.txt`.
- **Modern Packaging Tools**: Next-generation dependency resolvers (`Poetry`, `Pipenv`, `flit`).
- **High-Performance Tooling**: Ultra-fast Rust-based package management using `uv`.

---

## 📚 Curriculum & Planned Notebook Roadmap

| # | Planned Notebook | Topic | Key Concepts to be Covered |
|---|------------------|-------|----------------------------|
| 1 | `virtual_environments.ipynb` | Virtual Environment Isolation | Creating and activating `venv`, system vs environment site-packages, environment activation scripts, `conda` environment management |
| 2 | `pip_and_requirements.ipynb` | Dependency Management with Pip | `pip install`, `pip freeze`, pinned dependencies, Semantic Versioning (`==`, `>=`, `~=`), wheels (`.whl`) vs source distributions (`sdist`) |
| 3 | `poetry_management.ipynb` | Modern Packaging with Poetry | `pyproject.toml` configuration, dependency resolution locking (`poetry.lock`), managing dev dependencies, building and publishing packages |
| 4 | `uv_fast_packaging.ipynb` | Next-Gen Ultra-Fast Tooling (`uv`) | `uv pip`, `uv venv`, high-speed Rust dependency resolution, workspace management, replacing legacy `pip-tools` |

---

## 🛠️ Recommended Setup

To explore these packaging tools:
```bash
pip install poetry uv
```
