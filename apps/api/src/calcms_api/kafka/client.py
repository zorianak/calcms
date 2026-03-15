"""
Kafka producer and consumer stubs using kafka-python-ng.

Quick start:
    producer = KafkaProducerClient(bootstrap_servers=["localhost:9092"])
    producer.send("my-topic", {"key": "value"})
    producer.close()

    consumer = KafkaConsumerClient(topics=["my-topic"], bootstrap_servers=["localhost:9092"])
    for message in consumer.messages():
        print(message)
    consumer.close()
"""

import json
import logging
from collections.abc import Iterator
from typing import Any

from kafka import KafkaConsumer, KafkaProducer  # type: ignore[import-untyped]

logger = logging.getLogger(__name__)


class KafkaProducerClient:
    """Thin wrapper around KafkaProducer for JSON messages."""

    def __init__(self, bootstrap_servers: list[str] | None = None) -> None:
        self._servers = bootstrap_servers or ["localhost:9092"]
        self._producer = KafkaProducer(
            bootstrap_servers=self._servers,
            value_serializer=lambda v: json.dumps(v).encode(),
        )

    def send(self, topic: str, payload: Any) -> None:
        """Send a JSON-serialisable payload to a Kafka topic."""
        future = self._producer.send(topic, payload)
        try:
            future.get(timeout=10)
        except Exception:
            logger.exception("Failed to send message to topic '%s'", topic)
            raise

    def close(self) -> None:
        self._producer.flush()
        self._producer.close()


class KafkaConsumerClient:
    """Thin wrapper around KafkaConsumer for JSON messages."""

    def __init__(
        self,
        topics: list[str],
        bootstrap_servers: list[str] | None = None,
        group_id: str = "calcms-consumer",
    ) -> None:
        self._consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers or ["localhost:9092"],
            group_id=group_id,
            auto_offset_reset="earliest",
            value_deserializer=lambda v: json.loads(v.decode()),
        )

    def messages(self) -> Iterator[Any]:
        """Yield decoded messages from subscribed topics."""
        for msg in self._consumer:
            yield msg.value

    def close(self) -> None:
        self._consumer.close()
