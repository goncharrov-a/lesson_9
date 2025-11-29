from datetime import date
from pathlib import Path

from models.enums import Gender, Hobby
from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_high_level():
    user = User(
        first_name='Luke',
        last_name='Skywalker',
        email='example.user@mail.ru',
        mobile='9990003388',
        birthday=date(1992, 1, 15),
        gender=Gender.MALE,
        subjects=['Maths', 'Computer Science'],
        hobbies=[Hobby.SPORTS, Hobby.READING],
        picture=Path(__file__).parent / 'resources' / 'image.png',
        address='Tatooine home',
        state='NCR',
        city='Delhi',
    )

    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.register(user)
    registration_page.should_have_registered(user)
