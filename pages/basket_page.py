from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            'The items in the cart are displayed, but they should not be'

    def should_be_see_text_that_basket_empty(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        print(basket_empty.text)
        assert basket_empty.text == 'Your basket is empty. Continue shopping', \
            'There is no text in English that the basket is empty'

    # def should_be_basket_items(self):
    #     assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), \
    #         ''

