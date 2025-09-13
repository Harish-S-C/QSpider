import time

# To Open Google Chrome without close automatically
from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options)

#launch the Application
driver.get("https://www.myntra.com/")
time.sleep(2)

#Maximize Window
# driver.maximize_window()
# time.sleep(5)

#To go Back
# driver.back()
# time.sleep(2)

#To go Forward
# driver.forward()
# time.sleep(2)

#To go Refresh
# driver.refresh()
# time.sleep(2)

#Fullscreen Window
# driver.fullscreen_window()

#To get Title
# print(driver.title)

#To get which name of the Browser
# print(driver.name)

#To get the URL
# print(driver.current_url)

# To take screenshot in Current Directory
# driver.save_screenshot('myntra.png')

#To get screenshot in other directory
# driver.save_screenshot('D:\\Python\\selenium_training\\Files\\myntra1.png')

#To close the browser
# driver.close()

#To close the Multiple browser
#driver.quit()