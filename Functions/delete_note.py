def delete_note(manager):
    note_id = int(input("Введите ID заметки для удаления: "))
    manager.delete_note(note_id)
    print("Заметка успешно удалена!")

