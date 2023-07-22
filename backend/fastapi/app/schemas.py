from pydantic import BaseModel


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
