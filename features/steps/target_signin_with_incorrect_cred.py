from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open target page')
# def open_target_page(context):
#     context.app.main_page.open_target()


# @when('Click Sign In header')
# def click_sign_in(context):
#     context.app.header.click_signin_header_btn()


# @when('From right side navigation menu click Sign In')
# def click_sign_in_nav_menu(context):
#     context.app.header.click_sign_in_nav_menu()


@when('Input incorrect email and password on Signin page')
def input_incorrect_credentials(context):
    context.app.sign_in_page.input_incorrect_credentials()


# @when('Click Sign In button')
# def click_signin_btn(context):
#     context.app.sign_in_page.click_signin_btn()


@then("Verify 'Please enter a valid email or phone number' message is shown")
# Please enter a valid email or phone number
# Please enter a valid password
def verify_error_message_is_shown(context):
    context.app.sign_in_page.verify_error_message_is_shown()