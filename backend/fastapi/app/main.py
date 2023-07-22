from fastapi import FastAPI
from .routes import api

app = FastAPI(title="Bees API", description="API for managing datasets of bees")

app.include_router(api.router, prefix="/v1")


@app.get("/")
def read_root():
    return {
        "app": "Bees API",
        "version": "0.1",
        "description": "Welcome to the Bees API. Use the /docs route to access the API documentation",
    }
