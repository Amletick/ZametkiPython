def add_note(manager):
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    manager.add_note(title, message)
    print("Заметка успешно добавлена!")

