from sqlalchemy.orm import Session
from . import models


def get_dataset(db: Session, dataset_id: str):
    return db.query(models.Dataset).filter(models.Dataset.id == dataset_id).first()


def get_datasets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dataset).offset(skip).limit(limit).all()


def create_dataset(db: Session, dataset: models.DatasetCreate):
    db_dataset = models.Dataset(**dataset.dict())
    db.add(db_dataset)
    db.commit()
    db.refresh(db_dataset)
    return db_dataset


# Do the same for the Entry model.


def get_entry(db: Session, entry_id: str):
    return db.query(models.Entry).filter(models.Entry.id == entry_id).first()


def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Entry).offset(skip).limit(limit).all()


def create_entry(db: Session, entry: models.EntryCreate):
    db_entry = models.Entry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry
