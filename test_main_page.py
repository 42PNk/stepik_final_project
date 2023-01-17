from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                       # инициализируем Page Object c главной страницы, 
                                                         # передаем в конструктор экземпляр драйвера и url адрес
    
    page.open()                                          # открываем страницу
    page.go_to_login_page()                              # переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url) # инициализируем Page Object со страницей логина
                                                         # передаем в конструктор экземпляр драйвера и url адрес
    login_page.should_be_login_page()                    # выполняем проверку страницы логина
    
    
