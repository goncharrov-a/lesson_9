from datetime import date
from pathlib import Path
from models.enums import Gender, Hobby
from models.user import User


student = User(
    first_name='Luke',
    last_name='Skywalker',
    email='example.user@mail.ru',
    mobile='9990003388',
    birthday=date(1992, 1, 15),
    gender=Gender.MALE,
    subjects=['Maths', 'Computer Science'],
    hobbies=[Hobby.SPORTS, Hobby.READING],
    picture=Path(__file__).parent.parent / 'tests' / 'resources' / 'image.png',
    address='Tatooine home',
    state='NCR',
    city='Delhi',
)