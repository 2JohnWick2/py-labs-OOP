BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    },
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализирует объект книги.
        :param id_: идентификатор книги
        :param name: название книги
        :param pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращаем строковое представление книги для пользователя.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает валидную python строку, по которой можно инициализировать
        точно такой же экземпляр книги.
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


class Library:
    def __init__(self, books=None):
        """
        Инициализирует библиотеку книг.
        :param books: список книг, по умолчанию пустой список.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий идентификатор для новой книги в библиотеке.
        Если библиотека пуста, возвращает 1. Иначе возвращает последний id + 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её id.
        :param book_id: идентификатор книги
        :return: индекс книги в списке
        :raises ValueError: если книга с таким id не найдена.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(
            id_=book_dict["id"],
            name=book_dict["name"],
            pages=book_dict["pages"]
        )
        for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())
    print(library_with_books.get_index_by_book_id(1))
