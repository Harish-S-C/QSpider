from selenium import webdriver

c_driver = webdriver.Chrome()
print("Driver in use:", c_driver.service.path)  # Shows which driver is running

c_driver.get("https://www.google.com")
c_driver.quit()

e_driver = webdriver.Edge()
print("Driver in use:", e_driver.service.path)  # Shows which driver is running

e_driver.get("https://www.google.com")
e_driver.quit()

f_driver = webdriver.Firefox()
print("Driver in use:", f_driver.service.path)  # Shows which driver is running

f_driver.get("https://www.google.com")
f_driver.quit()
