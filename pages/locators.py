from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_ACCEPT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProducttLocators():
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")

