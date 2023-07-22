from fastapi import APIRouter
from . import store, models

router = APIRouter()


@router.get("/datasets/", tags=["datasets"])
async def read_datasets():
    return {"message": "This will return a list of datasets"}


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
