# Вимоги до завдання:

# Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
# Функція має повертати список словників, де кожен словник містить інформацію про одного кота.
# author Глінський Артем Валерійович

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    try:
                        cat_info = {
                            "id": cat_data[0],
                            "name": cat_data[1],
                            "age": int(cat_data[2])
                        }
                    except ValueError:
                        print("Недійсний формат даних для рядка:", line)
                else:
                    print("Недійсний формат рядка:", line)

                cats_info.append(cat_info)

    except FileNotFoundError:
        print("Файл не знайдено")
    except Exception as err:
        print("Виникла помилка:", err)

    return cats_info

# Приклад використання:
path_to_file = "m4_2_cats.txt"
cats_info = get_cats_info(path_to_file)
print(cats_info)
