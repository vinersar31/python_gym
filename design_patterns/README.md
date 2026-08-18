# 🧩 Python Design Patterns Catalog

A comprehensive collection of classic **Gang of Four (GoF)** and modern Pythonic design patterns, implemented with production-grade type annotations, docstrings, and automated unit test suites.

---

## 🗺️ Patterns Directory

### 🏗️ 1. Creational Patterns (`design_patterns/01_creational/`)
*Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.*

| Pattern | File | Summary & Use Case |
|---|---|---|
| **Factory Method** | [factory_method.py](file:///e:/repositories/python_gym/design_patterns/01_creational/factory_method.py) | Defer instantiation to subclasses (e.g. Email/SMS/Push notifications). |
| **Abstract Factory** | [abstract_factory.py](file:///e:/repositories/python_gym/design_patterns/01_creational/abstract_factory.py) | Create families of related products without concrete coupling (e.g. UI theme suites). |
| **Builder** | [builder.py](file:///e:/repositories/python_gym/design_patterns/01_creational/builder.py) | Step-by-step construction of complex objects with method chaining (e.g. HTTP requests). |
| **Prototype** | [prototype.py](file:///e:/repositories/python_gym/design_patterns/01_creational/prototype.py) | Clone existing objects with deep copying via registry (e.g. template documents). |
| **Singleton** | [singleton.py](file:///e:/repositories/python_gym/design_patterns/01_creational/singleton.py) | Ensure only a single global instance exists (Thread-safe Metaclass & `__new__`). |

---

### 🏛️ 2. Structural Patterns (`design_patterns/02_structural/`)
*Deal with object composition and simplifying the structure by identifying relationships.*

| Pattern | File | Summary & Use Case |
|---|---|---|
| **Adapter** | [adapter.py](file:///e:/repositories/python_gym/design_patterns/02_structural/adapter.py) | Convert one interface into another (e.g. Legacy XML to modern JSON). |
| **Composite** | [composite.py](file:///e:/repositories/python_gym/design_patterns/02_structural/composite.py) | Represent part-whole tree hierarchies uniformly (e.g. File & Directory systems). |
| **Decorator** | [decorator_pattern.py](file:///e:/repositories/python_gym/design_patterns/02_structural/decorator_pattern.py) | Dynamically wrap objects to attach behaviors (e.g. Coffee beverage additions). |
| **Facade** | [facade.py](file:///e:/repositories/python_gym/design_patterns/02_structural/facade.py) | Provide a simplified high-level interface to complex subsystems (e.g. E-commerce checkout). |
| **Proxy** | [proxy.py](file:///e:/repositories/python_gym/design_patterns/02_structural/proxy.py) | Placeholder to control access, cache results, or lazy-load expensive subjects. |

---

### 🚦 3. Behavioral Patterns (`design_patterns/03_behavioral/`)
*Deal with communication and assignment of responsibilities between objects.*

| Pattern | File | Summary & Use Case |
|---|---|---|
| **Chain of Responsibility** | [chain_of_responsibility.py](file:///e:/repositories/python_gym/design_patterns/03_behavioral/chain_of_responsibility.py) | Pass request along a chain of potential handlers (e.g. Middleware auth pipeline). |
| **Command** | [command.py](file:///e:/repositories/python_gym/design_patterns/03_behavioral/command.py) | Encapsulate request as object supporting Undo/Redo (e.g. Text editor history). |
| **Observer** | [observer.py](file:///e:/repositories/python_gym/design_patterns/03_behavioral/observer.py) | One-to-many publish-subscribe event mechanism (e.g. Stock ticker alert bots). |
| **State** | [state.py](file:///e:/repositories/python_gym/design_patterns/03_behavioral/state.py) | Alter behavior when internal state changes (e.g. E-commerce order lifecycle). |
| **Strategy** | [strategy.py](file:///e:/repositories/python_gym/design_patterns/03_behavioral/strategy.py) | Encapsulate interchangeable algorithms (e.g. Dynamic discount calculations). |

---

## 🏃 Running Tests

Run any individual pattern file:
```bash
python design_patterns/01_creational/factory_method.py
```

Or test all design patterns with the `gym.py` CLI:
```bash
python gym.py test design_patterns
```
