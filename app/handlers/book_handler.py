from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.book_schema import Book, updateBook
from usecases.book_usecase import BookUseCase
from database import get_db

router = APIRouter()

@router.get("/books")
async def get_books(db: Session = Depends(get_db)):
    return BookUseCase.get_books(db)

@router.post("/books")
async def add_books(book: Book, db: Session = Depends(get_db)):
    added_book = BookUseCase.add_book(db, book.dict())
    return {'message': 'Your skibidi ohio book added!', 'book': added_book}

@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    deleted_book = BookUseCase.delete_book(db, book_id)
    if deleted_book:
        return {'message': 'Your skibidi ohio book deleted!'}
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/books/{book_id}")
async def update_book(book_id: int, book: updateBook, db: Session = Depends(get_db)):
    updated_book = BookUseCase.update_book(db, book_id, book.dict())
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")