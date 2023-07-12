notebook = {}

def add_note():
    name = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    notebook[name] = text
    print(f"Заметка {name} успешно добавлена.")

def edit_note():
    name = input("Введите название заметки, которую хотите отредактировать: ")
    if name in notebook:
       text = input("Введите новый текст: ")
       notebook[name] = text
    print(f"Текст {name} успешно изменен.")

def delete_note():
    name = input("Введите название заметки, которую хотите удалить: ")
    if name in notebook:
        del notebook[name]
        print(f"Заметка {name} успешно удалена.")
    else:
        print(f"Заметка {name} не найдена в справочнике.")

def print_notes():
    if notebook:
        print("Список заметок:")
        for name, text in notebook.items():
            print(f"{name}: {text}")
    else:
        print("Справочник пуст.")
def main():
    while True:
        print("Меню:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Список всех заметок")
        print("5. Выйти")
        choice = input("Введите номер действия: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            edit_note()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print_notes()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == '__main__':
    main()