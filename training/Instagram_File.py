import time

# To Open Google Chrome without close automatically
from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options)

driver.get("https://www.instagram.com/")
time.sleep(2)

# driver.get("https://www.myntra.com/")
# time.sleep(2)