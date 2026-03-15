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

Uncomment the `psycopg` dependency in `pyproject.toml`, then implement
`DatabaseConnection` in `src/calcms_api/db/connection.py`.

## GraphQL

The GraphQL schema is in `src/calcms_api/graphql/schema.py`.
Add types and resolvers there. Strawberry integrates with most Python web
frameworks (ASGI/WSGI).
