from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser =='chrome':
        driver = webdriver.Chrome()       #this is for multiple browsers
        driver.implicitly_wait(20)
        print("Launching  Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(20)

        print("Launching Firefox browser")
    else:
        driver = webdriver.Edge()
        driver.implicitly_wait(20)

        print("Launching Edge browser")
    return driver

def pytest_addoption(parser): #this will get the value from CLI/ hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to setup method
    return request.config.getoption("--browser")


################# pytest HTML report##############
#
# # It is hook for Adding Environment info to HTML report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'magentoApp'
#     config._metadata['Module Name'] = 'Catalogs'
#     config._metadata['Tester'] = 'Meghanath'
#
#
# # It is hook for delete/modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)  # Java home is displyed defaultly soo we making it NONE
#     metadata.pop("plugins", None)