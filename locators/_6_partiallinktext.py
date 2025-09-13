from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get('https://mail.hostinger.com/')
driver.find_element("partial link text",'Forgot').click()
time.sleep(1)
driver.quit()
