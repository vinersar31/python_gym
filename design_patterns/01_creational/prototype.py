"""
# Design Pattern: Prototype (Creational)

## Intent
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Use Cases
- When creating an object is expensive (e.g. requires network/DB call or complex computation).
- Cloneable documents, game entities (NPCs, bullets), configuration profiles.
"""

import copy
from typing import Dict, Any, List


class DocumentPrototype:
    """A prototype class supporting deep cloning."""

    def __init__(self, title: str, content: str, tags: List[str], metadata: Dict[str, Any]):
        self.title = title
        self.content = content
        self.tags = tags
        self.metadata = metadata

    def clone(self) -> "DocumentPrototype":
        """Perform a deep copy of self."""
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        return f"Document(title='{self.title}', tags={self.tags}, metadata={self.metadata})"


class PrototypeRegistry:
    """Registry to store and retrieve predefined prototype templates."""

    def __init__(self):
        self._prototypes: Dict[str, DocumentPrototype] = {}

    def register_prototype(self, name: str, prototype: DocumentPrototype):
        self._prototypes[name] = prototype

    def unregister_prototype(self, name: str):
        if name in self._prototypes:
            del self._prototypes[name]

    def create(self, name: str) -> DocumentPrototype:
        if name not in self._prototypes:
            raise KeyError(f"Prototype '{name}' not found in registry")
        return self._prototypes[name].clone()


# =====================================================================
# Tests
# =====================================================================
def test_prototype():
    # Base invoice template
    invoice_template = DocumentPrototype(
        title="Standard Invoice",
        content="Items: ...\nTotal: ...",
        tags=["finance", "invoice"],
        metadata={"currency": "USD", "vat_rate": 0.20},
    )

    registry = PrototypeRegistry()
    registry.register_prototype("invoice", invoice_template)

    # Clone and modify instance 1
    client1_invoice = registry.create("invoice")
    client1_invoice.title = "Invoice #1001 for Acme Corp"
    client1_invoice.tags.append("acme")
    client1_invoice.metadata["client_id"] = "C1001"

    # Clone instance 2
    client2_invoice = registry.create("invoice")

    assert client1_invoice.title == "Invoice #1001 for Acme Corp"
    assert "acme" in client1_invoice.tags
    assert "acme" not in client2_invoice.tags  # Independent deep copy
    assert "client_id" not in client2_invoice.metadata


if __name__ == "__main__":
    test_prototype()
    print("Prototype tests passed successfully! [OK]")
