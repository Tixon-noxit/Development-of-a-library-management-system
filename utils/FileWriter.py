class FileWriter:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_to_file(self, data)->bool:
        """Запись данных в файл в формате JSON"""
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

    def format_json(self, data):
        """Форматирование данных в строку JSON"""
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
