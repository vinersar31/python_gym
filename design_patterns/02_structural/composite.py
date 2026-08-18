"""
# Design Pattern: Composite (Structural)

## Intent
Composes objects into tree structures to represent part-whole hierarchies.
Composite lets clients treat individual objects and compositions of objects uniformly.

## Use Cases
- File System hierarchies (Files and Folders with recursive size calculations).
- UI component trees (Containers, Panels, Buttons, Inputs).
- Organization Charts (Employees and Managers).
"""

from abc import ABC, abstractmethod
from typing import List


# 1. Component Base Interface
class FileSystemComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        """Return total size in bytes."""
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        """Display ASCII tree representation."""
        pass


# 2. Leaf (Individual item)
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        return self._size

    def display(self, indent: int = 0) -> str:
        return "  " * indent + f"- File: {self._name} ({self._size} KB)"


# 3. Composite (Contains child leaves and composites)
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> "Directory":
        self._children.append(component)
        return self

    def remove(self, component: FileSystemComponent) -> "Directory":
        self._children.remove(component)
        return self

    def get_name(self) -> str:
        return self._name

    def get_size(self) -> int:
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0) -> str:
        lines = ["  " * indent + f"+ Directory: {self._name} (Total: {self.get_size()} KB)"]
        for child in self._children:
            lines.append(child.display(indent + 1))
        return "\n".join(lines)


# =====================================================================
# Tests
# =====================================================================
def test_composite():
    root = Directory("root")
    src = Directory("src")
    docs = Directory("docs")

    f1 = File("main.py", 12)
    f2 = File("utils.py", 8)
    f3 = File("README.md", 4)

    src.add(f1).add(f2)
    docs.add(f3)
    root.add(src).add(docs)

    assert root.get_size() == 24
    assert src.get_size() == 20
    assert docs.get_size() == 4

    tree_str = root.display()
    assert "+ Directory: root (Total: 24 KB)" in tree_str
    assert "- File: main.py" in tree_str


if __name__ == "__main__":
    test_composite()
    print("Composite tests passed successfully! [OK]")
