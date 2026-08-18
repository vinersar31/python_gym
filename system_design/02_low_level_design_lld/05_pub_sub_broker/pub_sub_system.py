"""
# Low-Level Design: In-Memory Pub-Sub Topic Broker

## Requirements
- Support multiple Topics.
- Allow Subscribers to subscribe / unsubscribe to specific topics.
- Allow Publishers to publish messages to a topic.
- Fan-out messages to all active topic subscribers with filter criteria.
"""

from typing import Dict, List, Callable, Any
from dataclasses import dataclass, field
import uuid
import time


@dataclass
class Message:
    topic: str
    payload: Any
    message_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: float = field(default_factory=time.time)


class Subscriber:
    def __init__(self, name: str, callback: Callable[[Message], None]):
        self.name = name
        self.callback = callback
        self.received_messages: List[Message] = []

    def on_message(self, message: Message):
        self.received_messages.append(message)
        self.callback(message)


class Topic:
    def __init__(self, name: str):
        self.name = name
        self.subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def publish(self, message: Message):
        for sub in self.subscribers:
            sub.on_message(message)


class PubSubBroker:
    def __init__(self):
        self.topics: Dict[str, Topic] = {}

    def get_or_create_topic(self, topic_name: str) -> Topic:
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic(topic_name)
        return self.topics[topic_name]

    def subscribe(self, topic_name: str, subscriber: Subscriber):
        topic = self.get_or_create_topic(topic_name)
        topic.add_subscriber(subscriber)

    def unsubscribe(self, topic_name: str, subscriber: Subscriber):
        if topic_name in self.topics:
            self.topics[topic_name].remove_subscriber(subscriber)

    def publish(self, topic_name: str, payload: Any) -> Message:
        topic = self.get_or_create_topic(topic_name)
        msg = Message(topic=topic_name, payload=payload)
        topic.publish(msg)
        return msg


# =====================================================================
# Tests
# =====================================================================
def test_pub_sub_system():
    broker = PubSubBroker()

    events_a = []
    events_b = []

    sub_a = Subscriber("Subscriber A", lambda m: events_a.append(m.payload))
    sub_b = Subscriber("Subscriber B", lambda m: events_b.append(m.payload))

    # Subscribe to "orders"
    broker.subscribe("orders", sub_a)
    broker.subscribe("orders", sub_b)

    # Subscribe sub_a to "payments"
    broker.subscribe("payments", sub_a)

    # Publish to "orders"
    broker.publish("orders", {"order_id": 101, "amount": 50})
    assert len(events_a) == 1
    assert len(events_b) == 1

    # Publish to "payments"
    broker.publish("payments", {"payment_id": "P-99"})
    assert len(events_a) == 2
    assert len(events_b) == 1  # sub_b not subscribed to payments

    # Unsubscribe sub_a from "orders"
    broker.unsubscribe("orders", sub_a)
    broker.publish("orders", {"order_id": 102})
    assert len(events_a) == 2  # did not receive new order
    assert len(events_b) == 2


if __name__ == "__main__":
    test_pub_sub_system()
    print("Pub-Sub Topic Broker LLD tests passed successfully! [OK]")
