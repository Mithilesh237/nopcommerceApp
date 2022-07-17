from pageObjects.LoginPage import LoginPage
import pytest
import time
from utilities.readProperties import ReadConfig

class Test_Login:

    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    baseURL = ReadConfig.getApplicationURL()

    def test_homePage(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot("C:\\Users\Hello\PycharmProjects\\nocommerceApp\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


    def test_logIn(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        login_title = self.driver.title
        lp.clickLogout()
        time.sleep(5)
        self.driver.close()
        if login_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False



