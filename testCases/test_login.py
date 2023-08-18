import pytest
from selenium import webdriver
# from conftest import setup
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_001_Login:
    # baseURL = "https://osc-ultimate-demo.mageplaza.com/admin/admin/"
    # username = "mageplaza"
    # password = "demo123"

    baseURL = ReadConfig.getApplictionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.Home_page
    def test_homePageTitle(self,setup):
        # self.driver = webdriver.Chrome()   #---> by using setup fixture we are avoiding duplicates means using multiple times
        self.logger.info("************ Test_001_Login *******")
        self.logger.info("************ Verifying Home page *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        acctual_title = self.driver.title
        if acctual_title == "Magento Admin":
            self.driver.close()
            self.logger.info("************ Home page title test is passed *******")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************ Home page title test is Failed *******")
            assert False

    @pytest.mark.Login
    def test_login(self,setup):
        self.logger.info("************ Verifying Login test *******")
        # self.driver = webdriver.Chrome()  #we repalced this with setup
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.lp.clickLogout()

        if actual_title == "Dashboard / Magento Admin":
            self.driver.close()
            self.logger.info("******** Login test is passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("******* Login test is Failed *********")
            assert False

