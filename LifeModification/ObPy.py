import subprocess

def install_module(module):
    try:
        __import__(module)
        print(f'{module} уже установлен')
    except ImportError:
        print(f'Установка {module}...')
        subprocess.call(['pip', 'install', module])

def update_module(module):
    try:
        subprocess.call(['pip', 'install', '--upgrade', module])
        print(f'{module} успешно обновлен')
    except Exception as e:
        print(f'Ошибка при обновлении {module}: {str(e)}')

def main():
    modules = {
        'TelegramClient': False,
        'asyncio': False,
        'telethon': False,
        'Flask': False,
        'Telebot': False,
        'Kivy': False,
        'math': False,
        'random': False,
        'datetime': False,
        'os': False,
        'sys': False,
        'json': False,
        'urllib': False,
        'sqlite3': False,
        'tkinter': False,
        'numpy': False,
        'pandas': False,
        'matplotlib': False,
        'scipy': False,
        'sklearn': False,
        'tensorflow': False,
        'keras': False,
        'pygame': False,
        'colorama': False,
        'time': False
    }

    print('Добро пожаловать в OBPY!')
    print('Выберите модули для установки или обновления:')

    while True:
        print()
        print('Список доступных модулей:')
        for i, module in enumerate(modules, start=1):
            print(f'{i}. {module}')

        choice = input('Выберите модуль (введите номер) или нажмите "q" для выхода: ')

        if choice == 'q':
            print("")
            break

        try:
            choice = int(choice)
            module = list(modules.keys())[choice - 1]

            install_or_update = input(f'Выбран модуль {module}. Введите "i" для установки или "u" для обновления: ')

            if install_or_update == 'i':
                install_module(module)
            elif install_or_update == 'u':
                update_module(module)
            else:
                print('Неверная команда. Попробуйте снова.')
        except (ValueError, IndexError):
            print('Неверный ввод. Попробуйте снова.')

correct_code = "" # задаем правильный код доступа
print("")
code = input("Введите код доступа (нажать Enter): ") # запрашиваем код доступа у пользователя

if code == correct_code: # проверяем, соответствует ли введенный код правильному
    print("Доступ разрешен")
    # здесь можно добавить код, который будет выполняться при успешном вводе кода
else:
    print("Неверный код доступа")
    # здесь можно добавить код, который будет выполняться при неправильном вводе кода
    # например, можно вызвать функцию, которая завершает программу
    exit()
if __name__ == '__main__':
    main()