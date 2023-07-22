# File: backend/fastapi/app/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from typing import Optional

Base = declarative_base()


# SQLAlchemy Models
class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(String, primary_key=True)
    name = Column(String)


class Entry(Base):
    __tablename__ = "entries"

    id = Column(String, primary_key=True)
    label = Column(String)
    status = Column(String)
    dataset_id = Column(String)  # foreign key to Dataset.id


# Pydantic Models
class DatasetBase(BaseModel):
    name: str


class DatasetCreate(DatasetBase):
    pass


class DatasetInDB(DatasetBase):
    id: str

    class Config:
        orm_mode = True


class EntryBase(BaseModel):
    label: str
    status: str
    dataset_id: str  # foreign key to Dataset.id


class EntryCreate(EntryBase):
    pass


class EntryInDB(EntryBase):
    id: str

    class Config:
        orm_mode = True
