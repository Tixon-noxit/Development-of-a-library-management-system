
class FileReader:
    def __init__(self, file_name):
        self.file_path = file_name

    def read_file(self):
        """Чтение и вывод содержимого JSON-файла с поддержкой вложенности."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as json_file:
                content = json_file.read().strip()
                if content:
                    return self.parse_json(content) if content else []

                else:
                    print("Файл пуст.")
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def parse_json(self, text):
        """Парсинг JSON-строки"""
        text = text.strip()
        if text.startswith("{"):
            return self.parse_object(text)
        elif text.startswith("["):
            return self.parse_array(text)
        elif text.startswith('"'):
            return self.parse_string(text)
        elif text.lower() == "true":
            return True
        elif text.lower() == "false":
            return False
        elif text.lower() == "null":
            return None
        else:
            return self.parse_number(text)

    def parse_object(self, text)->dict:
        """Парсинг JSON-объекта."""
        obj = {}
        text = text[1:-1].strip()
        if text:
            key_value_pairs = self.split_pairs(text)
            for pair in key_value_pairs:
                key, value = pair.split(":", 1)
                key = self.parse_string(key.strip())
                value = self.parse_json(value.strip())
                obj[key] = value
        return obj

    def parse_array(self, text)->list:
        """Парсинг JSON-массива."""
        arr = []
        text = text[1:-1].strip()
        if text:
            elements = self.split_elements(text)
            for element in elements:
                arr.append(self.parse_json(element.strip()))
        return arr

    @staticmethod
    def parse_string(text)->list:
        """Парсинг строки."""
        return text[1:-1]

    @staticmethod
    def parse_number(text):
        """Парсинг числовых значений (целые числа и числа с плавающей запятой)."""
        try:
            if '.' in text:
                return float(text)
            return int(text)
        except ValueError:
            raise ValueError(f"Ошибка при парсинге числа: {text}")

    @staticmethod
    def split_pairs(text)->list:
        """Разделение строк на пары ключ-значение."""
        pairs = []
        balance = 0
        current_pair = []
        for char in text:
            if char == ',' and balance == 0:
                pairs.append(''.join(current_pair).strip())
                current_pair = []
            else:
                if char == '{' or char == '[':
                    balance += 1
                elif char == '}' or char == ']':
                    balance -= 1
                current_pair.append(char)
        if current_pair:
            pairs.append(''.join(current_pair).strip())
        return pairs

    @staticmethod
    def split_elements(text)->list:
        """Разделение элементов массива."""
        elements = []
        balance = 0
        current_element = []
        for char in text:
            if char == ',' and balance == 0:
                elements.append(''.join(current_element).strip())
                current_element = []
            else:
                if char == '{' or char == '[':
                    balance += 1
                elif char == '}' or char == ']':
                    balance -= 1
                current_element.append(char)
        if current_element:
            elements.append(''.join(current_element).strip())
        return elements