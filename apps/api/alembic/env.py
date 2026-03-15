from __future__ import annotations

import os
from logging.config import fileConfig
from pathlib import Path

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from sqlalchemy.exc import OperationalError
from sqlmodel import SQLModel

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

# Import models so SQLModel metadata is populated for autogenerate.
from calcms_api.models.content import ContentItem  # noqa: F401, E402

config = context.config

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is not set. Define it in .env or environment.")

config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    try:
        with connectable.connect() as connection:
            context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)

            with context.begin_transaction():
                context.run_migrations()
    except OperationalError as exc:
        raise SystemExit(
            "Could not connect to PostgreSQL for migrations. "
            "Check DATABASE_URL and ensure Postgres is running (for Docker: `docker compose up -d postgres`)."
        ) from exc


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()