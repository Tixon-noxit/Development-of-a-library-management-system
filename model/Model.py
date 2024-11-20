from common.common import book_details


class Library:
    """Модель для работы с книгами"""
    def __init__(self, file_reader):
        self.reader = file_reader
        self.data = self.reader.read_file()
        self.books = self.data.get('books', []) if isinstance(self.data, dict) else self.data



    def changing_the_status_of_a_book(self):
        """ Изменение статуса книги"""
        pass


    def display_all_books(self)->list:
        """Получение списка книг из данных."""
        books = []
        if isinstance(self.data, dict) and 'books' in self.data:
            books = self.data['books']
        elif isinstance(self.data, list):
            books = self.data

        book_list = []
        for book in books:
            if isinstance(book, dict):
                book_info = {
                    book_details[0]: book.get('id'),
                    book_details[1]: book.get('title'),
                    book_details[2]: book.get('author'),
                    book_details[3]: book.get('year'),
                    book_details[4]: book.get('status')
                }
                book_list.append(book_info)
        return book_list

    def search_book(self,  keyword):
        """Поиск книги"""
        results = []
        keyword = keyword.lower()

        for book in self.books:
            if any(keyword in str(value).lower() for key, value in book.items() if key != book_details[0]):
                results.append(book)

        return results


    def remove_book(self):
        """Удаление книги"""
        pass

    def add_book(self):
        """Добавление книги"""
        pass