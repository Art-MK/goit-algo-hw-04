# Вимоги до завдання:

# Створіть віртуальне оточення Python для ізоляції залежностей проєкту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.
# author Глінський Артем Валерійович

#додаткове викорастанi символи Box Drawing https://en.wikipedia.org/wiki/Box_Drawing

import sys
from pathlib import Path
from colorama import init ,Fore

# Ініціалізуємо colorama для підтримки кольорового виводу , щоб по завершенню скрипта повертати дефолтну кольорову схему задаемо autoreset
init(autoreset=True)

def display_colour_dir_tree(directory_path, indent=''):
    try:
        directory = Path(directory_path)

        # Перевіряємо, чи директорія існує
        if directory.exists() and directory.is_dir():
            for item in directory.iterdir():
                if item.is_dir():
                    print(Fore.BLUE + indent + '├── ' + item.name)
                    display_colour_dir_tree(item, indent + '│   ')
                else:
                    print(Fore.GREEN + indent + '├── ' + item.name)
        else:
            print(Fore.RED + "Шлях не існує або не веде до директорії.")
    except PermissionError:
        print(Fore.RED + "Немає дозволу на доступ до директорії.")
    except Exception as err:
        print(Fore.RED + f"Помилка: ", err)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях до директорії>")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_colour_dir_tree(directory_path)
