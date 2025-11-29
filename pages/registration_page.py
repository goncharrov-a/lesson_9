from pathlib import Path

from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        s('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        s('#lastName').type(value)
        return self

    def fill_email(self, value):
        s('#userEmail').type(value)
        return self

    def fill_mobile(self, value):
        s('#userNumber').type(value)
        return self

    def set_birthday(self, day, month, year):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click()
        ss('.react-datepicker__month-select option').element_by(have.text(month)).click()

        s('.react-datepicker__year-select').click()
        ss('.react-datepicker__year-select option').element_by(have.text(str(year))).click()

        ss('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
            .element_by(have.exact_text(str(day))).click()
        return self

    def select_gender(self, gender):
        s(f'//label[text()="{gender}"]').click()
        return self

    def add_subject(self, subject):
        s('#subjectsInput').type(subject).press_enter()
        return self

    def select_hobby(self, hobby):
        s(f'//label[text()="{hobby}"]').click()
        return self

    def upload_picture(self, path: Path):
        s('#uploadPicture').send_keys(str(path))
        return self

    def fill_address(self, value):
        s('#currentAddress').type(value)
        return self

    def select_state(self, value):
        s('#state').click()
        s('#react-select-3-input').type(value).press_enter()
        return self

    def select_city(self, value):
        s('#city').click()
        s('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        s('#submit').click()
        return self

    def should_have_registered(self, **expected):
        s('.modal-content').should(be.visible)
        s('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        rows = ss('.modal-content tbody tr')

        def check(label, value):
            rows.element_by_its('td:first-child', have.exact_text(label)) \
                .element('td:nth-child(2)') \
                .should(have.text(value))

        for label, value in expected.items():
            check(label, value)

        return self
