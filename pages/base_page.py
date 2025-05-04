from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .locators import BasePageLocators

class BasePage:

    BASE_URL = 'https://qa-desk.stand.praktikum-services.ru'

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url_suffix=""):
        self.driver.get(self.BASE_URL + url_suffix)

    def go_to_enter_and_registration_form(self):
        link = self.browser.find_element(*BasePageLocators.ENTER_AND_REGISTRATION_BUTTON)
        link.click()


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True    