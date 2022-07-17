from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\\chromedriver2022\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(5)

#When there is anchor tag, we can use link_text
driver.get("https://text-compare.com/")