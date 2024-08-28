from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Dict

from sqlalchemy.orm import Session
from database import SessionLocal, engine
from model import Book as BookModel, Base

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

# list_books: Dict[int, Book] = {
#     1: {"id":1,"title":"Bonheur, Le","price":100,"description":"Unsp athscl type of bypass of the extremities, left leg"},
#     2: {"id":2,"title":"Makai Tensho: Samurai Reincarnation (Makai tenshô)","price":91,"description":"Cystic meniscus, other medial meniscus"},
#     3: {"id":3,"title":"The Mountain of the Cannibal God","price":80,"description":"Oth fx of low end r rad, subs for opn fx type I/2 w malunion"},
#     4: {"id":4,"title":"Darby O'Gill and the Little People","price":8,"description":"Arthropathic psoriasis"},
#     5: {"id":5,"title":"Ossessione","price":33,"description":"Oth cond assoc w female genital organs and menstrual cycle"}
# }

@app.get('/')
def lobby():
    return {'message': 'Welcome to veri-blubuk awek awek gedagedigedagedao!'}

@app.get("/books")
async def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()

@app.post("/books")
async def add_books(book: Book, db: Session = Depends(get_db)):
    db_book = BookModel(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return {'message': 'Your skibidi ohio book added!'}

@app.delete("/books/{book_id}")
async def del_books(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {'message': 'Your skibidi ohio book deleted!'}

@app.put("/books/{book_id}")
async def update_books(book_id: int, book: updateBook, db: Session = Depends(get_db)):
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book