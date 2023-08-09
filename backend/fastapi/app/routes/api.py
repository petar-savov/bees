from typing import List
from fastapi import APIRouter
from .. import store, schemas
from ..database import SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from fastapi.exceptions import HTTPException

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Retrieve a list of datasets with optional skip and limit parameters
@router.get("/datasets/", response_model=List[schemas.DatasetInDB])
async def read_datasets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    datasets = store.get_datasets(db, skip=skip, limit=limit)
    return datasets


# Retrieve a single dataset by its ID
@router.get("/datasets/{dataset_id}", tags=["datasets"])
async def read_dataset(dataset_id: str, db: Session = Depends(get_db)):
    dataset = store.get_dataset(db, dataset_id=dataset_id)
    return dataset


# Retrieve a list of entries with optional skip and limit parameters
@router.get("/entries/", response_model=List[schemas.EntryInDB], tags=["entries"])
async def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = store.get_entries(db, skip=skip, limit=limit)
    return entries


# Retrieve a single entry by its ID
@router.get("/entries/{entry_id}", response_model=schemas.EntryInDB, tags=["entries"])
async def read_entry(entry_id: str, db: Session = Depends(get_db)):
    entry = store.get_entry(db, entry_id=entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry


# Create a new entry using data provided in the request body
@router.post("/entries/", response_model=schemas.EntryInDB, tags=["entries"])
async def create_entry(entry: schemas.EntryCreate, db: Session = Depends(get_db)):
    db_entry = store.create_entry(db, entry=entry)
    return db_entry


# Create a new dataset using data provided in the request body
@router.post("/datasets/", response_model=schemas.DatasetInDB, tags=["datasets"])
async def create_dataset(dataset: schemas.DatasetCreate, db: Session = Depends(get_db)):
    db_dataset = store.create_dataset(db, dataset=dataset)
    return db_dataset
