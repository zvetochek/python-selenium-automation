from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

# @when('Search for {product}')
# def search_product(context, product):
#     # find search field and enter text
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # click search
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     # wait for the page with search results to load


@when('Click on product picture')
def click_on_selected_product(context):
    context.app.cart_page.click_on_selected_product()
    # sleep(5) # the code will not work w/o sleep command
    # context.driver.find_element(By.CSS_SELECTOR, 'picture[data-test="@web/ProductCard/ProductCardImage/primary"]').click()



@when("Click on the button 'Add to cart'")
def click_on_small_button_add_to_cart(context):
    context.app.cart_page.click_on_small_button_add_to_cart()
    # sleep(4) # the code will not work w/o sleep command
    # context.driver.execute_script("window.scrollBy(0, 1100)")
    # sleep(3) # the code will not work w/o sleep command
    # context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/AddToCart/FulfillmentSection'] button[id*='addToCartButtonOrTextId']").click()



# @when("Click on the large button 'Add to cart'")
# def click_on_large_button_add_to_cart(context):
#     context.app.cart_page.click_on_large_button_add_to_cart()
#     # context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()


@when("Click on 'View cart & check out button'")
def click_on_view_cart(context):
    context.app.cart_page.click_on_view_cart()
    # context.driver.find_element(By. CSS_SELECTOR, "[href='/cart']").click()


@then('Verify if one item is added in the cart')
def verify_item_added(context):
    context.app.cart_page.verify_item_added()
    # expected_no_of_item = '1 item'
    # actual_no_of_item = context.driver.find_element(By.CSS_SELECTOR, ".h-margin-b-tight, h-text-grayDark").text
    # assert expected_no_of_item in actual_no_of_item, f'Expected {expected_no_of_item}, but got {actual_no_of_item}'










