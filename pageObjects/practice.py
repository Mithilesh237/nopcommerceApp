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
driver.find_element(By.TAG_NAME,"")
input1 = driver.find_element(By.CSS_SELECTOR,"#inputText1")
input2 = driver.find_element(By.CSS_SELECTOR,"#inputText2")

input1.send_keys("I am working on action chains class")

act = ActionChains(driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

#act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()  --single line

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.perform()

#act.key_down(Keys.CONTROL).send_keys("c").perform()  --single line

input2.click()
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.perform()

#nput2.click().key_down(Keys.CONTROL).send_keys("v").perform()  --single line






