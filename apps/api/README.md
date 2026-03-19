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

Copy the example env file and set your values:

```bash
cp .env.example .env
```

Set environment variables in `.env` before starting the API:

```bash
# Optional for future multi-db support. Only "postgres" works right now.
DB_PROVIDER=postgres

# Set real credentials/host/db name for your local Postgres.
DATABASE_URL=postgresql+psycopg2://<db_user>:<db_password>@localhost:5432/<db_name>
```

Then run:

```bash
uv sync
uv run calcms-preflight
uv run alembic upgrade head
uv run python -m calcms_api.main
```

If you see a warning about `VIRTUAL_ENV` not matching the project `.venv`, either
deactivate your currently active shell environment first, or run with:

```bash
uv run --active calcms-preflight
uv run --active alembic upgrade head
```

At startup, the app verifies DB connectivity and exits with an error if the
database is unreachable. Schema creation is not run automatically.

### Migrations (Alembic)

Preflight check before migrations:

```bash
uv run calcms-preflight
```

Apply all migrations:

```bash
uv run alembic upgrade head
```

Create a new migration after model changes:

```bash
uv run alembic revision --autogenerate -m "describe_change"
```

Rollback one step:

```bash
uv run alembic downgrade -1
```

## Running With Docker

Use Docker Compose to run PostgreSQL and the API together:

```bash
docker compose up --build
```

Compose reads DB credentials from `.env`.

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

## CRUD Smoke Test

Once the API and Postgres are running, test CRUD on `/content`.

Create:

```bash
curl -X POST http://127.0.0.1:8080/content \
    -H "Content-Type: application/json" \
    -d '{"title":"First Post","body":"Hello from Postgres","published":false}'
```

List:

```bash
curl http://127.0.0.1:8080/content
```

Read one:

```bash
curl http://127.0.0.1:8080/content/1
```

Update:

```bash
curl -X PATCH http://127.0.0.1:8080/content/1 \
    -H "Content-Type: application/json" \
    -d '{"published":true}'
```

Delete:

```bash
curl -X DELETE http://127.0.0.1:8080/content/1
```
