import unittest
from unittest.mock import MagicMock
from model.Model import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Настройка тестов."""
        self.mock_file_reader = MagicMock()
        self.mock_file_writer = MagicMock()

        self.mock_data = {
            "books": [
                {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020, "status": "available"},
                {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021, "status": "borrowed"}
            ]
        }
        self.mock_file_reader.read_file.return_value = self.mock_data
        self.library = Library(self.mock_file_reader, self.mock_file_writer)

    def test_add_book_success(self):
        """Тест для успешного добавления новой книги."""
        new_book = {"title": "New Book", "author": "New Author", "year": 2022}

        self.mock_file_writer.write_to_file.return_value = True

        result = self.library.add_book(new_book)
        self.assertTrue(result)
        self.mock_file_writer.write_to_file.assert_called_once()

    def test_add_book_failure(self):
        """Тест для неудачного добавления книги (например, ошибка записи)."""
        new_book = {"title": "New Book", "author": "New Author", "year": 2022}

        self.mock_file_writer.write_to_file.return_value = False

        result = self.library.add_book(new_book)
        self.assertFalse(result)

    def test_remove_book_success(self):
        """Тест для успешного удаления книги по ID."""
        result = self.library.remove_book(1)
        self.assertTrue(result)
        self.mock_file_writer.write_to_file.assert_called_once()

    def test_remove_book_failure(self):
        """Тест для неудачного удаления книги (например, книга не найдена)."""
        result = self.library.remove_book(999)
        self.assertFalse(result)

    def test_changing_the_status_of_a_book_failure_invalid_status(self):
        """Тест для ошибки при изменении статуса на невалидное значение."""
        result = self.library.changing_the_status_of_a_book(1, 'invalid_status')
        self.assertFalse(result)

    def test_changing_the_status_of_a_book_failure_book_not_found(self):
        """Тест для ошибки при изменении статуса несуществующей книги."""
        result = self.library.changing_the_status_of_a_book(999, 'borrowed')
        self.assertFalse(result)

    def test_display_all_books(self):
        """Тест для получения списка всех книг."""
        expected_books = [
            {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020, "status": "available"},
            {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021, "status": "borrowed"}
        ]
        result = self.library.display_all_books()
        self.assertEqual(result, expected_books)

    def test_search_book_found(self):
        """Тест для поиска книг по ключевому слову."""
        result = self.library.search_book("Book 1")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Book 1")

    def test_search_book_not_found(self):
        """Тест для случая, когда книга не найдена по ключевому слову."""
        result = self.library.search_book("Nonexistent Book")
        self.assertEqual(result, [])