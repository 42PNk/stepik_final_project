from .locators import ProducttLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def product_add_to_basket(self):
        add_product = self.browser.find_element(*ProducttLocators.ADD_BASKET)
        add_product.click()

    def should_be_name_in_basket_equal_product(self):
        product_name = self.browser.find_element(*ProducttLocators.PRODUCT_NAME).text
        basket_name = self.browser.find_element(*ProducttLocators.BASKET_NAME).text
        print (f"{basket_name} add in basket!")
        assert product_name == basket_name, "Names are not equal"
       
    def should_be_price_in_basket_equal_product(self):
        product_price = self.browser.find_element(*ProducttLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProducttLocators.BASKET_PRICE).text
        print(f"Basket price is {basket_price}")
        assert product_price == basket_price, "prices are not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProducttLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProducttLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"
