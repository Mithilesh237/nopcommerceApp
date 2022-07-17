from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    text_email_id = "Email"
    text_pas_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    click_logout = "Logout"
    #driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,name):
        self.driver.find_element(By.ID,self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(name)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.text_pas_id).clear()
        self.driver.find_element(By.ID, self.text_pas_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.click_logout).click()




