from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import RegistrationFormLocators, BasePageLocators
from utils.generators import generate_random_email, generate_randon_password


class RegistrationModal(BasePage):

    def go_to_no_account_menu(self):

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((RegistrationFormLocators.NO_ACCOUNT_BUTTON))).click()  #ПРОВЕРИТЬ !!!
        

    def enter_new_user_email(self, domain: str = "@mail.ru"):
        email = generate_random_email(domain)
        link = self.browser.find_element(*RegistrationFormLocators.ENTER_EMAIL)
        link.send_keys(email)

    def enter_existing_email(self, email):
        link = self.browser.find_element(*RegistrationFormLocators.ENTER_EMAIL)
        link.send_keys(email)

    def enter_new_user_password(self):
        password = generate_randon_password()

        pwd_field = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD)
        pwd_field.send_keys(password)
        pwd_field_2 = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD_REPITE)
        pwd_field_2.send_keys(password)

    def enter_existing_user_password(self, password):
        pwd_field = self.browser.find_element(*RegistrationFormLocators.ENTER_PASSWORD)
        pwd_field.send_keys(password)

    def submit_account_creation(self):
        link = self.browser.find_element(*RegistrationFormLocators.CREATE_ACCOUNT_BUTTON).click()

    def is_email_error_displayed(self):
        error_text = self.browser.find_element(*RegistrationFormLocators.ERROR_MESSAGE)
        return error_text.is_displayed()

    def is_errored_fields_highlighted_red(self):
        wrapper = self.browser.find_element(*RegistrationFormLocators.ERROR_RED_BOX)
        return wrapper.value_of_css_property("border-color")

    def is_modal_with_warring_displayed(self):
        result = self.is_element_with_text_present(*BasePageLocators.WARNING_AUTHORISATION_MODAL_WINDOW, "Чтобы разместить объявление, авторизуйтесь")
        return result

    def submit_login_form_button(self):
        self.browser.find_element(*RegistrationFormLocators.LOGIN_FORM_ENTER_BUTTON).click()

    def submit_logout_button(self):
        self.browser.find_element(*RegistrationFormLocators.LOGIN_FORM_LOGOUT_BUTTON).click()
