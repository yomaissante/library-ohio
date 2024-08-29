from repositories.book_repository import BookRepository

class BookUseCase:
    @staticmethod
    def get_books(db):
        return BookRepository.get_books(db)

    @staticmethod
    def get_book_by_id(db, book_id: int):
        return BookRepository.get_book_by_id(db, book_id)

    @staticmethod
    def add_book(db, book_data):
        return BookRepository.add_book(db, book_data)

    @staticmethod
    def delete_book(db, book_id: int):
        return BookRepository.delete_book(db, book_id)

    @staticmethod
    def update_book(db, book_id: int, book_data):
        return BookRepository.update_book(db, book_id, book_data)