from sqlalchemy.orm import Session
from models.model import Book as BookModel

class BookRepository:

    @staticmethod
    def get_books(db: Session):
        return db.query(BookModel).all()

    @staticmethod
    def get_book_by_id(db: Session, book_id: int):
        return db.query(BookModel).filter(BookModel.id == book_id).first()

    @staticmethod
    def add_book(db: Session, book_data: dict):
        db_book = BookModel(**book_data)
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def delete_book(db: Session, book_id: int):
        db_book = BookRepository.get_book_by_id(db, book_id)
        if db_book:
            db.delete(db_book)
            db.commit()
            return db_book
        return None

    @staticmethod
    def update_book(db: Session, book_id: int, book_data: dict):
        db_book = BookRepository.get_book_by_id(db, book_id)
        if db_book:
            for key, value in book_data.items():
                setattr(db_book, key, value)
            db.commit()
            db.refresh(db_book)
            return db_book
        return None