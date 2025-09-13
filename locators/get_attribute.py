# 1.  wap to write the getattribute('href') of footer section in https://demo.nopcommerce.com/
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# time.sleep(2)
# footer_elements = driver.find_elements("xpath","//div[@class='footer-upper']//a")
# print(len(footer_elements))
# for ele in footer_elements:
#     print(ele.get_attribute('href'))
# driver.close()

#######################################################################################################

# 2. wap to print all the getattribute('href') of anchor tag present in https://www.python.org/
from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://www.python.org/")
driver.maximize_window()
time.sleep(2)

all_links = driver.find_elements("tag name","a")
print(len(all_links))
for link in all_links:
    print(link.get_attribute("href"))

driver.close()

























