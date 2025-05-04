import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.registration_modal import RegistrationModal




class TestRegistrationForm:

    @pytest.mark.registration_form
    def test_user_registration_true(self, browser, url):
        
        page = MainPage(browser)
        page.open()
        page.go_to_enter_and_registration_form()

        form = RegistrationModal(browser)
        form.enter_email()
        form.enter_password()
        form.submit_account_creation()

        assert page.is_current_url_correct(), "Неверный URL после регистрации"
        assert page.is_user_avatar_displayed(),  "Имя пользователя не отображается"
        assert page.is_user_name_displayed(),  "Аватар не отображается"




