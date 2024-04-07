from note_manager import NoteManager
from Functions.add_note import add_note;
from Functions.delete_note import delete_note;
from Functions.edit_note import edit_note;
from Functions.show_notes import show_notes;

def main():
    manager = NoteManager()

    while True:
        print("Выберите действие:")
        print("1. Добавить заметку")
        print("2. Редактировать заметку")
        print("3. Удалить заметку")
        print("4. Показать список заметок")
        print("5. Выйти из программы")

        choice = input("> ")

        if choice == "1":
            add_note(manager)
        elif choice == "2":
            edit_note(manager)
        elif choice == "3":
            delete_note(manager)
        elif choice == "4":
            show_notes(manager)
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()
