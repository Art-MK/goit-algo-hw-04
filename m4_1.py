# Вимоги до завдання:

# Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.
# author Глінський Артем Валерійович

def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print("Недійсний формат зарплати для рядка:", line)
                else:
                    print("Недійсний формат рядка:", line)

        if count == 0:
            return 0, 0  # повертаемо (0, 0) якщо в файлi нема валiдних данних

        average_salary = total / count
        return total, average_salary
    except FileNotFoundError:
        print("Файл не знайдено:", path)
    except Exception as err:
        print("Виникла помилка:", err)
        return None

# Приклад використання:
path_to_file = "m4_1_salaries.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
