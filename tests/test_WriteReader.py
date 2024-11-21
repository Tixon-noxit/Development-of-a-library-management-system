import unittest
from unittest.mock import mock_open, patch
from utils.FileWriter import FileWriter


class TestFileWriter(unittest.TestCase):

    def setUp(self):
        """Настройка тестов."""
        self.file_path = 'test.json'
        self.writer = FileWriter(self.file_path)

    def test_write_to_file_success(self):
        """Тест для успешной записи данных в файл."""
        data = [{"id": 1, "title": "Book Title", "author": "Author Name", "year": 2023, "status": "available"}]

        with patch("builtins.open", mock_open()) as mocked_file:
            result = self.writer.write_to_file(data)
            mocked_file.assert_called_once_with(self.file_path, 'w', encoding='utf-8')
            mocked_file().write.assert_called_once()
            self.assertTrue(result)

    def test_write_to_file_failure(self):
        """Тест для неудачной записи данных в файл."""
        data = [{"id": 1, "title": "Book Title", "author": "Author Name", "year": 2023, "status": "available"}]

        with patch("builtins.open", side_effect=IOError):
            result = self.writer.write_to_file(data)
            self.assertFalse(result)


    def test_format_json_string(self):
        """Тест для форматирования строки в JSON."""
        data = "Some string"
        expected_json = '"Some string"'
        result = self.writer.format_json(data)
        self.assertEqual(result, expected_json)

    def test_format_json_int(self):
        """Тест для форматирования целого числа в JSON."""
        data = 123
        expected_json = '123'
        result = self.writer.format_json(data)
        self.assertEqual(result, expected_json)

    def test_format_json_float(self):
        """Тест для форматирования числа с плавающей запятой в JSON."""
        data = 123.45
        expected_json = '123.45'
        result = self.writer.format_json(data)
        self.assertEqual(result, expected_json)

    def test_format_json_bool(self):
        """Тест для форматирования булевого значения в JSON."""
        data = True
        expected_json = 'True'
        result = self.writer.format_json(data)
        self.assertEqual(result, expected_json)

