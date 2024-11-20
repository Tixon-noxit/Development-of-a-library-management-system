from common.Common import statuses, book_details, main_menu

class CLI:
    """Класс для работы с пользовательским интерфейсом библиотеки"""

    def __init__(self, controller):
        self.controller = controller
        self.main_menu = main_menu

    @staticmethod
    def display_books_in_table(books):
        """Отображение всех книг в виде таблицы"""
        headers = ["ID", "Название", "Автор", "Год", "Статус"]

        column_widths = {header: len(header) for header in headers}

        for book in books:
            for i, key in enumerate(book_details):
                column_widths[headers[i]] = max(column_widths[headers[i]], len(str(book.get(key, ''))))

        def print_hr():
            print("+".join("-" * (column_widths[header] + 2) for header in headers))

        print_hr()
        print("".join(f" {header.ljust(column_widths[header])} |" for header in headers))
        print_hr()

        for book in books:
            print("".join(f" {str(book.get(book_details[i], '')).ljust(column_widths[headers[i]])} |" for i, header in
                          enumerate(headers)))
        print_hr()

    @staticmethod
    def hr():
        """Вывод разделителя"""
        print("=" * 30)

    def display_menu(self):
        """Отображение главного меню"""
        CLI.hr()
        print("     ГЛАВНОЕ МЕНЮ".center(30))
        CLI.hr()
        for key, value in self.main_menu.items():
            print(f'{key}. {value}')
        CLI.hr()

    @staticmethod
    def display_statuses():
        """Вывод на экран доступных статусов"""
        print("Доступные статусы:")
        for key, value in statuses.items():
            print(f'{key}. {value}')

    def change_status_menu(self):
        """Изменения статуса книги"""
        book_id = input("Укажите id книги для смены статуса: ")

        self.display_statuses()

        try:
            status_key = int(input("Укажите номер нового статуса книги: "))
            new_status = statuses.get(status_key)

            if new_status:
                if self.controller.change_book_status(book_id, new_status):
                    print(f"Статус книги {book_id} успешно изменён на {new_status}.")
                else:
                    print("Ошибка изменения статуса книги")
            else:
                print("Некорректный выбор статуса.")
        except ValueError:
            print("Неверный ввод статуса.")


    def add_book(self):
        """Метод для добавления новой книги."""
        print("=" * 30)

        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")

        try:
            year = int(year)
        except ValueError:
            print("Ошибка: год должен быть числом.")
            return

        new_book = {
            'title': title,
            'author': author,
            'year': year,
        }

        if self.controller.add_new_book(new_book):
            print(f"Книга '{title}' успешно добавлена!")
        else:
            print("Ошибка при добавлении книги.")

    def handle_choice(self):
        """Обработка выбора пользователя"""
        while True:
            try:
                self.hr()
                match int(input("Укажите номер(цифру) действия: ")):

                    case 1:
                        print(f"{self.main_menu.get(1)}")
                        self.add_book()
                    case 2:
                        print(f"{self.main_menu.get(2)}")
                        # self.add_book()
                    case 3:
                        print(f"{self.main_menu.get(3)} ...")
                        self.display_books_in_table(self.controller.search_books(input("Введите Название, Автора или Год издания(Что-то одно): ")))
                    case 4:
                        print(f"{self.main_menu.get(4)} ...")
                        self.display_books_in_table(self.controller.get_all_books())
                    case 5:
                        print(f"{self.main_menu.get(5)} ...")
                        self.change_status_menu()
                    case 6:
                        print(f"{self.main_menu.get(6)} ...")
                        break
                    case _:
                        print("Такого значения нет в списке!")
                self.hr()
            except ValueError:
                print("Пожалуйста, введите корректное число.")
                self.hr()