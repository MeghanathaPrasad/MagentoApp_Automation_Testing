import time
from selenium.webdriver.common.by import By

class VerifyAddedProduct:
    cross_xpath = "//button[@title='Close navigation']"
    txtSearchButton_xpath = "//div/form/div/div/input[@id='search']"
    msgSearchResult_xpath = "//div[@class='message notice']"
    btnSearch_xpath = "//button[@title='Search']"
    msgResultstxt_xpath = "//div[@class='product details product-item-details']/strong/a"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCross(self):
        self.driver.find_element(By.XPATH, self.cross_xpath).click()

    def clickOnSearch(self):
        self.driver.find_element(By.XPATH, self.txtSearchButton_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchButton_xpath).click()

    def setSearchtxt(self,searchItem):
        self.driver.find_element(By.XPATH, self.txtSearchButton_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtSearchButton_xpath).send_keys(searchItem)


    def clickOnSearch(self):
        ele = self.driver.find_element(By.XPATH, self.btnSearch_xpath)
        self.driver.execute_script("arguments[0].click();", ele)

    def getConfirmationMessage(self):
        return self.driver.find_element(By.XPATH,self.msgSearchResult_xpath).text

    def scorllUp(self):
        self.driver.execute_script("scrollBy(0,250);")

    def getSearchResults(self):
        return self.driver.find_element(By.XPATH, self.msgResultstxt_xpath).text