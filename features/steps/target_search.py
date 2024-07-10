from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_cart_icon(context):
        search = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']")
        search.click()
#
@then("Verify '{message}' message is shown")
def cart_is_empty(context, message):
    #message = 'Your cart is empty'
    actual_message = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert message in actual_message, f'Expected {message} to be shown but got {actual_message}'
