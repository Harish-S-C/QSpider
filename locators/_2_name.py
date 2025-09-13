# from selenium import webdriver
# import time

#To open in Google Chrome

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

#To Open in Firefox
# driver=webdriver.Firefox()

#To Open in Edge
# options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Edge()
#
# driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(1)
# driver.find_element("name","username").send_keys("Admin")
# driver.find_element("name","password").send_keys("admin123")
# time.sleep(1)
# driver.find_element("xpath","//button[normalize-space()='Login']").click()
# time.sleep(2)
# driver.close()

# ************************************************************************
#  Login for Instagram

from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://www.instagram.com/")
time.sleep(1)
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
time.sleep(1)
driver.close()


