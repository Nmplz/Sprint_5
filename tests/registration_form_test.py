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
        page = RegistrationModal(browser)
        page.enter_email()
        page.enter_password()
        page.submit_account_creation()
        assert #TODO 







"""
Регистрация пользователя
Что нужно сделать:
Нажать кнопку «Вход и регистрация».
Нажать кнопку «Нет аккаунта».
Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
"""
