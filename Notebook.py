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