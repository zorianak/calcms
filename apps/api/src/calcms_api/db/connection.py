"""Database setup for CalCMS.

Defaults to PostgreSQL while keeping a single module boundary for swapping
providers later.
"""

import os
from collections.abc import Generator

from sqlalchemy import text
from sqlmodel import Session, SQLModel, create_engine

DEFAULT_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/calcms"
DATABASE_PROVIDER = os.getenv("DB_PROVIDER", "postgres").lower()
DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)


if DATABASE_PROVIDER != "postgres":
	raise ValueError(
		f"Unsupported DB_PROVIDER '{DATABASE_PROVIDER}'. "
		"Only 'postgres' is supported right now."
	)


engine = create_engine(
	DATABASE_URL,
	echo=False,
	pool_pre_ping=True,
)


def init_db() -> None:
	"""Create known tables once model classes are registered."""
	SQLModel.metadata.create_all(engine)


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
