from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    price: int
    quantity: int
    description: str

class updateBook(BaseModel):
    title: str
    price: int
    quantity: int
    description: str