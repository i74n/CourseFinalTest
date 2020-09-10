from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_textbox = self.browser.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email_textbox.send_keys(email)
        password_textbox = self.browser.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password_textbox.send_keys(password)
        password_repeat_textbox = self.browser.find_element(*LoginPageLocators.PASSWORD_REPEAT_TEXTBOX)
        password_repeat_textbox.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "Sign up form is not presented"
