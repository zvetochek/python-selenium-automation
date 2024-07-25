from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@when('Click on Cart icon')
def click_cart(context):
        context.app.header.click_cart() # connecting to the page object, instead of working with Selenium directly
        # the name of the page object is 'header', click_cart is the name of the method that was just implemented

@then("Verify 'Your cart is empty' message is shown") # the message is shown inside the cart page, so we use cart_page here
def verify_cart_empty(context):
        context.app.cart_page.verify_cart_empty()

# Lana's code in class'
# @then ("Verify 'Your cart is empty' message is shown")
# def verify_cart_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] hi").text
#     assert expected_text == actual_text, f'Expected {expected_text} did not match actual {actual_text}'
