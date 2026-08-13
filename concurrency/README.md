# 🚀 Concurrency & Parallel Programming

Welcome to the **Concurrency** module of Python Gym! This module covers multi-core processing, multithreading, and asynchronous programming in Python.

---

## 📚 Notebook Directory

| # | Notebook | Topic | Key Concepts Covered |
|---|----------|-------|----------------------|
| 1 | [multiprocessing.ipynb](file:///e:/repositories/python_gym/concurrency/multiprocessing.ipynb) | Multiprocessing | GIL bypass, CPU-bound parallel execution, `Process` API, `ProcessPoolExecutor`, IPC (`Queue`, `Pipe`), Shared Memory (`Value`, `Array`, `Manager`), Locks, process start methods (`spawn`, `fork`), CPU benchmark |
| 2 | [asynchrony.ipynb](file:///e:/repositories/python_gym/concurrency/asynchrony.ipynb) | Asynchronous Programming | Non-blocking I/O with `asyncio`, `async`/`await` syntax, Event Loop mechanics, task scheduling (`create_task`), `gather()`, `as_completed()`, `wait_for()` timeouts, `async with`, `Semaphore`, `to_thread()` |

---

## 🚀 How to Use

Launch Jupyter Lab in the root directory:
```bash
jupyter lab
```
And navigate into `concurrency/` to run the notebooks.
