from behave import given, when, then


@given('Open sign in page')
def open_login_page(context):
    context.app.terms_cond_page.open_login_page()


@when("Store original window")
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.target_app_page.click_tc_link()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_cond_page.verify_tc_url()


@then('User can close new window and switch back to original')
def close(context):
    context.app.terms_cond_page.close()