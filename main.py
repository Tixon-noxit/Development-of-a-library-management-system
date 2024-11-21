# Импорт необходимых классов и модулей
from utils.FileReader import FileReader  # Класс для чтения данных из файла
from utils.FileWriter import FileWriter  # Класс для записи данных в файл
from common.Common import FILE_NAME  # Имя файла с данными
from model.Model import Library  # Класс библиотеки, реализующий логику работы с книгами
from common import Controller  # Контроллер, управляющий взаимодействием между моделью и интерфейсом
from cli.CLI import CLI  # Класс для отображения пользовательского интерфейса (CLI)

def main():
    """Основная функция, которая инициализирует все компоненты приложения и запускает работу с пользовательским интерфейсом."""
    # Создание экземпляра FileReader для чтения данных из файла
    app_reader = FileReader(FILE_NAME)

    # Создание экземпляра FileWriter для записи данных в файл
    add_writer = FileWriter(FILE_NAME)

    # Инициализация модели библиотеки с использованием файлового читателя и писателя
    app_library = Library(app_reader, add_writer)

    # Создание экземпляра контроллера для управления библиотекой
    app_controller = Controller.Controller(app_library)

    # Создание экземпляра CLI для работы с пользовательским интерфейсом
    app_cli = CLI(app_controller)

    # Отображение главного меню
    app_cli.display_menu()

    # Обработка выбора пользователя
    app_cli.handle_choice()

if __name__ == '__main__':
    main()
