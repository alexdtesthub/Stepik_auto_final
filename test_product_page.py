import faker
import pytest

from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


# Гость (промо) поиск бага в списке страниц:
@pytest.mark.need_review
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])
def test_guest_can_add_product_to_basket(browser):
    pages = ProductPage(browser, link_promo)
    pages.open()
    pages.add_button()
    pages.solve_quiz_and_get_code()
    pages.book_path_correct(link_promo)
    pages.book_price_correct(link_promo)


# Гость (промо) отрицательные проверки корзины:
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    pages = ProductPage(browser, link_promo)
    pages.open()
    pages.add_button()
    pages.solve_quiz_and_get_code()
    pages.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    pages = ProductPage(browser, link_promo)
    pages.open()
    pages.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    pages = ProductPage(browser, link_promo)
    pages.open()
    pages.add_button()
    pages.solve_quiz_and_get_code()
    pages.should_not_disappeared()


# Гость на странице продукта и корзины:
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    pages = ProductPage(browser, link)
    pages.open()
    pages.go_to_login_page()
    pages.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    basket = BasketPage(browser, link)
    basket.open()
    basket.go_to_basket_page()
    basket.basket_is_empty()
    basket.empty_basket_have_text()


# Зарегистрированный пользователь на странице продукта и корзины:
@pytest.mark.setup_test
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        pages = LoginPage(browser, link)
        pages.open()
        pages.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password = f.password() + str(1234567890)
        pages.register_new_user(email, password)
        pages.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        pages = ProductPage(browser, link_product)
        pages.open()
        pages.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        pages = ProductPage(browser, link_product)
        pages.open()
        pages.add_button()
        pages.book_path_correct(link_product)
        pages.book_price_correct(link_product)
