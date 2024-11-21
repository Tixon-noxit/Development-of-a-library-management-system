from common.Common import book_details, statuses
from utils.FileReader import FileReader
from utils.FileWriter import FileWriter


class Library:
    """
    Класс для управления библиотекой книг. Поддерживает добавление, удаление,
    изменение статуса книг, поиск и отображение всех книг.
    """
    def __init__(self,  file_reader: FileReader, file_writer: FileWriter):
        """
                Инициализация библиотеки.

                :param file_reader: Объект для чтения данных из файла.
                :param file_writer: Объект для записи данных в файл.
        """
        self.reader = file_reader
        self.file_writer = file_writer
        self.data = self.reader.read_file()
        self.books = self.data.get('books', []) if isinstance(self.data, dict) else self.data


    def changing_the_status_of_a_book(self,  book_id: int, new_status: str) -> bool:
        """
                Изменение статуса книги.

                :param book_id: Идентификатор книги.
                :param new_status: Новый статус книги.
                :return: True, если статус изменён успешно, иначе False.
        """
        for book in self.books:
            if book['id'] == int(book_id):
                if new_status in statuses.values():
                    book['status'] = new_status
                    self.file_writer.write_to_file(self.books)
                    return True
                else:
                    return False
        return False


    def display_all_books(self)-> list[dict]:
        """
        Получение списка всех книг.

        :return: Список словарей с информацией о книгах.
        """
        books = []
        if isinstance(self.data, dict) and 'books' in self.data:
            books = self.data['books']
        elif isinstance(self.data, list):
            books = self.data

        book_list = []
        for book in books:
            if isinstance(book, dict):
                book_info = {detail: book.get(detail) for detail in book_details}
                book_list.append(book_info)
        return book_list


    def search_book(self,  keyword: str) -> list[dict]:
        """
        Поиск книг по ключевому слову. Ключевое слово проверяется в полях
        title, author и year.

        :param keyword: Ключевое слово для поиска.
        :return: Список книг, соответствующих ключевому слову.
        """
        results = []
        keyword = keyword.lower()

        for book in self.books:
            if any(keyword in str(value).lower() for key, value in book.items() if key != book_details[0]):
                results.append(book)

        return results


    def remove_book(self, book_id: int) -> bool:
        """
        Удаление книги по её идентификатору.

        :param book_id: Идентификатор книги для удаления.
        :return: True, если книга успешно удалена, иначе False.
        """
        try:
            book_id = int(book_id)
            book_to_remove = next((book for book in self.books if book['id'] == book_id), None)

            if book_to_remove:
                self.books.remove(book_to_remove)
                self.file_writer.write_to_file(self.books)
                return True
            return False
        except:
            return False


    def add_book(self, new_book: dict) -> bool:
        """
                Добавление новой книги в библиотеку.

                :param new_book: Словарь с информацией о новой книге (title, author, year).
                :return: True, если книга успешно добавлена, иначе False.
        """
        try:
            new_id = max([book['id'] for book in self.books], default=0) + 1

            ordered_book = {
                'id': new_id,
                'title': new_book.get('title', ''),
                'author': new_book.get('author', ''),
                'year': new_book.get('year', ''),
                'status': 'в наличии'
            }

            self.books.append(ordered_book)
            if self.file_writer.write_to_file(self.books):
                return True
            else: return False
        except:
            return False