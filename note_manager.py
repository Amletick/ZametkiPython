import json
import os
import datetime
from note import Note


class NoteManager:
    def __init__(self, file_name="data/notes.json"):
        self.file_name = file_name
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                notes_data = json.load(file)
                self.notes = [self._deserialize_note(note) for note in notes_data]

    def save_notes(self):
        notes_data = [self._serialize_note(note) for note in self.notes]
        with open(self.file_name, "w") as file:
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, message):
        note = Note(title, message)
        note.id = len(self.notes) + 1
        note.timestamp = str(datetime.datetime.now())
        self.notes.append(note)
        self.save_notes()

    def edit_note(self, note_id, title=None, message=None):
        for note in self.notes:
            if note.id == note_id:
                if title is not '':
                    note.title = title
                if message is not '':
                    note.message = message
                note.timestamp = str(datetime.datetime.now())
                self.save_notes()
                return True
        return False

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def list_notes(self, date_filter=None):
        if date_filter:
            notes_filtered = [note for note in self.notes if date_filter in note.timestamp]
        else:
            notes_filtered = self.notes
        return notes_filtered

    @staticmethod
    def _serialize_note(note):
        return {
            "id": note.id,
            "title": note.title,
            "message": note.message,
            "timestamp": note.timestamp
        }

    @staticmethod
    def _deserialize_note(data):
        note = Note(data["title"], data["message"])
        note.id = data["id"]
        note.timestamp = data["timestamp"]
        return note
