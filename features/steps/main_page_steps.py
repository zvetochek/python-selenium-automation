from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_product(context, product):
        # find search field and enter text
        context.driver.find_element(By.ID, 'search').send_keys(product)
        # click search
        context.driver.find_element(By. XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
        # wait for the page with search results to load
        sleep(6)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']")

