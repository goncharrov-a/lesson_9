from app.left_panel import LeftPanel
from pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.left_panel = LeftPanel(self)
        self.simple_registration = SimpleRegistrationPage()


app = ApplicationManager()