import math
from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.driver = browser

    def add_button(self):
        button = self.browser.find_element(*ProductPageLocator.ADD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        # alert = self.browser.switch_to.alert
        # alert_text = alert.text
        # print(f"Your code: {alert_text}")
        # alert.accept()
        # except NoAlertPresentException:
        # print("No second alert presented")


    def book_path_correct(self, link):
        book_name = self.browser.find_element(*ProductPageLocator.BOOK_NAME)
        book_path = self.browser.find_element(*ProductPageLocator.BOOK_NAME_PATH)
        assert book_name.text == book_path.text, f"The Book's name not right here! {link}"

    def book_price_correct(self, link):
        book_price = self.browser.find_element(*ProductPageLocator.BOOK_PRICE)
        book_price_path = self.browser.find_element(*ProductPageLocator.BOOK_PRICE_PATH)
        assert book_price.text in book_price_path.text, f"Book's price not right here! {link}"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_disappeared(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE), \
            "Message is disappeared"