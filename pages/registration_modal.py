from base_page import BasePage
from locators import RegistrationFormLocators
from utils import generate_random_email, generate_randon_password


class RegistrationModal(BasePage):

    def go_to_no_account_menu(self):

        link = self.browser.find_element(*RegistrationFormLocators.NO_ACCOUNT_BUTTON)
        link.click()

    def enter_email(self, domain="@mail.ru"):
        email = generate_random_email(domain)

        link = self.browser.find_element(*RegistrationFormLocators.ENTER_EMAIL).click()
        link.send_keys(email)

    def enter_password(self):
        password = generate_randon_password()

        link = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD).click()
        link.send_keys(password)
        link = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD_REPITE).click()
        link.send_keys(password)

    def submit_account_creation(self):

        link = self.browser.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()



    """
Регистрация пользователя
Что нужно сделать:
Нажать кнопку «Вход и регистрация».
Нажать кнопку «Нет аккаунта».
Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
"""
