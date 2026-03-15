from fastapi import FastAPI

from calcms_api.db import DATABASE_URL, init_db, ping_database
from calcms_api.models import ContentItem as _ContentItem
from calcms_api.routes.content import router as content_router
from calcms_api.routes.health import router as health_router

# update eventually to use .env
hostname = "localhost"
serverPort = "8080"

app = FastAPI()

app.include_router(health_router)
app.include_router(content_router)


@app.on_event("startup")
def on_startup() -> None:
    init_db()
    db_ready = ping_database()
    if not db_ready:
        raise RuntimeError(
            "Database is not reachable. "
            f"Check DATABASE_URL: {DATABASE_URL}"
        )

@app.get("/")

def read_root():
    return {"message": "The webserver is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=hostname, port=int(serverPort))