from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

from pages.base_page import Page

class Header(Page):
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By. XPATH, "//button[@data-test='@web/Search/SearchButton']")
    SIGN_IN_ICON = (By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
    SIGN_NAV_MANU = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    SIGN_IN_HEADER_BTN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')


    def search_product(self, product): # this function expects the argument to be passed, makes it dynamic
        print('POM layer:', product)
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def click_cart(self):
        self.wait_and_click(*self.CART_BTN)
        # self.click(*self.CART_BTN) # b/c this locator is inside the class, we can access it using 'self'


    def click_sign_in_nav_menu(self):
        self.wait_and_click(*self.SIGN_NAV_MANU)


    def click_signin_header_btn(self):
        self.wait_and_click(*self.SIGN_IN_HEADER_BTN)


