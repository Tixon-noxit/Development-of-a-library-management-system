import unittest
from unittest.mock import mock_open, patch
from utils.FileReader import FileReader


class TestFileReader(unittest.TestCase):

    def test_read_file_success(self):
        """Тест: корректное чтение файла"""
        mock_data = '{"books": [{"id": 1, "title": "Book Title", "author": "Author Name", "year": 2023, "status": "available"}]}'

        with patch("builtins.open", mock_open(read_data=mock_data)):
            reader = FileReader("test_file.json")
            result = reader.read_file()

            expected_result = {'books': [
                {'id': 1, 'title': 'Book Title', 'author': 'Author Name', 'year': 2023, 'status': 'available'}]}
            self.assertEqual(result, expected_result)

    def test_read_file_file_not_found(self):
        """Тест: файл не найден"""
        with patch("builtins.open", side_effect=FileNotFoundError):
            reader = FileReader("non_existent_file.json")
            result = reader.read_file()

            self.assertEqual(result, {})

    def test_read_file_invalid_json(self):
        """Тест: неверный формат JSON в файле"""
        invalid_json_data = "{ books: [id: 1, title: 'Invalid JSON'] }"

        with patch("builtins.open", mock_open(read_data=invalid_json_data)):
            reader = FileReader("invalid_json_file.json")
            result = reader.read_file()

            self.assertEqual(result, {})

    def test_read_file_empty(self):
        """Тест: чтение пустого файла"""
        with patch("builtins.open", mock_open(read_data="")):
            reader = FileReader("empty_file.json")
            result = reader.read_file()

            self.assertEqual(result, {})
