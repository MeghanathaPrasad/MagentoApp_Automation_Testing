from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginPage:
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_xpath = "//input[@id='login']"
    button_login_xpath = "//span[normalize-space()='Sign in']"
    navigation_close_xpath = "//button[@title='Close navigation']"
    link_MyAccount_xpath = "(//a[@title='My Account'])[1]"
    link_logout_link_text = "//a[normalize-space()='Sign Out']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        # self.driver
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.navigation_close_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.link_MyAccount_xpath).click()
        self.driver.find_element(By.XPATH, self.link_logout_link_text).click()





