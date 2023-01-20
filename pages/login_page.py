from .locators import LoginPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "Login URL is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "11aa22bb33cc"
        EMAIL_FIELD = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        EMAIL_FIELD.send_keys(email)
        PASS_FIELD = self.browser.find_element(*LoginPageLocators.PASS_FIELD)
        PASS_FIELD.send_keys(password)
        PASS_ACCEPT = self.browser.find_element(*LoginPageLocators.PASS_ACCEPT)
        PASS_ACCEPT.send_keys(password)
        REG_BUTTON = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        REG_BUTTON.click()
        
       
