from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.book_schema import Book, updateBook
from usecases.book_usecase import BookUseCase
from database import get_db

router = APIRouter()

@router.get("/books")
async def get_books(bookUsecase: BookUseCase = Depends(BookUseCase)):
    return bookUsecase.get_books()  

@router.post("/books")
async def add_books(book: Book, bookUsecase: BookUseCase = Depends(BookUseCase)):
    added_book = bookUsecase.add_book(book.dict())
    return {'message': 'Your skibidi ohio book added!', 'book': added_book}

@router.delete("/books/{book_id}")
async def delete_book(book_id: int, bookUsecase: BookUseCase = Depends(BookUseCase)):
    deleted_book = bookUsecase.delete_book(book_id)
    if deleted_book:
        return {'message': 'Your skibidi ohio book deleted!'}
    raise HTTPException(status_code=404, detail="Book not found")

@router.put("/books/{book_id}")
async def update_book(book_id: int, book: updateBook, bookUsecase: BookUseCase = Depends(BookUseCase)):
    updated_book = bookUsecase.update_book(book_id, book.dict())
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail="Book not found")