from selenium.webdriver.common.by import By

def test_addbutton(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    add_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert add_button, "Oops! No button here!"

