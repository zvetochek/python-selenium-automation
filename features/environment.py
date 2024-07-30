from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # these 3 lines 16 to 18 needed for GOOGLE CHROME
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari()

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/19-python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ### SAFARI ### does not require ANY additional steps, just this line!!!
    # context.driver = webdriver.Safari()

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'larisa_t3lePz'
    # bs_key = 'MNfpB7RR7gXKZXYPLsyp'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion" : "11",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    #
    # # for Mac: "os": "OS X", "osVersion" : "ventura", 'browserName': 'chrome' 'sessionName': scenario_name
    #
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
