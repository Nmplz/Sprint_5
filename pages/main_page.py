from pages.locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_current_url_correct(self):
        return self.browser.current_url == f"{self.BASE_URL}/regiatration"

    def is_user_avatar_displayed(self):
        avatar = self.is_element_present(*MainPageLocators.AVATAR_IMAGE)
        return avatar

    def is_user_name_displayed(self):
        name = self.is_element_with_text_present(*MainPageLocators.USER_NAME, "User.")
        return name
