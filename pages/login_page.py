from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.driver = browser

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url_text = self.driver.current_url
        assert "login" in url_text.lower(), "Oops! Incorrect login URL"

    def should_be_login_form(self):
        try:
            self.driver.find_element(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False, "No login form found"

    def should_be_register_form(self):
        try:
            self.driver.find_element(*LoginPageLocators.REG_FORM)
        except NoSuchElementException:
            assert False, "No register form found"

    def register_new_user(self, email, password):
        address = self.driver.find_element(*LoginPageLocators.ADDRESS_FIELD)
        address.click()
        address.send_keys(email)
        passw1 = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        passw1.click()
        passw1.send_keys(password)
        passw2 = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD_CONFIRM)
        passw2.click()
        passw2.send_keys(password)
        self.driver.find_element(*LoginPageLocators.REG_SUBMIT).click()