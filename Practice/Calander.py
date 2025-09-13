from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath","//span[@class='commonModal__close']").click()
time.sleep(1)
driver.find_element("xpath","//span[text()='Departure']").click()
time.sleep(1)
driver.find_element("xpath","//div[text()='October 2025']/../..//p[text()=31]").click()








# def select(mon,date):
#     while True:
#         try:
#             driver.find_element("xpath", f"//div[text()='{mon}']/../..//p[text()='{date}']").click()
#             break
#         except:
#             driver.find_element("xpath","//span[@aria-label='Next Month']").click()
#
# select("September 2025","30")