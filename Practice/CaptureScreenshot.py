from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

#########################Login###############################
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\\chromedriver2022\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.get("https://www.nopcommerce.com/en/demo")

reglink = Keys.CONTROL + Keys.RETURN
driver.find_element(By.XPATH, "//nav/ul/li/a[text()='Get started']").send_keys (reglink)
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH,"//div[@class='page-body page-body-wrapper']/div/div/div/div/a[text()='Download nopCommerce']").send_keys(reglink)

#New tab selenium 4: Open new tab and switch to new tab:




