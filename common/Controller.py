class Controller:
    """Тонкий контроллер для управления взаимодействием между моделью Library и интерфейсом"""
    def __init__(self, library):
        self.library = library

    def change_book_status(self, book_id, new_status):
        """Изменение статуса книги"""
        return self.library.changing_the_status_of_a_book(book_id, new_status)


    def search_books(self, keyword):
        """Поиск книг по ключевому слову"""
        return self.library.search_book(keyword)

    def get_all_books(self):
        """Получение всех книг"""
        return self.library.display_all_books()

    def add_new_book(self, new_book):
        """Добавление книги"""
        return self.library.add_book(new_book)

    def remove_book(self, book_id):
        """Удаление книги"""
        for book in self.library.books:
            if book['id'] == book_id:
                self.library.books.remove(book)
                return f"Книга '{book['title']}' удалена."
        return "Книга с указанным ID не найдена."
