from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime


@dataclass
class Note:
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    code: int
    title: str
    text: str
    #creation_time: datetime = field(default_factory= datetime.now)
    importance: str
    tags: List[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        if tag not in self.tags:
            self.tags.append(tag)

    def _str_(self) -> str:
        return f"Code: {self.code}\nCreation date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:
    def _init_(self):
        self.notes: List[Note] = []
        self.next_code: int = 1

    def add_note(self, title: str, text: str, importance: str) -> int:
        note = Note(code=self.next_code, title=title, text=text, importance=importance)
        self.notes.append(note)
        self.next_code += 1
        return note.code

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes if note.importance in (Note.HIGH, Note.MEDIUM)]

    def tags_note_count(self) -> Dict[str, int]:
        tag_count: Dict[str, int] = {}
        for note in self.notes:
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1
        return tag_count