import json
import datetime

application = {}
filename = "notes_file.txt"


def open_file():
    with open(filename, "r", encoding="'UTF-8'") as file:
        notes = file.readlines()
    for id, note in enumerate(notes, 1):
        note = note.strip().split(";")
        application[id] = note
    # print(application)


def save_file():
    data = []
    for note in application.values():
        note = ";".join(note)
        data.append(note)
    data = "\n".join(data)
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(data)


def show_file(app: dict):
    print()
    for id, note in app.items():
        print(f"{id: >3}; {note[0]:<10} ; {note[1]:<20} ; {note[2]:40} ")
    print()


def add_new_note():
    # number = input("Введите номер: ")
    name = input("Ведите название заметки: ")
    content = input("Введите содержание заметки: ")
    timestamp = input("Введите дату внесения заметки (в формате чч-мм-гг ): ")
    id = max(application.keys()) + 1
    application[id] = [name, content, timestamp]
    return name


def find_note():
    result = {}
    word = input("Введите слово для поиска: ").lower()
    for id, note in application.items():
        if word in "".join(note).lower():
            result[id] = note
    print(f"Заметка, содержащая слово '{word.title()}', не найдена!")
    return result


def edit_note():
    result = find_note()
    show_file(result)
    id = int(input("Введите ID заметки, которую хотите изменить:  "))
    c_name, c_content, c_timestamp = application[id]
    # number = input(" ")
    name = input("Ведите новое название заметки (или оставьте поле пустым, если название не изменится): ")
    content = input("Введите новое содержание заметки (или оставьте поле пустым, если содержание не изменится): ")
    timestamp = input("Введите новую дату заметки (или оставьте поле пустым, если дата не изменится): ")
    application[id] = [name if name else c_name, content if content else c_content,
                       timestamp if timestamp else c_timestamp]
    return name if name else c_name


def del_note():
    result = find_note()
    show_file(result)
    id = int(input("Введите ID заметки,которую хотите удалить: "))
    name = application.pop(id)
    return name[0]


def menu_application():
    txt_zapros = "Главное меню\n" \
                 "1. Открыть файл. \n" \
                 "2. Сохранить файл.\n" \
                 "3. Показать все заметки.\n" \
                 "4. Записать новые данные в файл.\n" \
                 "5. Найти заметку.\n" \
                 "6. Внести изменения в файл.\n" \
                 "7. Удалить заметку.\n" \
                 "8. Выйти из программы.\n"
    while True:
        print(txt_zapros)
        choise = input("Выберите пункт главного меню: ")
        print()
        if choise == "1":
            open_file()
            print("\nПриложение 'Заметки' загружено.\n")
            print()
        elif choise == "2":
            save_file()
            print("\nЗаметки сохранены.\n")
            print()
        elif choise == "3":
            show_file(application)
            print()
        elif choise == "4":
            name = add_new_note()
            print(f"\nНовая заметка '{name.title()}' успешно сохранена.\n")
        elif choise == "5":
            result = find_note()
            show_file(result)
            print()
        elif choise == "6":
            name = edit_note()
            print(f"\nЗаметка  '{name.title()}' успешно изменена.\n")
            print()
        elif choise == "7":
            name = del_note()
            print(f"\nЗаметка  '{name.title()}' успешно удалена.\n")
            print()
        elif choise == "8":
            print("\nДо свидания!\n")
            print()
            break
        else:
            print("\nОшибка ввода! Выберите пункт меню от 1 до 8\n")
            print()


menu_application()