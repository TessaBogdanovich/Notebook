notebook = {}

def add_note():
    name = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    notebook[name] = text
    print(f"Заметка {name} успешно добавлена.")
