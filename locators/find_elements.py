#1.  wap to print the elements present at the footer of https://demo.nopcommerce.com/

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get('https://demo.nopcommerce.com/')
# driver.maximize_window()
# time.sleep(2)
# footer_elements = driver.find_elements("xpath","//div[@class='footer-upper']//a")
# print(len(footer_elements))
# for ele in footer_elements:
#     print(ele.text)

#############################################################################################
#2.  wap to print the elements present at the footer of https://demo.nopcommerce.com/

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get('https://demowebshop.tricentis.com/')
# driver.maximize_window()
# time.sleep(2)
# footer_elements = driver.find_elements("xpath","//div[@class='footer-menu-wrapper']//a")
# print(len(footer_elements))
# for ele in footer_elements:
#     print(ele.text)
# driver.close()

###################################################################################################
# 3.  wap to print the elements present in the categories section in https://demowebshop.tricentis.com/

#
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# time.sleep(2)
# categories = driver.find_elements("xpath","//div[@class='block block-category-navigation']//a")
# print(len(categories))
# for ele in categories:
#     print(ele.text)
# driver.close()


######################################################################################################
# 4.  wap to print all the elements present in the popular searches in https://www.myntra.com/

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.myntra.com/")
# driver.maximize_window()
# time.sleep(2)
# popular_searches = driver.find_elements("xpath","//div[@class='desktop-pSearchlinks']/a")
# print(len(popular_searches))
# for ele in popular_searches:
#     print(ele.text)
# print(popular_searches[3].text)#sandals
# driver.close()

#######################################################################################################
#5.  wap to print all the links present in https://www.python.org/

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.python.org/")
# driver.maximize_window()
# time.sleep(2)
# all_links = driver.find_elements("tag name","a")
# print(len(all_links))
# for link in all_links:
#     print(link.text)
# driver.close()

#####################################################################################################
# 6.  wap to write the data to the textboxes present in demo.html
from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("D:\\Python\\selenium_training\\Files\\demo.html")
driver.maximize_window()
time.sleep(2)
textboxes = driver.find_elements("xpath","//input[@name='fname']")
# for ele in textboxes:
#     ele.send_keys("Harish")
data_list = ['dark', 'GOT', 'heart beat', 'wednesday', 'breaking bad', 'parizaat', 'arrow', 'peaky blinders', 'demon slayer']

for textbox, data in zip(textboxes, data_list):
    textbox.send_keys(data)



