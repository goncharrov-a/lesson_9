from selene import browser, have
from selene.support.shared.jquery_style import ss


class LeftPanel:

    def __init__(self, app):
        self.app = app

    def open(self, category, item):
        if 'demoqa.com' not in browser.driver.current_url:
            browser.open('/')

        ss('.category-cards .card-body') \
            .element_by(have.text(category)) \
            .click()

        ss('.element-group') \
            .element_by(have.text(category)) \
            .ss('.menu-list li') \
            .element_by(have.text(item)) \
            .click()

        return self

    def open_simple_registration_form(self):
        return self.open('Elements', 'Text Box')
