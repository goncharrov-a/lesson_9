from pathlib import Path

from pages.registration_page import RegistrationPage

FILE = Path(__file__).parent / 'resources' / 'image.png'


def test_registration_form():
    page = RegistrationPage()

    (
        page.open()
        .fill_first_name('Luke')
        .fill_last_name('Skywalker')
        .fill_email('example.user@mail.ru')
        .fill_mobile('9990003388')
        .set_birthday(15, 'January', 1992)
        .select_gender('Male')
        .add_subject('Maths')
        .add_subject('Computer Science')
        .select_hobby('Sports')
        .select_hobby('Reading')
        .upload_picture(FILE)
        .fill_address('Tatooine home')
        .select_state('NCR')
        .select_city('Delhi')
        .submit()
    )

    page.should_have_registered(
        **{
            'Student Name': 'Luke Skywalker',
            'Student Email': 'example.user@mail.ru',
            'Gender': 'Male',
            'Mobile': '9990003388',
            'Date of Birth': '15 January,1992',
            'Subjects': 'Computer Science',
            'Hobbies': 'Reading',
            'Picture': 'image.png',
            'Address': 'Tatooine home',
            'State and City': 'NCR Delhi',
        }
    )
