import time

from selenium.webdriver.common.by import By


class CreateNewUser:
    cross = "//button[@title='Close navigation']"
    # cross2 = "//button[@title='Close navigation']"
    New_user_page_URL = "https://osc-ultimate-demo.mageplaza.com/"
    btnCreate_New_User_xpath = "//li/a[text()='Create an Account']"
    txtFirstName_xpath = "//input[@id='firstname']"
    txtLastName_xpath = "//input[@id='lastname']"
    txtEmail_xpath = "//input[@id='email_address_create']"
    txtDateOfBirth_xpath = "//input[@id='mp_sociallogin_dob']"
    txtPassword_xpath = "//input[@id='password-social']"
    txtPassword_Confirm_xpath = "//input[@id='password-confirmation-social']"
    btnRegister_xpath = "//div/form/div/div/button[@id = 'button-create-social']"
    btnDropDownForSingOut = "//div[@class='panel header']//button[@type='button']"
    btnClickOnSingOut = "//div[@aria-hidden='false']//a[normalize-space()='Sign Out']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCreate_new_user(self):
        self.driver.find_element(By.XPATH, self.cross).click()
        self.driver.find_element(By.XPATH, self.btnCreate_New_User_xpath).click()

    def setUserFname(self, fname):
        self.driver.find_element(By.XPATH, self.txtFirstName_xpath).send_keys(fname)

    def setUserLname(self, lname):
        self.driver.find_element(By.XPATH, self.txtLastName_xpath).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.txtDateOfBirth_xpath).send_keys(dob)

    def setPass(self, password):
        self.driver.find_element(By.XPATH, self.txtPassword_xpath).send_keys(password)


    def setConfpass(self, confpassord):
        self.driver.find_element(By.XPATH, self.txtPassword_Confirm_xpath).send_keys(confpassord)

    def clickOnRegister(self):
        self.driver.find_element(By.XPATH, self.btnRegister_xpath).click()

    def clickOnSingOut(self):
        self.driver.find_element(By.XPATH, self.btnDropDownForSingOut).click()
        self.driver.find_element(By.XPATH, self.btnClickOnSingOut).click()
