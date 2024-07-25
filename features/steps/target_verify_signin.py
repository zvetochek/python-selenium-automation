from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target page')
# def open_target_page(context):
#     context.driver.get('https://www.target.com/')

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    # search = context.driver.find_element(By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
    # search.click()


@when('From right side navigation menu click Sign In')
def click_sign_in_nav_menu(context):
    context.app.header.click_sign_in_nav_menu()
    # search= context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    # search.click()


@then('Verify Sign In form opened')
def verify_sigin_page_url(context):
    context.app.sign_in_page.verify_sigin_page_url()
    # url = context.driver.current_url
    # expected_page = 'www.target.com/login'
    # assert expected_page in url, f'Expected {expected_page} not in {url}'