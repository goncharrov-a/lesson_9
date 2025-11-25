from pathlib import Path

from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss

FILE = Path(__file__).parent / 'resources' / 'image.png'


def test_demo_qa():
    browser.open('/automation-practice-form')

    s('#firstName').type('Luke')
    s('#lastName').type('Skywalker')
    s('#userEmail').type('example.user@mail.ru')
    s('#userNumber').type('9990003388')

    s('#dateOfBirthInput').click()
    s('.react-datepicker__month-select').click()
    ss('.react-datepicker__month-select option').element_by(have.text('January')).click()
    s('.react-datepicker__year-select').click()
    ss('.react-datepicker__year-select option').element_by(have.text('1992')).click()
    ss('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
        .element_by(have.exact_text('15')).click()

    s('//label[text()="Male"]').click()

    s('#subjectsInput').type('Ma')
    ss('.subjects-auto-complete__menu-list div').element_by(have.text('Maths')).click()
    s('#subjectsInput').type('Computer Science').press_enter()

    s('//label[text()="Sports"]').click()
    s('//label[text()="Reading"]').click()
    s('#hobbies-checkbox-3').execute_script('element.click()')

    s('#uploadPicture').send_keys(str(FILE))

    s('#currentAddress').type('Tatooine home')

    s('#state').click()
    s('#react-select-3-input').type('NCR').press_enter()
    s('#city').click()
    s('#react-select-4-input').type('Delhi').press_enter()

    s('#submit').click()

    s('.modal-content').should(be.visible)
    s('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    rows = ss('.modal-content tbody tr')

    def check(label, value):
        rows.element_by_its('td:first-child', have.exact_text(label)) \
            .element('td:nth-child(2)') \
            .should(have.text(value))

    check('Student Name', 'Luke Skywalker')
    check('Student Email', 'example.user@mail.ru')
    check('Gender', 'Male')
    check('Mobile', '9990003388')
    check('Date of Birth', '15 January,1992')
    check('Subjects', 'Maths')
    check('Subjects', 'Computer Science')
    check('Hobbies', 'Sports')
    check('Hobbies', 'Reading')
    check('Hobbies', 'Music')
    check('Picture', 'image.png')
    check('Address', 'Tatooine home')
    check('State and City', 'NCR Delhi')

    s('#closeLargeModal').click()
