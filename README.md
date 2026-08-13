# Python Gym 🐍🏋️‍♂️

Welcome to **Python Gym**, a comprehensive repository of interactive Jupyter notebooks designed for hands-on learning, mastering Python fundamentals, data structures, algorithms, advanced design patterns, and modern Python application development.

---

## 📚 Curriculum & Notebook Map

### 📖 1. Learn the Basics (`learn_the_basics/`)

| Notebook | Topics Covered | Key Concepts |
|----------|----------------|--------------|
| [basic_syntax.ipynb](file:///e:/repositories/python_gym/learn_the_basics/basic_syntax.ipynb) | Basic Syntax & Structure | Statements, line continuation, indentation rules, comments, `print()`, `input()`, built-in keywords |
| [variables_and_data_types.ipynb](file:///e:/repositories/python_gym/learn_the_basics/variables_and_data_types.ipynb) | Variables & Data Types | Dynamic typing, object references, `int`, `float`, `complex`, `bool`, `str`, `list`, `tuple`, `dict`, `set`, `type()`, `isinstance()`, type casting |
| [operators.ipynb](file:///e:/repositories/python_gym/learn_the_basics/operators.ipynb) | Operators | Arithmetic, comparison, assignment, logical, bitwise, membership (`in`), identity (`is`), operator precedence, walrus operator `:=` |
| [control_flow.ipynb](file:///e:/repositories/python_gym/learn_the_basics/control_flow.ipynb) | Control Flow | `if / elif / else`, ternary expressions, `match / case` (Python 3.10+), `for` loops, `while` loops, `break`, `continue`, `pass`, loop `else` clause |
| [working_with_strings.ipynb](file:///e:/repositories/python_gym/learn_the_basics/working_with_strings.ipynb) | Working with Strings | String indexing & slicing, string operators, escape sequences, raw strings, f-string formatting, case methods, string search/trim/split/join, UTF-8 bytes |
| [loops.ipynb](file:///e:/repositories/python_gym/learn_the_basics/loops.ipynb) | Loops — Deep Dive | Iterating over iterables, `range()` internals, `enumerate()`, `zip()`, nested loops, matrix flattening, `itertools` basics, generator performance |
| [functions.ipynb](file:///e:/repositories/python_gym/learn_the_basics/functions.ipynb) | Functions — Complete Guide | Function definition, default parameters, mutable default trap, `*args`, `**kwargs`, positional/keyword-only markers (`/`, `*`), return tuples, LEGB scope, docstrings, typing hints, lambda, closures, decorators intro, recursion |

---

### ⚡ 2. Data Structures & Algorithms (`data_structures_and_algorithms/`)

| Notebook | Topics Covered | Key Concepts |
|----------|----------------|--------------|
| [modules.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/modules.ipynb) | Modules & Packages | Creating `.py` modules, import variants, `sys.path`, executable scripts (`if __name__ == '__main__'`), `importlib.reload()`, standard library overview, package creation with `__init__.py`, `__all__` export control |
| [lambdas.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/lambdas.ipynb) | Lambda Functions | Anonymous functions, syntax, key functions in sorting/searching (`sorted()`, `min()`, `max()`), `map()`, `filter()`, `reduce()`, ternary logic, closure binding trap, bytecode analysis |
| [decorators.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/decorators.ipynb) | Decorators & Profiling | First-class functions, wrapper functions, preserving metadata with `@functools.wraps`, `@timeit` benchmark, `@count_calls`, `@memoize` for Dynamic Programming, decorator factories, stacked decorators, class-based decorators |
| [iterators.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/iterators.ipynb) | Iterators & Generators | Iterator Protocol (`__iter__`, `__next__`), manual `for` loop simulation, custom iterator classes, Linked List iteration, `yield` generator functions, coroutine `.send()`, `itertools` module, $O(1)$ memory benchmarking |
| [regular_expressions.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/regular_expressions.ipynb) | Regular Expressions (Regex) | `re` module, search functions (`search`, `match`, `findall`, `finditer`), metacharacters, quantifiers (greedy vs lazy), named capture groups, zero-width lookaround assertions, PII masking, lexical analyzer tokenizer |
| [variable_scope.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/variable_scope.ipynb) | Variable Scope & Namespaces | Namespace inspection (`locals()`, `globals()`), LEGB resolution rule, `global` keyword, `nonlocal` keyword for tree/graph DFS helpers, shadowing built-in names, loop vs comprehension scope isolation |

---

### 🏗️ 3. Upcoming Modules (In Progress)

- **`object_oriented_programming/`**: Classes, objects, inheritance, polymorphism, encapsulation, dunder/magic methods (`__str__`, `__repr__`, `__len__`, `__getitem__`).
- **`concurrency/`**: Multithreading (`threading`), multiprocessing (`multiprocessing`), async I/O (`asyncio`).
- **`fast_api/`**: Asynchronous web APIs, Pydantic data schemas, Uvicorn server integration, OpenAPI documentation.
- **`package_manager/`**: Virtual environments (`venv`, `conda`), dependency management (`pip`, `poetry`, `uv`).

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **Jupyter Notebook** / **JupyterLab** or **VS Code** with Python & Jupyter extensions.

### Installation & Launch

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vinersar31/python_gym.git
   cd python_gym
   ```

2. **Launch Jupyter Lab**:
   ```bash
   jupyter lab
   ```
   Or open any `.ipynb` file directly in VS Code / PyCharm / Antigravity IDE.

---

## 🛠️ Best Practices Followed in Notebooks

- **Runnable & Verified**: Every code cell is fully valid and runnable in Python 3.10+.
- **Clean Output**: Uses clean, explicit print formatting without console encoding issues.
- **Self-Contained**: Each notebook includes an intro, index, detailed explanations, executable code cells, quick reference cheat sheet, and summary table.
- **Standard UTF-8**: All notebooks are saved in standard UTF-8 format.

---

## 📄 License
This repository is open-source and available under the [MIT License](LICENSE).