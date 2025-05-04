from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    def is_current_url_correct(self):
        return self.driver.current_url == f"{self.BASE_URL}/login"


    def is_user_avatar_displayed(self):
        avatar = self.is_element_present(*MainPageLocators.AVATAR_IMAGE)
        return avatar

    def is_user_name_displayed(self):
        name = self.is_element_with_text_present(*MainPageLocators.USER_NAME)
        return name
