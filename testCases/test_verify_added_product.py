import time

import pytest
from selenium import webdriver
# from conftest import setup
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddProduct import AddProduct
from pageObjects.VerifyAddedProduct import VerifyAddedProduct
from utilities.customLogger import LogGen


class Test_004_Verify_Added_Product:

    baseURL2 = ReadConfig.getApplicationURL2()
    # username = ReadConfig.getUseremail()
    # password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.added_product
    def test_verify_added_product(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL2)
        self.driver.maximize_window()
        self.sp = VerifyAddedProduct(self.driver)
        time.sleep(5)
        self.sp.clickOnCross()
        self.sp.setSearchtxt("Latest_bag")
        time.sleep(5)
        self.sp.clickOnSearch()
        time.sleep(5)
        self.sp.scorllUp()
        time.sleep(5)
        # FoundResults = self.sp.getSearchResults()
        # if FoundResults == "ramesh_bah":
        #     assert True
        # else:
        #     assert False
        #

        try:
            FoundResults = self.sp.getSearchResults()
            if FoundResults == "Latest_bag":
                self.logger.info("********* product added verifyed successfully ******")
                assert True
            else:
                raise Exception
        except:
            self.logger.info("********* verifying added product is failed ********")
            assert False

        self.driver.close()





