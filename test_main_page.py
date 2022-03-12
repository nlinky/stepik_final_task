import pytest

from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_basket_items()
    page.should_be_see_text_that_basket_empty()


# pytest -v --tb=line --language=en -s -m "new" test_product_page.py
# pytest -s -m "new" test_product_page.py
# pytest -v --tb=line --language=en -s -m "new" .\test_main_page.py

