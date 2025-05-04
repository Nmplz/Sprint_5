from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import RegistrationFormLocators, BasePageLocators
from utils.generators import generate_random_email, generate_randon_password


class RegistrationModal(BasePage):

    def go_to_no_account_menu(self):

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((RegistrationFormLocators.NO_ACCOUNT_BUTTON)))
        link = self.browser.find_element(*RegistrationFormLocators.NO_ACCOUNT_BUTTON)
        link.click()

    def enter_email(self, domain="@mail.ru"):
        email = generate_random_email(domain)

        link = self.browser.find_element(*RegistrationFormLocators.ENTER_EMAIL)
        link.send_keys(email)

    def enter_password(self):
        password = generate_randon_password()

        pwd_field = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD)
        pwd_field.send_keys(password)
        pwd_field_2 = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD_REPITE)
        pwd_field_2.send_keys(password)

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
