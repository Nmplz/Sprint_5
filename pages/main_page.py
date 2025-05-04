from pages.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_current_url_correct(self, suffix=""):
        return self.browser.current_url == f"{self.BASE_URL}/{suffix}"

    def is_user_avatar_displayed(self):
        avatar = self.is_element_present(*MainPageLocators.AVATAR_IMAGE)
        return avatar

    def is_user_name_displayed(self):
        name = self.is_element_with_text_present(*MainPageLocators.USER_NAME, "User.")
        return name

    def click_place_ad_button(self, expect_page_reload=False):
        if expect_page_reload:
            old_button = self.browser.find_element(*MainPageLocators.PLACE_AD_BUTTON)
            WebDriverWait(self.browser, 10).until(EC.staleness_of(old_button))

        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)).click()

    def go_to_user_profile(self):

        old_button = self.browser.find_element(*MainPageLocators.AVATAR_IMAGE)
        WebDriverWait(self.browser, 10).until(EC.staleness_of(old_button))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(MainPageLocators.AVATAR_IMAGE)).click()

    def get_ad_info_by_title(self, title):
        ad_card = self.browser.find_element(By.XPATH, f"//div[@class='card'][.//h2[text()='{title}']]")
        name = ad_card.find_element(By.XPATH, ".//h2").text
        city = ad_card.find_element(By.XPATH, ".//h3").text
        price_text = ad_card.find_element(By.XPATH, ".//div[@class='price']/h2").text

        price = int(price_text.replace("₽", "").replace(" ", "").strip())

        return name, city, price
