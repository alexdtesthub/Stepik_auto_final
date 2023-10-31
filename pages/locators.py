from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGINP_LINK = (By.CSS_SELECTOR, "#login_link")
    ADRESS_LINK = (By.ID, "id_login-username")
    PASSWORD_LINK = (By.ID, "id_login-password")
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")