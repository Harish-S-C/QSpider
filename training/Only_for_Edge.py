from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

options = Options()
options.add_experimental_option("detach",True)


serv_obj=Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj,options=options)

driver.get("https://www.google.com")
driver.get("https://www.amazon.in/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.name)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.back()
