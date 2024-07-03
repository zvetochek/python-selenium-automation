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
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(5)

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") #Amazon logo
driver.find_element(By.ID,'ap_email') #Email Field
driver.find_element(By.XPATH, "//input[@id='continue']") #Continue button
driver.find_element(By.ID, 'legalTextRow') #Conditions of use link and Privacy Notice link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']") #Need help link
driver.find_element(By.XPATH, "//span[@class='a-text-bold']") #Buying for work? (MY SIGN IN PAGE LOOKS DIFFERENT!)
driver.find_element(By.XPATH, "//a[@id='ab-sign-in-ingress-link']") #Shop on Amazon Business
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']") #Create your Amazon account


print('Test Passed')