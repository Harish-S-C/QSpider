import time

from selenium import  webdriver

# For Google Chrome
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

# For Edge
# options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Edge(options)

# for Firefox
driver=webdriver.Firefox()

# driver.get("https://www.instagram.com/")
# time.sleep(1)
# driver.find_element("class name","_aa4b._add6._ac4d._ap35").send_keys("Harish")

# driver.get("https://www.saucedemo.com/")
# driver.find_element("class name","input_error.form_input").send_keys("Harish")

driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element("class name","inputtext._55r1._6luy").send_keys("harishsc10@gmail.com")
time.sleep(1)
driver.find_element("class name","inputtext._55r1._6luy._9npi").send_keys("haRIsh2123")
time.sleep(1)
driver.find_element("class name","_42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()
print(driver.title)