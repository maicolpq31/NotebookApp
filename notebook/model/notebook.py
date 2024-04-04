from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    code: int
    title: str
    text: str
    #creation_date: datetime = field(default_factory=datetime.now)
    importance: str
    tags: list[str] = field(default_factory=list)

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)


    def __str__(self) -> str:
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def __init__(self):
        self.notes: dict[int, Note] = {}


    def add_note(self, title: str, text: str, importance: str) -> int:
        code = len(self.notes) + 1
        self.notes[code] = Note(code=code, title=title, text=text, importance=importance)
        return code

    def important_notes(self) -> list[Note]:
        important = []
        for note in self.notes.values():
            if note.importance.upper() in [Note.HIGH, Note.MEDIUM]:
                important.append(note)
        return important


    def tags_note_count(self) -> dict[str, int]:
        tag_count: dict[str, int] = {}
        for note in self.notes.values():
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count