"""
# Design Pattern: Adapter (Structural)

## Intent
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

## Use Cases
- Integrating third-party payment gateways (e.g. PayPal vs Stripe vs Legacy XML).
- Wrapping legacy APIs with modern JSON interfaces.
- Standardizing logging or metric reporters.
"""

from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET


# 1. Target Interface expected by Modern Client
class ModernDataProcessor(ABC):
    @abstractmethod
    def process_json_data(self, json_str: str) -> dict:
        """Process modern JSON string and return parsed dictionary."""
        pass


# 2. Adaptee (Legacy Service with Incompatible XML Interface)
class LegacyXMLService:
    def process_xml_feed(self, xml_str: str) -> str:
        """Legacy method that only accepts XML and returns XML summary."""
        root = ET.fromstring(xml_str)
        user_id = root.find("user_id").text
        amount = root.find("amount").text
        return f"<result status='SUCCESS' user_id='{user_id}' amount='{amount}'/>"


# 3. Adapter Class
class XMLToJSONAdapter(ModernDataProcessor):
    def __init__(self, legacy_service: LegacyXMLService):
        self._legacy_service = legacy_service

    def process_json_data(self, json_str: str) -> dict:
        # Convert incoming JSON into XML payload for legacy service
        data = json.loads(json_str)
        xml_payload = f"<transaction><user_id>{data['user_id']}</user_id><amount>{data['amount']}</amount></transaction>"

        # Call legacy service
        xml_response = self._legacy_service.process_xml_feed(xml_payload)

        # Parse XML response back into client-friendly dictionary
        root = ET.fromstring(xml_response)
        return {
            "status": root.attrib.get("status"),
            "user_id": root.attrib.get("user_id"),
            "amount": float(root.attrib.get("amount")),
        }


# =====================================================================
# Tests
# =====================================================================
def test_adapter():
    legacy_service = LegacyXMLService()
    adapter = XMLToJSONAdapter(legacy_service)

    json_payload = '{"user_id": "usr_99", "amount": 149.99}'
    result = adapter.process_json_data(json_payload)

    assert result["status"] == "SUCCESS"
    assert result["user_id"] == "usr_99"
    assert result["amount"] == 149.99


if __name__ == "__main__":
    test_adapter()
    print("Adapter tests passed successfully! [OK]")
