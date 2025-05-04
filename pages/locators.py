from selenium.webdriver.common.by import By


class BasePageLocators:

    ENTER_AND_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button.buttonSecondary.inButtonText[type='button']")
    ENTER_MODAL_WINDOW = (By.XPATH, "//form[@class='popUp_shell__LuyqR' and contains(text(), 'Войти') ]")
    REGISTRATION_MODAL_WINDOW = (By.XPATH, "//form[@class='popUp_shell__LuyqR' and contains(text(), 'Зарегистрироваться')]")


class RegistrationFormLocators:
    
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Нет аккаунта')]")
    ENTER_EMAIL = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    ENTER_PASSWORD = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    ENTER_PASSWORD_REPITE = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Создать аккаунт')]")
    ALLREADY_HAVE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(), 'Уже есть аккаунт')]")


class MainPageLocators:
    PLACE_AD_BUTTON = (By.XPATH, "//button[@type='button'] and contains(text(), 'Разместить объявление')]")
    AVATAR_IMAGE = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "div.columnSmall h3.profileText.name")



