from typing import List
from fastapi import APIRouter
from .. import store, models, schemas
from ..database import SessionLocal, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, FastAPI

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/datasets/", response_model=List[schemas.DatasetInDB])
async def read_datasets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    datasets = store.get_datasets(db, skip=skip, limit=limit)
    return datasets


@router.get("/datasets/{dataset_id}", tags=["datasets"])
async def read_dataset(dataset_id: str):
    return {"message": f"This will return dataset {dataset_id}"}


@router.post("/datasets/", tags=["datasets"])
async def create_dataset():
    return {"message": "This will create a new dataset"}


@router.get("/entries/", tags=["entries"])
async def read_entries():
    return {"message": "This will return a list of entries"}


@router.get("/entries/{entry_id}", tags=["entries"])
async def read_entry(entry_id: str):
    return {"message": f"This will return entry {entry_id}"}


@router.post("/entries/", tags=["entries"])
async def create_entry():
    return {"message": "This will create a new entry"}
