"""Database setup for CalCMS.

Defaults to PostgreSQL while keeping a single module boundary for swapping
providers later.
"""

import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import text
from sqlmodel import Session, create_engine

load_dotenv()

DATABASE_PROVIDER = os.getenv("DB_PROVIDER", "postgres").lower()
DATABASE_URL = os.getenv("DATABASE_URL")


if DATABASE_PROVIDER != "postgres":
    raise ValueError(
        f"Unsupported DB_PROVIDER '{DATABASE_PROVIDER}'. "
        "Only 'postgres' is supported right now."
    )


if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not set. Define it in your environment or .env file."
    )


engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency for a DB session."""
    with Session(engine) as session:
        yield session


def ping_database() -> bool:
    """Return True when the database connection is healthy."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        return False
