from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        self.login_url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        assert "login" in self.login_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP), "Register form is not presented"
