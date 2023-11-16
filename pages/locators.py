from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADDRESS_LINK = (By.ID, "id_login-username")
    PASSWORD_LINK = (By.ID, "id_login-password")
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    ADDRESS_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    PASSWORD_FIELD_CONFIRM = (By.ID, "id_registration-password2")
    REG_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocator:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1")
    BOOK_NAME_PATH = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    BOOK_PRICE_PATH = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, ".btn-group > a")
    ITEM_IN_BASKET = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BUTTON_ADD_T0_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")