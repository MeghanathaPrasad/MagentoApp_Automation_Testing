# import pytest
# from testCases.test_login import Test_001_Login
import time

import pytest
from selenium import webdriver
# from conftest import setup
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddProduct import AddProduct
from utilities.customLogger import LogGen


class Test_003_Add_Product:

    baseURL = ReadConfig.getApplictionURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.add_product
    def test_add_product(self, setup):
        self.logger.info("********** Test_003_Add_Product *********")
        self.logger.info("********* Verifying  add product *******")
        # self.driver = webdriver.Chrome()  #we repalced this with setup
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************  Logined  successfully   *******")
        self.AP = AddProduct(self.driver)
        self.driver.maximize_window()
        self.AP.clickOnCross()
        # self.AP.clickOnCross2()
        time.sleep(3)
        self.AP.clickOnCatalog()
        time.sleep(5)
        self.AP.scorllUp()
        time.sleep(3)
        self.AP.clickOnProduct()
        time.sleep(5)
        self.AP.clickOnAddProduct()
        # self.AP.clickOnCross2()
        time.sleep(3)
        self.AP.scorllUp()
        time.sleep(3)
        # self.AP.clickOnCross2()
        # self.AP.clickOnEnableProduct()
        self.AP.setAttributeSet()
        self.AP.setProductName("Latest_bag")
        self.AP.setPrice(200)
        self.AP.setProductWeight(1)
        self.AP.scorllUp()
        # self.AP.clickOnCategories()
        time.sleep(3)

        self.AP.clickOnProductAsNewFrom()
        self.AP.clickOnProductAsNewTo()
        self.AP.scorllUp()
        time.sleep(5)
        self.AP.setManufaturing()
        time.sleep(2)
        self.AP.clickOnBagActivity()
        self.AP.clickOnBagStyle()
        self.AP.clickOnBagMaterial()
        self.AP.clickOnBagHandling()
        self.AP.clickOnBagFeatures()
        self.AP.scorllUp()
        self.AP.scorllUp()
        time.sleep(3)
        self.AP.setAssingSources()
        time.sleep(6)
        self.AP.clickOnDefault()
        # self.AP.clickOnCross2()
        self.AP.clickOnDone()
        time.sleep(3)
        self.AP.setBagQuantity(100)
        self.AP.scorllUp()
        self.AP.clickOnImage()
        time.sleep(20)
        self.AP.scorllUp()
        # self.AP.setBagImage("D:\Meghu\python_hybrid_framwork\pics")
        self.AP.clickOnSave()
        time.sleep(30)
        self.AP.scorllUp()

        result = self.AP.getConfirmationMessage()

        if result == "You saved the product.":
            self.logger.info("******** Add New Product successfully *******")
            assert True
        else:
            self.logger.info("********* Add New Product Failed ***********")
            assert False

        self.driver.close()



    # def test_verify_added_product(self,setup):
    #     self.logger.info("********* Verifying  added product *******")


