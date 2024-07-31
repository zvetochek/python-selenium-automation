from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):

    INPUT_EMAIL = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    SIGNIN_BTN = (By.ID, "login")
    USER_NAME_ERROR_MESSAGE = (By.ID, "username--ErrorMessage")
    PASSWORD_ERROR_MESSAGE = (By.ID, "password--ErrorMessage")


    def verify_sigin_page_url(self):
        self.verify_partial_url('www.target.com/login')
        # url = self.driver.current_url
        # expected_page = 'www.target.com/login'
        # assert expected_page in url, f'Expected {expected_page} not in {url}'

    def input_email_and_password(self):
        sleep(5)
        self.input_text('rozencrantz@wotomail.com', *self.INPUT_EMAIL)
        self.input_text('Wewanttowin1', *self.INPUT_PASSWORD)


    def input_incorrect_credentials(self):
        self.input_text('hhhhhh333333', *self.INPUT_EMAIL)
        self.input_text('iuhhkljlk45', *self.INPUT_PASSWORD)

    def click_signin_btn(self):
        self.click(*self.SIGNIN_BTN)

    def verify_user_logged_in(self):
        self.verify_partial_url('https://www.target.com/')

    def verify_error_message_is_shown(self):
        expected_error_message = 'Please enter a valid email or phone number'
        username_error = self.find_element(*self.USER_NAME_ERROR_MESSAGE).text
        #password_error = self.find_element(*self.PASSWORD_ERROR_MESSAGE).text
        assert expected_error_message == username_error, f'Expected {expected_error_message} but got {username_error}'
        #Password error message is not shown, I just used email as verification

    def input_incorrect_password(self):
        self.input_text('iuhhkljlk45', *self.INPUT_PASSWORD)


