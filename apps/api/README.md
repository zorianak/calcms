# CalCMS API

Bare-bones Python backend for CalCMS.

## Structure

```
src/calcms_api/
├── main.py          # HTTP server entry point — write your server logic here
├── db/
│   └── connection.py  # Abstract DB interface — implement for your database (e.g. PostgreSQL)
├── kafka/
│   └── client.py    # Kafka producer/consumer stubs
└── graphql/
    └── schema.py    # Strawberry GraphQL schema
```

## Running

```bash
# Install dependencies
pip install -e ".[dev]"

# Start server (placeholder — implement your HTTP server in main.py)
python -m calcms_api.main
```

## Adding PostgreSQL

PostgreSQL is the default database provider.

Set environment variables before starting the API:

```bash
# Optional for future multi-db support. Only "postgres" works right now.
DB_PROVIDER=postgres

# Adjust credentials/host/db name for your local Postgres.
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/calcms
```

Then run:

```bash
uv sync
uv run python -m calcms_api.main
```

At startup, the app verifies DB connectivity and exits with an error if the
database is unreachable.

## Running With Docker

Use Docker Compose to run PostgreSQL and the API together:

```bash
docker compose up --build
```

Once containers are healthy, test the API:

```bash
curl http://127.0.0.1:8080/health
```

Stop the stack:

```bash
docker compose down
```

To remove the Postgres data volume too:

```bash
docker compose down -v
```

## GraphQL

The GraphQL schema is in `src/calcms_api/graphql/schema.py`.
Add types and resolvers there. Strawberry integrates with most Python web
frameworks (ASGI/WSGI).
