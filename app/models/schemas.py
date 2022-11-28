from datetime import date
from pydantic import BaseModel


class Record(BaseModel):
    id: str
    text: str
    label: int

    class Config:
        orm_mode = True