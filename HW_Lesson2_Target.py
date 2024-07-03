from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

sleep(5)

driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(5)

actual_text = driver.find_element(By.XPATH,"//h1[contains(@class,'styles__StyledHeading')]").text
expected_text = 'Sign into your Target account'

assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'

#assert 'Sign into your Target account' in actual_text, f'Expected Sign into your Target account but got {actual_text}'



