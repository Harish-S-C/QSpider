import time
from selenium import webdriver

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

options=webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Edge(options)

# driver=webdriver.Firefox()

driver.get("https://www.saucedemo.com/")

driver.find_element("id","user-name").send_keys("visual_user")
time.sleep(2)
driver.find_element("id","password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element("id","login-button").click()
time.sleep(2)
driver.find_element("id","react-burger-menu-btn").click()
time.sleep(2)
driver.find_element("id","logout_sidebar_link").click()