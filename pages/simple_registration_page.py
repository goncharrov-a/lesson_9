from selene import browser, have


class SimpleRegistrationPage:

    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.submit_btn = browser.element('#submit')
        self.result = browser.element('#output')

    def open(self):
        browser.open('/text-box')
        return self

    def register(self, user):
        self.full_name.type(user.full_name)
        self.email.type(user.email)
        self.current_address.type(user.current_address)
        self.permanent_address.type(user.permanent_address)
        self.submit_btn.click()
        return self

    def should_have_registered(self, user):
        self.result.should(
            have.text(f"Name:{user.full_name}")
            .and_(have.text(f"Email:{user.email}"))
            .and_(have.text(f"Current Address :{user.current_address}"))
            .and_(have.text(f"Permananet Address :{user.permanent_address}"))
        )
        return self
