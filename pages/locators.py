from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADDRESS_LINK = (By.ID, "id_login-username")
    PASSWORD_LINK = (By.ID, "id_login-password")
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")

class ProductPageLocator:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    BOOK_NAME_PATH = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    BOOK_PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    BOOK_PRICE_PATH = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, "/html/body/header/div[1]/div/div[2]/span/a")
    ITEM_IN_BASKET = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
    BUTTON_ADD_T0_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")