
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setUp(browser):
    if browser=="chrome":
        ser_obj = Service("C:\\chromedriver2022\\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
        driver.maximize_window()
        print("Launching chrome browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

##############PyTest HTML Report #####################

#It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Mithilesh'

#It is hook for delete/Modify Environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata (metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
