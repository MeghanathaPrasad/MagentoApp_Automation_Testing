import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddProduct:
    cross_xpath = "//button[@class='navigation-close']"
    cross2_xpath = "//span[@data-id='chat_opened']/span/span"
    lnkCatalog_xpath = "//div/nav/ul/li[@id='menu-magento-catalog-catalog']"
    lnkProducts_xpath = "//div/ul/li/div/ul/li/a[.='Products']"
    # btnAddProduct_xpath = "//span[normalize-space()='Add Product']"
    btnAddProduct_xpath = "//div/button[@class='action-default primary add']"
    btnEnableProduct_xpath = "//label[@class='admin__actions-switch-label']"
    # dpdAttribute_set_xpath = "//div[.='Default']"
    # dpdAttribute_set_xpath = "//div[text()='Default']"
    # dpdAttribute_set_xpath = "//div[contains(text(),'Default')]"
    dpdAttribute_set_xpath = ".admin__action-multiselect-text[data-role='selected-option']"
    btnSelect_Bag_xpath = "//span[normalize-space()='Bag']"
    txtProdcut_name_xpath = "//div/div/input[contains(@name,'product[name]')]"
    txtProduct_Price_xpath = "//div/input[@name='product[price]']"
    txtProduct_Weight_xpath = "//div/div/input[contains(@name,'product[weight]')]"
    dpdCategories_xpath = "//div[contains(text(),'Select...')]"
    txtCategories_name_xpath = "//input[@id='GX7HAKK2']"
    btnSelect_category_xpath = "//div[@class='action-menu-item _with-checkbox _hover']//label[@class='admin__action-multiselect-label'][normalize-space()='Collections']"
    # btnClickOnOption_xpath = "//div[contains(@class,'action-menu-item _last _with-checkbox _hover')]//label[contains(@class,'admin__action-multiselect-label')]"
    btnClickOnDone_xpath = "//button[@class='action-default']//span[contains(text(),'Done')]"
    txtSet_product_new_from_date_xpath = "//div[contains(@data-index,'news_from_date')]//button[contains(@type,'button')]"
    btnGo_today_xpath = "//button[normalize-space()='Go Today']"

    btnClose_xpath = "//button[contains(text(),'Close')]"
    txtSet_product_new_to_date_xpath = "//div[contains(@data-index,'news_to_date')]//button[contains(@type,'button')]"
    btnClickOn31_xpath = "//button[normalize-space()='Go Today']"
    btnClose2_xpath ="//button[contains(text(),'Close')]"
    dpdCuntry_of_manufacturing_xpath = "//div/select[@name='product[country_of_manufacture]']"

    btnSelect_bag_activity_xpath = "//option[normalize-space()='Outdoor']"
    btnBagStyle_bags_xpath = "//option[@value='25']"
    btnBagMaterial_xpath = "//option[@value='142']"
    # btnBagColor_id = "//select[@id='B2AWYPX']"
    btnBanHandling_xpath = "//option[@value='61']"
    btnBagFeatures_xpath = "//option[@value='74']"
    btnEco_collection_xpath = "//div/input[@type='checkbox'][@id='O9P94SW']"
    btnPerformance_fabric_xpath = "//div[contains(@class,'admin__actions-switch')]//label[contains(@for,'U3SDWC7')]"
    btnNew_xpath = "//div[contains(@class,'admin__actions-switch')]//label[contains(@for,'XGXT7A6')]"
    btnSale_xpath = "//label[contains(@for,'KRAMPDM')]//span[contains(@class,'admin__actions-switch-text')]"

    btnAssingSources_xpath = "//span[normalize-space()='Assign Sources']"
    # btnSelect_default_xpath = "//input[@id='idscheckdefault']"
    btnSelect_default_xpath = "//label/input[@id='idscheckdefault']"
    # btnDone_xpath = "//body[1]/div[6]/aside[13]/div[2]/header[1]/div[1]/div[1]/div[1]/button[2]"
    btnDone_xpath = "//aside[13]/div/header/div/div/div/button[2]"
    txtQuantity_xpath = "//input[@name='sources[assigned_sources][0][quantity]']"

    # btnContent_xpath = "//strong[@class='admin__collapsible-title']//span[contains(text(),'Content')]"
    # btnImages_xpath = "//span[normalize-space()='Images And Videos']"
    btnImages_xpath = "//div[@class='entry-edit form-inline']/div[5]"
    btnUpload_image_xpath = "//input[@id='fileupload']"
    btnSave_xpath = "//span[normalize-space()='Save']"

    conf_msg_xpath = "//div[@data-ui-id='messages-message-success']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCatalog(self):
        self.driver.find_element(By.XPATH, self.lnkCatalog_xpath).click()

    def clickOnProduct(self):
        self.driver.find_element(By.XPATH, self.lnkProducts_xpath).click()

    def scorllUp(self):
        self.driver.execute_script("scrollBy(0,250);")

    def clickOnCross(self):
        self.driver.find_element(By.XPATH, self.cross_xpath).click()

    def clickOnCross2(self):

        element = self.driver.find_element(By.XPATH, self.cross2_xpath)
        self.driver.execute_script("arguments[0].click();", element)

    def clickOnAddProduct(self):
        self.driver.find_element(By.XPATH, self.btnAddProduct_xpath).click()

    def clickOnEnableProduct(self):
        self.driver.find_element(By.XPATH, self.btnEnableProduct_xpath).click()

    def setAttributeSet(self):
        self.driver.find_element(By.CSS_SELECTOR, self.dpdAttribute_set_xpath).click()
        self.driver.find_element(By.XPATH, self.btnSelect_Bag_xpath).click()

    def setProductName(self,pname):
        self.driver.find_element(By.XPATH, self.txtProdcut_name_xpath).send_keys(pname)

    def setPrice(self,price):
        self.driver.find_element(By.XPATH, self.txtProduct_Price_xpath).send_keys(price)

    def setProductWeight(self,pweight):
        self.driver.find_element(By.XPATH, self.txtProduct_Weight_xpath).send_keys(pweight)

    def clickOnCategories(self):
        self.driver.find_element(By.XPATH, self.dpdCategories_xpath).click()

    # def setCategoriesName(self,categoryName):
    #     self.driver.find_element(By.XPATH, self.txtCategories_name_xpath).clear()
    #     self.driver.find_element(By.XPATH, self.txtCategories_name_xpath).click()
    #     self.driver.find_element(By.XPATH, self.txtCategories_name_xpath).send_keys(categoryName)
    #     self.driver.find_element(By.XPATH, self.btnClickOnOption_xpath).click()

    def clickonSelectCatergory(self):
        self.driver.find_element(By.XPATH, self.btnSelect_category_xpath).click()

    def clickOnDone(self):
        self.driver.find_element(By.XPATH, self.btnClickOnDone_xpath).click()

    def clickOnProductAsNewFrom(self):
        self.driver.find_element(By.XPATH, self.txtSet_product_new_from_date_xpath).click()
        self.driver.find_element(By.XPATH, self.btnGo_today_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClose_xpath).click()

    def clickOnProductAsNewTo(self):
        self.driver.find_element(By.XPATH, self.txtSet_product_new_to_date_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClickOn31_xpath).click()
        self.driver.find_element(By.XPATH, self.btnClose2_xpath).click()


    def setManufaturing(self):
        self.driver.find_element(By.XPATH,self.dpdCuntry_of_manufacturing_xpath).click()
        dropdown = Select(self.driver.find_element(By.XPATH, self.dpdCuntry_of_manufacturing_xpath))
        dropdown.select_by_visible_text("India")

    def clickOnBagActivity(self):
        self.driver.find_element(By.XPATH, self.btnSelect_bag_activity_xpath).click()

    def clickOnBagStyle(self):
        self.driver.find_element(By.XPATH, self.btnBagStyle_bags_xpath).click()

    def clickOnBagMaterial(self):
        self.driver.find_element(By.XPATH, self.btnBagMaterial_xpath).click()

    def clickOnBagHandling(self):
        self.driver.find_element(By.XPATH, self.btnBanHandling_xpath).click()

    def clickOnBagFeatures(self):
        self.driver.find_element(By.XPATH, self.btnBagFeatures_xpath)

    def clickOnBagEcoCollection(self):
        self.driver.find_element(By.XPATH, self.btnEco_collection_xpath).click()

    def clickOnPerformanceFabric(self):
        self.driver.find_element(By.XPATH, self.btnPerformance_fabric_xpath)

    def clickOnBagNewType(self):
        self.driver.find_element(By.XPATH, self.btnNew_xpath).click()

    def clickOnBagSale(self):
        self.driver.find_element(By.XPATH, self.btnSale_xpath).click()

    def setAssingSources(self):
        self.driver.find_element(By.XPATH, self.btnAssingSources_xpath).click()

    def clickOnDefault(self):
        self.driver.find_element(By.XPATH, self.btnSelect_default_xpath).click()

    def clickOnDone(self):
        self.driver.find_element(By.XPATH, self.btnDone_xpath).click()

    def setBagQuantity(self,quantity):
        self.driver.find_element(By.XPATH, self.txtQuantity_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtQuantity_xpath).click()
        self.driver.find_element(By.XPATH, self.txtQuantity_xpath).send_keys(quantity)

    def clickOnImage(self):
        self.driver.find_element(By.XPATH, self.btnImages_xpath).click()


    def setBagImage(self,path):
        file_input = self.driver.find_element(By.XPATH, self.btnImages_xpath)
        file_input.send_keys(path)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()


    def getConfirmationMessage(self):
        return self.driver.find_element(By.XPATH,self.conf_msg_xpath).text