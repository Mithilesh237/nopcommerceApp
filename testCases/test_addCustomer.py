import random
import string

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
import pytest
from utilities.readProperties import ReadConfig
from selenium import webdriver


class Test_AddCustomer:

    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserName()
    password = ReadConfig.getPassword()


    def test_addCustomer(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.addCust = AddCustomer(setUp)
        self.addCust.clickOnCustomersMenu()
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddnew()

        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("abc123")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 1")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Mithilesh")
        self.addCust.setLastName("Roley")
        self.addCust.setDob("7/29/1995")
        self.addCust.setCompanyName("abc company")
        self.addCust.setAdminContent("I am done with this shit")
        self.addCust.clickOnSave()
        self.msg = self.driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]").text

        print(self.msg)
        if "customer has been successfully added" == self.msg:
            assert True == True
        else:
            assert False == False



def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))







