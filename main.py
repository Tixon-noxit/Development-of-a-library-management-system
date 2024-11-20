from cli import CLI as console
from common import common
from model.Model import Library
from model.FileReader import FileReader


def main():
    # Проверка консольного вывода
    # console.menu(common.main_menu)
    # choice = console.choice(common.main_menu)

    # Проверка чтения из .json
    file_reader = FileReader(common.FILE_NAME)
    # print(file_reader.read_file())

    # Проверка получения списка книг
    library = Library(file_reader)
    # for book in library.display_all_books():
    #     print(book)

    book = library.search_book("1984")
    if book:
        print(f"Найдена книга: {book}")
    else:
        print("Книга не найдена.")




if __name__ == '__main__':
    main()