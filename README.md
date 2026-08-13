# Python Gym 🐍🏋️‍♂️

Welcome to **Python Gym**, a comprehensive repository of interactive Jupyter notebooks designed for hands-on learning, mastering Python fundamentals, data structures, algorithms, concurrency, and modern Python application development.

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
| [arrays.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/arrays.ipynb) | Arrays & Dynamic Arrays | Static vs dynamic array memory layout, typed `array` module, `sys.getsizeof()` over-allocation, 2D matrix shallow copy trap, Two Pointers, Sliding Window, Prefix Sum, Kadane's Algorithm |
| [linked_lists.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/linked_lists.ipynb) | Linked Lists | Singly, Doubly, and Circular Linked Lists, pointer mechanics, iterative & recursive reversal, Floyd's Cycle Finding (fast/slow pointers), middle node, merging sorted lists, intersection |
| [hash_maps.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/hash_maps.ipynb) | Hash Maps & Hash Tables | Hash functions, collision resolution (Separate Chaining vs Open Addressing), custom HashMap with auto-resizing, CPython `dict` compact layout, frequency counter, Two Sum, Group Anagrams, Subarray Sum Equals K, LRU Cache ($O(1)$ Hash Map + Doubly Linked List) |
| [stacks.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/stacks.ipynb) | Stacks | LIFO principle, `collections.deque` vs `list` performance, custom Stack class, call stack overhead, Balanced Parentheses, Monotonic Stack (Next Greater Element), RPN Evaluator, Min Stack ($O(1)$ Min) |
| [queues.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/queues.ipynb) | Queues & Deques | FIFO principle, `list.pop(0)` $O(n)$ anti-pattern, `collections.deque` $O(1)$ mechanics, thread-safe `queue.Queue`, BFS level-order traversal, Sliding Window Max (Monotonic Deque), Circular Queue |
| [heaps.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/heaps.ipynb) | Heaps & Priority Queues | Min-Heap vs Max-Heap binary tree array indexing, built-in `heapq` module ($O(n)$ `heapify`), custom MinHeap implementation (`sift_up`/`sift_down`), Top-K elements, Merge K Sorted Lists, Dual Heap Stream Median |
| [binary_search_trees.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/binary_search_trees.ipynb) | Binary Search Trees | BST Invariant ($Left < Root < Right$), custom BST class (`insert`, `search`, 3-case `delete`), DFS (In-Order, Pre-Order, Post-Order) & BFS Level-Order, Validate BST, Lowest Common Ancestor (LCA), Sorted Array to Balanced BST, Kth Smallest Element, Serialization |
| [recursion.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/recursion.ipynb) | Recursion & Backtracking | Base case & recursive step, call stack frames, Tail Call Optimization (TCO), converting recursion to iterative stack, `@lru_cache` memoization, Divide & Conquer (Merge Sort), Backtracking (Subsets $O(2^n)$, Permutations $O(n!)$, N-Queens), Tree flattening |
| [sorting_algorithms.ipynb](file:///e:/repositories/python_gym/data_structures_and_algorithms/sorting_algorithms.ipynb) | Sorting Algorithms | Stability, in-place vs out-of-place, Bubble Sort, Selection Sort, Insertion Sort, Merge Sort ($O(n \log n)$), Quick Sort (partitioning), Heap Sort, Counting Sort ($O(n+k)$), CPython Timsort internals, empirical benchmarks |

---

### 🚀 3. Concurrency (`concurrency/`)

| Notebook | Topics Covered | Key Concepts |
|----------|----------------|--------------|
| [multiprocessing.ipynb](file:///e:/repositories/python_gym/concurrency/multiprocessing.ipynb) | Multiprocessing | GIL bypass, CPU-bound parallel execution, `Process` API, `ProcessPoolExecutor`, `Pool.map()`, IPC (`Queue`, `Pipe`), Shared Memory (`Value`, `Array`, `Manager`), Locks, start methods (`spawn`, `fork`), CPU benchmark |
| [asynchrony.ipynb](file:///e:/repositories/python_gym/concurrency/asynchrony.ipynb) | Asynchronous Programming | Non-blocking I/O with `asyncio`, `async`/`await` syntax, Event Loop mechanics, task scheduling (`create_task`), `gather()`, `as_completed()`, `wait_for()` timeouts, `async with`, `Semaphore`, `to_thread()` |
| [gil.ipynb](file:///e:/repositories/python_gym/concurrency/gil.ipynb) | Global Interpreter Lock (GIL) | What is the GIL, CPython reference counting (`sys.getrefcount`), `sys.getswitchinterval()`, CPU-bound vs I/O-bound multithreading impact, bypassing GIL via `multiprocessing` / NumPy, free-threaded Python 3.13+ (PEP 703) |

---

### 🏗️ 4. Upcoming Modules (In Progress)

- **`object_oriented_programming/`**: Classes, objects, inheritance, polymorphism, encapsulation, dunder/magic methods (`__str__`, `__repr__`, `__len__`, `__getitem__`).
- **`concurrency/`**: Multithreading (`threading`), async I/O (`asyncio`).
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