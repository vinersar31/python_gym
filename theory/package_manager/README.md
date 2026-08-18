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

| # | Notebook | Topic | Key Concepts Covered | Status |
|---|----------|-------|----------------------|--------|
| 1 | [common_packages_and_modules.ipynb](common_packages_and_modules.ipynb) | Packages & Modules Foundations | Module vs package structure, `sys.path`, `importlib`, standard library ("Batteries Included"), PyPI ecosystem, `__all__` |  Completed |
| 2 | `virtual_environments.ipynb` | Virtual Environment Isolation | Creating and activating `venv`, system vs environment site-packages, activation scripts, `conda` | 📝 Planned |
| 3 | [pip_and_requirements.ipynb](pip_and_requirements.ipynb) | Dependency Management with Pip | `pip install`, `pip freeze`, pinned requirements, SemVer (`==`, `>=`, `~=`), wheels vs sdist, hash security |  Completed |
| 4 | `poetry_management.ipynb` | Modern Packaging with Poetry | `pyproject.toml` configuration, `poetry.lock`, managing dev dependencies, publishing | 📝 Planned |
| 5 | [uv_fast_packaging.ipynb](uv_fast_packaging.ipynb) | Next-Gen Ultra-Fast Tooling (`uv`) | Rust PubGrub resolver, `uv pip`, `uv venv`, `uv python`, `uv init`/`add`/`run`, PEP 723 single-file scripts, `uvx` |  Completed |

---

## 🛠️ Recommended Setup

To explore these packaging tools:
```bash
pip install poetry uv
```
