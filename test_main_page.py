from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = BasePage(browser, link)                        # инициализируем Page Object c главной страницы, 
                                                                   # передаем в конструктор экземпляр драйвера и url адрес
     
        self.page.open()                                           # открываем страницу
        self.page.go_to_login_page()                               # переходим на страницу логина
        self.login_page = LoginPage(browser, browser.current_url)  # инициализируем Page Object со страницей логина
                                                                   # передаем в конструктор экземпляр драйвера и url адрес
        self.login_page.should_be_login_page()                     # выполняем проверку страницы логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = BasePage(browser, link)
        self.page.open()
        self.page.should_be_login_link()        
    

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_item_in_basket()
    basket_page.should_be_message_in_basket()
