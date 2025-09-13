import time
from selenium import webdriver

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

options=webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Edge()

# driver=webdriver.Firefox()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element("id","name").clear()
driver.find_element("id","name").send_keys("Harish")
driver.find_element("id","email").clear()
driver.find_element("id","email").send_keys("harishsc10@gmail.com")
driver.find_element("id","phone").clear()
driver.find_element("id","phone").send_keys("7204442510")
driver.find_element("id","textarea").clear()
driver.find_element("id","textarea").send_keys("620/1 3rd Cross M G Koppal Road Hebbal Mysuru 17")
driver.find_element("id","male").click()
driver.find_element("id","saturday").click()
