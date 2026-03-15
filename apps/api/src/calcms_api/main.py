from fastapi import FastAPI

from calcms_api.routes.health import router as health_router

# update eventually to use .env
hostname = "localhost"
serverPort = "8080"

app = FastAPI()

app.include_router(health_router)

@app.get("/")

def read_root():
    return {"message": "The webserver is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=hostname, port=int(serverPort))