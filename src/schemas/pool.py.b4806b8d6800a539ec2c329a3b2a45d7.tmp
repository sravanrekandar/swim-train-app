from pydantic import BaseModel


class CreatePool(BaseModel):
    name: str
    location: str

    class Config:
        orm_mode = True


class Pool(CreatePool):
    id: int

    class Config:
        orm_mode = True
