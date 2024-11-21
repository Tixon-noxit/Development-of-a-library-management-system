# Имя файла, в котором будет храниться информация о книгах
FILE_NAME = "library.json"

# Основное меню, где ключи - это номера действий, а значения - это описания действий
main_menu = {
    1: 'Добавление книги',  # Действие для добавления книги
    2: 'Удаление книги',  # Действие для удаления книги
    3: 'Поиск книги',  # Действие для поиска книги
    4: 'Отображение всех книг',  # Действие для отображения всех книг
    5: 'Изменение статуса книги',  # Действие для изменения статуса книги
    6: 'Выход из программы'  # Действие для выхода из программы
}

# Статусы, которые могут быть у книги, где ключи - это числовые коды статуса,
# а значения - текстовые представления статусов
statuses = {
    1: 'в наличии',  # Книга есть в наличии
    2: 'выдана'  # Книга выдана
}

# Список деталей книги, используемых для отображения данных о книге
book_details = ['id', 'title', 'author', 'year', 'status']  # Атрибуты книги
