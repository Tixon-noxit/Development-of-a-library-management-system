from model.Model import Library


class Controller:
    """
    Контроллер для управления взаимодействием между моделью Library и пользовательским интерфейсом.
    """
    def __init__(self, library: Library):
        """
                Инициализация контроллера.

                :param library: Экземпляр модели Library для работы с книгами.
        """
        self.library = library

    def change_book_status(self, book_id: int, new_status: str) -> bool:
        """
        Изменение статуса книги.

        :param book_id: Идентификатор книги.
        :param new_status: Новый статус книги.
        :return: True, если статус изменён успешно, иначе False.
        """
        return self.library.changing_the_status_of_a_book(book_id, new_status)

    def search_books(self, keyword: str) -> list[dict]:
        """
        Поиск книг по ключевому слову.

        :param keyword: Ключевое слово для поиска.
        :return: Список книг, соответствующих ключевому слову.
        """
        return self.library.search_book(keyword)

    def get_all_books(self)-> list[dict]:
        """
        Получение всех книг из библиотеки.

        :return: Список всех книг в библиотеке.
        """
        return self.library.display_all_books()

    def add_new_book(self, new_book: dict) -> bool:
        """
        Добавление новой книги.

        :param new_book: Словарь с информацией о книге (title, author, year).
        :return: True, если книга успешно добавлена, иначе False.
        """
        return self.library.add_book(new_book)

    def remove_book(self, book_id: int) -> bool:
        """
        Удаление книги из библиотеки.

        :param book_id: Идентификатор книги для удаления.
        :return: True, если книга успешно удалена, иначе False.
        """
        return self.library.remove_book(book_id)

