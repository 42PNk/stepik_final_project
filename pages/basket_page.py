from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_be_no_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
           "Item in basket is presented, but should not be"

    def should_be_message_in_basket(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text, \
           "Message 'Your basket is empty' is not presented, but should be"
