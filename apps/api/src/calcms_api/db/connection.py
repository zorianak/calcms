"""
Non-opinionated database connection interface.

Implement this for your chosen database. The example below is designed
for PostgreSQL (psycopg3), but the abstract interface works with any DB.

Quick start with PostgreSQL:
    1. Uncomment `psycopg[binary]` in pyproject.toml.
    2. Subclass `DatabaseConnection` and implement all abstract methods.
    3. Inject your implementation wherever you need DB access.
"""

from abc import ABC, abstractmethod
from typing import Any


class DatabaseConnection(ABC):
    """Abstract interface for a database connection.

    Implement this class for your specific database driver.
    """

    @abstractmethod
    async def connect(self) -> None:
        """Open the connection / connection pool."""

    @abstractmethod
    async def disconnect(self) -> None:
        """Close the connection / connection pool."""

    @abstractmethod
    async def execute(self, query: str, *args: Any) -> None:
        """Execute a query that returns no rows (INSERT / UPDATE / DELETE)."""

    @abstractmethod
    async def fetch_one(self, query: str, *args: Any) -> dict[str, Any] | None:
        """Execute a query and return a single row as a dict, or None."""

    @abstractmethod
    async def fetch_all(self, query: str, *args: Any) -> list[dict[str, Any]]:
        """Execute a query and return all rows as a list of dicts."""


# ── PostgreSQL example stub ────────────────────────────────────────────────────
# Uncomment and fill in once you add `psycopg[binary]` to your dependencies.
#
# import psycopg
# from psycopg.rows import dict_row
#
# class PostgresConnection(DatabaseConnection):
#     def __init__(self, dsn: str) -> None:
#         self._dsn = dsn
#         self._conn: psycopg.AsyncConnection | None = None
#
#     async def connect(self) -> None:
#         self._conn = await psycopg.AsyncConnection.connect(self._dsn, row_factory=dict_row)
#
#     async def disconnect(self) -> None:
#         if self._conn:
#             await self._conn.close()
#
#     async def execute(self, query: str, *args: Any) -> None:
#         assert self._conn, "Not connected"
#         await self._conn.execute(query, args)
#
#     async def fetch_one(self, query: str, *args: Any) -> dict[str, Any] | None:
#         assert self._conn, "Not connected"
#         async with self._conn.cursor() as cur:
#             await cur.execute(query, args)
#             return await cur.fetchone()
#
#     async def fetch_all(self, query: str, *args: Any) -> list[dict[str, Any]]:
#         assert self._conn, "Not connected"
#         async with self._conn.cursor() as cur:
#             await cur.execute(query, args)
#             return await cur.fetchall()
