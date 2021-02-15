import pytest
from selenium import webdriver
import os
from sys import platform



@pytest.fixture()
def setup(browser):
    global driver
    capabilities = {'browserName': 'chrome',
                    "chromeOptions": {
                        'binary': "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    }
                    }

    if browser == 'chrome':
        if platform == "win32":
            driver = webdriver.Chrome(executable_path="." + os.sep + "browsers" + os.sep + "chromedriver.exe",
                                      desired_capabilities=capabilities)
            print("Launching chrome browser in Windows.........")
        elif platform == "darwin":
            driver = webdriver.Chrome(executable_path="." + os.sep + "browsers" + os.sep + "chromedriver")
            print("Launching chrome driver in Mac")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

def teardown():
    driver.quit()


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Sennder QA Assignment'
    config._metadata['Module Name'] = 'Sprint boards'
    config._metadata['Tester'] = 'Saurabh'

