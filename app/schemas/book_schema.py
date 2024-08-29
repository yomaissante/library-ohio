from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    price: int
    description: str

class updateBook(BaseModel):
    title: str
    price: int
    description: str