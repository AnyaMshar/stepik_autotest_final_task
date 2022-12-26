from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    SIGN_IN = (By.CSS_SELECTOR, "#login_form")
    SIGN_UP = (By.CSS_SELECTOR, "#register_form")
