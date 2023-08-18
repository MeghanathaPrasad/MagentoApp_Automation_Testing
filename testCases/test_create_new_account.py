import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Create_New_user import CreateNewUser
from testCases import test_login
from utilities.customLogger import LogGen


class Test_002_Create_new_user:
    logger = LogGen.loggen()

    # def test_create_new_user_page(self, setup):
    #     self.logger.info("********** Test_002_Create_new_user *********")
    #     self.logger.info("********** verifying test_create_new_user_page *********")
    #     self.driver = setup
    #     self.cn = CreateNewUser(self.driver)
    #     self.driver.get("https://osc-ultimate-demo.mageplaza.com/")
    #
    #     self.cn.clickOnCreate_new_user()
    #     actual_create_new_tile = self.driver.title
    #     if actual_create_new_tile == "Home Page":
    #         self.driver.close()
    #         self.logger.info("******** create new user test page is passed ********")
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "create_new_user_page.png")
    #         self.driver.close()
    #         self.logger.info("******* Create new user page test is Failed *********")
    #         assert False
    @pytest.mark.Create_new
    def test_create_new_user(self, setup):
        self.driver = setup
        self.logger.info("********* verifying  test_Create_new_user *********** ")
        self.CN = CreateNewUser(self.driver)
        self.driver.get("https://osc-ultimate-demo.mageplaza.com/")
        self.driver.maximize_window()
        self.CN.clickOnCreate_new_user()
        self.CN.setUserFname("Ramesh4")
        self.CN.setUserLname("Srinivas4")
        self.CN.setEmail("Ramesh4@gmail.com")
        self.CN.setDob("01/01/2004")
        self.CN.setPass("Ramesh123@")
        self.CN.setConfpass("Ramesh123@")
        self.CN.clickOnRegister()
        time.sleep(5)
        # self.CN.clickOnCross()
        actual_title = self.driver.title


        try:
            registered_name = self.driver.find_element(By.XPATH, "//ul/li/span[@class='logged-in']").text
            if actual_title == "Home Page" and registered_name == "Welcome, Ramesh4 Srinivas4!":
                self.logger.info("******** new user added successfully *********")
                self.logger.info("****** Passed ******")
                assert True


        except:
            self.driver.save_screenshot(".\\Screenshots\\" + "create_new_user.png")
            self.logger.info("********* verifying new user  is failed ********")
            assert False

        self.CN.clickOnSingOut()
        self.driver.close()





