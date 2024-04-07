def show_notes(manager):
    date_filter = input("Введите дату в формате YYYY-MM-DD для фильтрации (необязательно): ")
    notes = manager.list_notes(date_filter)
    if notes:
        for note in notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Текст: {note.message}, Дата: {note.timestamp}")
    else:
        print("Заметок не найдено.")