# Вимоги до завдання:

# Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.
# author Глінський Артем Валерійович

#ремарка: без обробки помилок. т.к у наступних ДЗ будемо використовивати декоратор
#ремарка2: без будь яких додаткових верiфiкацiй.
#ремарка3: тут булоб краще описати логiку у ршзних файлах. main.py, parsers.py , handlers.py - тут описано у одному , як базовий прототип на майбутьне


# парсер вводу
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# функцiя додовання контакту
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# функцiя змiни контакту
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact phone number updated."
    else:
        return "Contact not found."

# функцiя лiстiнгу контакту
def get_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return "Contact not found."

# функцiя лiстiнгу усix контактiв
def show_all_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            return(f"{name}: {phone}")
    else:
        return("No contacts found.")

# entrypoint - головна фунцiя
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print("List of contacts:")
            show_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
