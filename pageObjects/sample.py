from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#########################Login###############################
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\\chromedriver2022\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://admin-demo.nopcommerce.com/")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[text()='Log in']").click()

#########################AddCustomer##################################

driver.find_element(By.XPATH,"//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]/p[1]").click()
driver.find_element(By.XPATH,"//body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/ul[1]/li[1]/a[1]/p[1]").click()
driver.find_element(By.XPATH,"//div[@class='float-right']/a").click()


driver.find_element(By.XPATH,"//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div").click()
elements = driver.find_elements(By.XPATH,"//ul[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li")

for element in elements:
    if element.text == "Test store 2":
        element.click()