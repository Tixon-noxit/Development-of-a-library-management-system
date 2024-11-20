def hr():
    print("=" * 30)

def menu(main_menu):
    hr()
    print("     ГЛАВНОЕ МЕНЮ".center(30))  # Заголовок меню
    hr()
    for key, value in main_menu.items():
        print(f'{key}. {value}')  # Пункты меню
    hr()

def choice(main_menu)->int:
    while True:
        try:
            a = int(input("Укажите номер(цифру) действия: "))
            hr()
            if a in main_menu.keys():
                print(f"Вы выбрали: {main_menu[a]}")
                hr()
                return a
            else:
                print("Такого значения нет в списке!")
                hr()
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            hr()