from fastapi import Depends
from sqlalchemy.orm import Session
from models.model import Book as BookModel
from database import get_db

class BookRepository:
    def get_session(self) -> Session:
        db_generator = get_db()
        db_session = next(db_generator)
        return db_session

    def get_books(self):
        db = self.get_session()
        return db.query(BookModel).all()

    def get_book_by_id(self, db, book_id: int):
        return db.query(BookModel).filter(BookModel.id == book_id).first()

    def add_book(self, book_data: dict):
        db = self.get_session()
        db_book = BookModel(**book_data)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int):
        db = self.get_session()
        db_book = self.get_book_by_id(db, book_id)
        if db_book:
            db.delete(db_book)
            db.commit()
            return db_book
        return None

    def update_book(self, book_id: int, book_data: dict):
        db = self.get_session()
        db_book = self.get_book_by_id(db, book_id)
        if db_book:
            for key, value in book_data.items():
                setattr(db_book, key, value)
            db.commit()
            db.refresh(db_book)
            return db_book
        return None