# 🧱 Object-Oriented Programming (OOP) in Python

Welcome to the **Object-Oriented Programming (OOP)** module of Python Gym! This section explores class design, object lifecycle management, data encapsulation, inheritance hierarchies, and magic (dunder) methods.

---

## 📌 Module Overview

In Python, **everything is an object** — from primitive integers and strings to functions and modules. Mastering OOP principles allows developers to build modular, maintainable, and scalable software architectures.

### The Four Pillars of OOP in Python:
1. **Encapsulation**: Bundling data and operating methods inside classes, enforcing public/private boundaries.
2. **Abstraction**: Hiding internal implementation details using Abstract Base Classes (`abc.ABC`).
3. **Inheritance**: Reusing code across class hierarchies using single, multiple, and multilevel inheritance.
4. **Polymorphism**: Allowing uniform interface interaction across different object types (Duck Typing).

---

## 📚 Curriculum & Planned Notebook Roadmap

| # | Notebook | Status | Key Concepts Covered |
|---|----------|--------|----------------------|
| 1 | [classes_and_objects.ipynb](classes_and_objects.ipynb) | ✅ Complete | `class` definition, `self` reference, `__init__` constructor, instance vs class attributes, `@classmethod`, `@staticmethod`, `__slots__` memory optimization, introspection |
| 2 | [methods.ipynb](methods.ipynb) | ✅ Complete | Descriptor method binding, fluent method chaining, `@classmethod` polymorphic factory constructors, `@staticmethod`, `@singledispatchmethod` polymorphic dispatch, abstract contracts (`abc.ABC`), method decorators, core dunder methods |
| 3 | [inheritance_and_polymorphism.ipynb](inheritance_and_polymorphism.ipynb) | ✅ Complete | Single/Multiple inheritance, `super()` proxy mechanics, MRO (C3 Linearization), Cooperative multiple inheritance, Mixin pattern, Duck Typing & `typing.Protocol`, Composition vs. Inheritance |
| 4 | [encapsulation_and_properties.ipynb](encapsulation_and_properties.ipynb) | ✅ Complete | Access modifiers & name mangling (`__private`), `@property` getters/setters/deleters, custom descriptor protocol (`__get__`, `__set__`, `__set_name__`), `@cached_property`, immutable `@dataclass(frozen=True)` |
| 5 | `dunder_methods.ipynb` | 📝 Planned | Object representation (`__str__`, `__repr__`), operator overloading (`__add__`, `__eq__`), container emulation (`__len__`, `__getitem__`), callable objects (`__call__`) |

---

## 🛠️ Getting Started

All notebooks in this section require standard Python 3.10+ and execute directly in Jupyter Lab / VS Code without external dependencies.
