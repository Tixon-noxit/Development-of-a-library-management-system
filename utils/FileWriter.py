class FileWriter:
    """
        Класс для записи данных в файл в формате JSON.
    """
    def __init__(self, file_path: str)->None:
        """
                Инициализация FileWriter.

                :param file_path: Путь к файлу, в который будут записываться данные.
        """
        self.file_path = file_path

    def write_to_file(self, data: list | dict) -> bool:
        """
        Запись данных в файл в формате JSON.

        :param data: Данные (список или словарь) для записи в файл.
        :return: True, если запись выполнена успешно, иначе False.
        """
        try:
            books_data = {
                "books": data
            }
            json_content = self.format_json(books_data)
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write(json_content)
            return True
        except:
            return False

    def format_json(self, data: list | dict | str | int | float | bool | None) -> str:
        """
        Форматирование данных в строку JSON.

        :param data: Данные для форматирования (словарь, список, строка, число, bool, None).
        :return: Строка в формате JSON.
        """
        if isinstance(data, dict):
            json_str = "{\n"
            for key, value in data.items():
                json_str += f'    "{key}": {self.format_json(value)},\n'
            json_str = json_str.rstrip(",\n") + "\n}"
            return json_str
        elif isinstance(data, list):
            json_str = "[\n"
            for item in data:
                json_str += f"    {self.format_json(item)},\n"
            json_str = json_str.rstrip(",\n") + "\n]"
            return json_str
        elif isinstance(data, str):
            return f'"{data}"'
        else:
            return str(data)
