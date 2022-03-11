from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    NAME_PRODUCT_TO_MESSAGE = (By.CSS_SELECTOR, '#messages strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_PRODUCT_TO_MESSAGE = (By.CSS_SELECTOR, '.alert-info p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
