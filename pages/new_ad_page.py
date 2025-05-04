from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import NewAdvertisementPageLocators
from utils.generators import generate_unique_title


class NewAdvertisementPage(BasePage):

    def fill_product_name_form(self):

        name = generate_unique_title("ProductUniqueName")

        link = self.browser.find_element(*NewAdvertisementPageLocators.PRODUCT_NAME_FIELD)
        link.send_keys(name)
        return name

    def fill_product_disc_form(self):

        disc = generate_unique_title("ProductUniqueDiscription")
        link = self.browser.find_element(*NewAdvertisementPageLocators.PRODUCT_DISCRIPTION_FIELD)
        link.send_keys(disc)
        return disc

    def fill_product_price(self):

        price = 100500
        link = self.browser.find_element(*NewAdvertisementPageLocators.PRODUCT_PRICE_FIELD)
        link.send_keys(price)
        return price

    def set_product_category(self):
        
        category_dropdown =self.browser.find_element(*NewAdvertisementPageLocators.CATEGORY_DROP_DOWN_MENU).click()
        set_tech_category =self.browser.find_element(*NewAdvertisementPageLocators.CATEGORY_DROP_DOWN_MENU_TECHNOLOGY).click()

    def set_product_city(self):
        city_dropdown =self.browser.find_element(*NewAdvertisementPageLocators.CITY_DROPDOWN_MENU).click()
        set_city_kazan  = self.browser.find_element(*NewAdvertisementPageLocators.CITY_DROPDOWN_MENU_KAZAN).click()
        return f'Казань'

    def set_product_condition_to_used (self):
        self.browser.find_element(*NewAdvertisementPageLocators.PRODUCT_CONDITION_USED_RADIO).click()

    
    def click_submit_button(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(NewAdvertisementPageLocators.SUBMIT_BUTTON)).click()





"""
Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
Выбрать из Dropdown «Категорию» и «Город».
Выбрать RabioButton «Состояние товара».
Нажать кнопку «Опубликовать».
Перейти в профиль пользователя.
Проверить: в блоке «Мои объявления» отображается созданное объявление.
"""
