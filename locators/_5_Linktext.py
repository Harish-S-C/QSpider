from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(1)
driver.find_element("link text","Hidden Elements & AJAX").click()
time.sleep(2)
driver.find_element("link text","Download Files").click()
time.sleep(2)
driver.close()
