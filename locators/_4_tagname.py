from selenium import webdriver
import time

#For Google
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

#For edge
# options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Edge(options)

#For Firefox
driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(1)
driver.find_element("tag name","input").send_keys("Hello")
time.sleep(1)
driver.find_element("tag name","input").send_keys("123")
time.sleep(1)
driver.close()