from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        link.click()

    def add_to_basket(self, timeout=10):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((*BasePageLocators.BUTTON_ADD_T0_BASKET,)))
        link = self.browser.find_element(*BasePageLocators.BUTTON_ADD_T0_BASKET)
        link.click()

    def basket_is_empty(self, timeout=4):
        try:
            basket = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((*BasePageLocators.ITEM_IN_BASKET,)))
            assert not basket, "Basket is not empty"
            return False
        except TimeoutException:
            return True

    def empty_basket_have_text(self):
        try:
            self.browser.find_element(*BasePageLocators.EMPTY_BASKET_TEXT)
        except NoSuchElementException:
            raise AssertionError("No text about empty basket")
