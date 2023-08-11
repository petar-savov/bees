from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import api

app = FastAPI(title="Bees API", description="API for managing datasets of bees")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of origins you want to allow (e.g., ["http://localhost:3000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/v1")


@app.get("/")
def read_root():
    return {
        "app": "Bees API",
        "version": "0.1",
        "description": "Welcome to the Bees API. Use the /docs route to access the API documentation",
    }
