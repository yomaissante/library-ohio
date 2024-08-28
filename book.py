from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict


## Base Model
class Book(BaseModel):
    id: int
    title: str
    price: int
    description: str

class updateBook(BaseModel):
    title: str
    price: int
    description: str

## API Route
app = FastAPI()

list_books: Dict[int, Book] = {
    1: {"id":1,"title":"Bonheur, Le","price":100,"description":"Unsp athscl type of bypass of the extremities, left leg"},
    2: {"id":2,"title":"Makai Tensho: Samurai Reincarnation (Makai tenshô)","price":91,"description":"Cystic meniscus, other medial meniscus"},
    3: {"id":3,"title":"The Mountain of the Cannibal God","price":80,"description":"Oth fx of low end r rad, subs for opn fx type I/2 w malunion"},
    4: {"id":4,"title":"Darby O'Gill and the Little People","price":8,"description":"Arthropathic psoriasis"},
    5: {"id":5,"title":"Ossessione","price":33,"description":"Oth cond assoc w female genital organs and menstrual cycle"}
}

@app.get('/')
def lobby():
    return {'message': 'Welcome to veri-blubuk awek awek gedagedigedagedao!'}

@app.get("/books")
async def get_books():
    return list_books

@app.post("/books")
async def add_books(book: Book):
    list_books.append(book)
    return {'message': 'Your skibidi ohio book added!'}

@app.delete("/books/{book_id}")
async def del_books(book_id: int):
    del list_books[book_id]
    return {'message': 'Your skibidi ohio book deleted!'}

@app.put("/books/{book_id}")
async def update_books(book_id: int, book: updateBook):
    list_books[book_id] = book
    return list_books[book_id]