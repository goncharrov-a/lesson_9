from app.application_manager import app
from models.users import student


def test_simple_registration():
    app.left_panel.open_simple_registration_form()
    (
        app.simple_registration
        .open()
        .register(student)
        .should_have_registered(student)
    )
