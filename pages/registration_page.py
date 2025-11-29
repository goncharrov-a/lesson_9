from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user):
        s('#firstName').type(user.first_name)
        s('#lastName').type(user.last_name)

        s('#userEmail').type(user.email)
        s('#userNumber').type(user.mobile)

        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click()
        ss('.react-datepicker__month-select option').element_by(
            have.text(user.birthday.strftime('%B'))
        ).click()

        s('.react-datepicker__year-select').click()
        ss('.react-datepicker__year-select option').element_by(
            have.text(str(user.birthday.year))
        ).click()

        ss('.react-datepicker__day:not(.react-datepicker__day--outside-month)') \
            .element_by(have.exact_text(str(user.birthday.day))).click()

        s(f'//label[text()="{user.gender.value}"]').click()

        for subject in user.subjects:
            s('#subjectsInput').type(subject).press_enter()

        for hobby in user.hobbies:
            s(f'//label[text()="{hobby.value}"]').click()

        s('#uploadPicture').send_keys(str(user.picture))

        s('#currentAddress').type(user.address)

        s('#state').click()
        s('#react-select-3-input').type(user.state).press_enter()
        s('#city').click()
        s('#react-select-4-input').type(user.city).press_enter()

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        s('#submit').should(be.enabled).click()

        return self

    def should_have_registered(self, user):
        s('.modal-content').should(be.visible)
        s('#example-modal-sizes-title-lg').should(
            have.text('Thanks for submitting the form')
        )

        rows = ss('.modal-content tbody tr')

        def check(label, value):
            rows.element_by_its('td:first-child', have.exact_text(label)) \
                .element('td:nth-child(2)') \
                .should(have.text(value))

        check('Student Name', user.full_name)
        check('Student Email', user.email)
        check('Gender', user.gender.value)
        check('Mobile', user.mobile)
        check('Date of Birth', user.birthday.strftime('%d %B,%Y'))

        for subject in user.subjects:
            check('Subjects', subject)

        for hobby in user.hobbies:
            check('Hobbies', hobby.value)

        check('Picture', user.picture.name)
        check('Address', user.address)
        check('State and City', f'{user.state} {user.city}')

        return self
