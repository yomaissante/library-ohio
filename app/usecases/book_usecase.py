from fastapi import Depends
from repositories.book_repository import BookRepository

class BookUseCase:

    def __init__(self, bookRepo: BookRepository = Depends(BookRepository)):
        self.bookRepo = bookRepo

    def get_books(self):
        return self.bookRepo.get_books()
        # return BookRepository.get_books(db)

    def get_book_by_id(seld, book_id: int):
        return BookRepository.get_book_by_id(book_id)

    def add_book(self, book_data):
        return self.bookRepo.add_book(book_data)

    def delete_book(self, book_id: int):
        return self.bookRepo.delete_book(book_id)

    def update_book(self, book_id: int, book_data):
        return self.bookRepo.update_book(book_id, book_data)