from dataclasses import dataclass
from datetime import date
from pathlib import Path

from models.enums import Gender, Hobby


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    birthday: date
    gender: Gender
    subjects: list[str]
    hobbies: list[Hobby]
    picture: Path
    address: str
    state: str
    city: str

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'