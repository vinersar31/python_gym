"""
# Design Pattern: Command (Behavioral)

## Intent
Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Use Cases
- Text editor Undo / Redo stacks.
- Job queues / Task schedulers.
- Transactional database operations with rollback.
"""

from abc import ABC, abstractmethod
from typing import List


# 1. Receiver (Holds the actual business state)
class TextDocument:
    def __init__(self):
        self.text: str = ""

    def insert(self, position: int, text: str):
        self.text = self.text[:position] + text + self.text[position:]

    def delete(self, position: int, length: int) -> str:
        deleted = self.text[position : position + length]
        self.text = self.text[:position] + self.text[position + length :]
        return deleted


# 2. Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# 3. Concrete Commands
class InsertTextCommand(Command):
    def __init__(self, doc: TextDocument, position: int, text: str):
        self._doc = doc
        self._position = position
        self._text = text

    def execute(self):
        self._doc.insert(self._position, self._text)

    def undo(self):
        self._doc.delete(self._position, len(self._text))


# 4. Invoker (Manages history and executes commands)
class EditorInvoker:
    def __init__(self):
        self._history: List[Command] = []
        self._undone: List[Command] = []

    def execute_command(self, cmd: Command):
        cmd.execute()
        self._history.append(cmd)
        self._undone.clear()  # Clear redo history on new action

    def undo(self) -> bool:
        if not self._history:
            return False
        cmd = self._history.pop()
        cmd.undo()
        self._undone.append(cmd)
        return True

    def redo(self) -> bool:
        if not self._undone:
            return False
        cmd = self._undone.pop()
        cmd.execute()
        self._history.append(cmd)
        return True


# =====================================================================
# Tests
# =====================================================================
def test_command_pattern():
    doc = TextDocument()
    editor = EditorInvoker()

    # Step 1: Type "Hello"
    editor.execute_command(InsertTextCommand(doc, 0, "Hello"))
    assert doc.text == "Hello"

    # Step 2: Append " World"
    editor.execute_command(InsertTextCommand(doc, 5, " World"))
    assert doc.text == "Hello World"

    # Step 3: Undo -> "Hello"
    assert editor.undo() is True
    assert doc.text == "Hello"

    # Step 4: Undo -> ""
    assert editor.undo() is True
    assert doc.text == ""

    # Step 5: Redo -> "Hello"
    assert editor.redo() is True
    assert doc.text == "Hello"


if __name__ == "__main__":
    test_command_pattern()
    print("Command pattern tests passed successfully! [OK]")
