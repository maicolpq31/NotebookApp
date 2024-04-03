from dataclasses import dataclass
from datetime import datetime

@dataclass
class Note:

    creation_time: datetime = field(default_factory = 2024, 4, 3)



    tags: list[str] = field(default_factory = list)


    def __str__(self):
        return f"code {code} n/ creation date: {creation date} n/ title {text}"


    def add_tag(self):

        pass


    def add_note(self):
        pass


    def important_notes(self):
        pass


class NoteBook:


    def tags_note_count(self, ):




