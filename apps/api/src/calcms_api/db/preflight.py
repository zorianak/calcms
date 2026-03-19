"""Preflight checks for database connectivity and configuration."""

from __future__ import annotations

import os
import sys

from dotenv import load_dotenv


def main() -> int:
    load_dotenv()

    db_provider = os.getenv("DB_PROVIDER", "postgres").lower()
    database_url = os.getenv("DATABASE_URL")

    if db_provider != "postgres":
        print(
            "[preflight] ERROR: Unsupported DB_PROVIDER. "
            "Only 'postgres' is currently supported.",
            file=sys.stderr,
        )
        return 1

    if not database_url:
        print(
            "[preflight] ERROR: DATABASE_URL is not set. "
            "Set it in your environment or .env file.",
            file=sys.stderr,
        )
        return 1

    try:
        from calcms_api.db.connection import ping_database
    except Exception as exc:  # pragma: no cover
        print(f"[preflight] ERROR: Failed to initialize DB connection settings: {exc}", file=sys.stderr)
        return 1

    if not ping_database():
        print(
            "[preflight] ERROR: Could not connect to PostgreSQL. "
            "Check DATABASE_URL and ensure Postgres is running.",
            file=sys.stderr,
        )
        return 1

    print("[preflight] OK: PostgreSQL configuration and connectivity look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())