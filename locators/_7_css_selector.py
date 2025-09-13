# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# driver.find_element("css selector","input[name='firstname']").send_keys("Harish")
# time.sleep(1)
# driver.find_element("css selector","input[name='lastname']").send_keys("S C")
# time.sleep(1)
# driver.find_element("css selector","input[name='reg_email__']").send_keys("harishsc10@gmail.com")
# driver.find_element("css selector","input[name='reg_passwd__']").send_keys("harishSC123")
#
#
import time

from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
driver.find_element("css selector","a[class='ico-register']").click()
time.sleep(1)
driver.find_element("css selector","input[id='gender-female']").click()
time.sleep(1)
driver.find_element("css selector","input[id='FirstName']").send_keys("Reeshma")
time.sleep(1)
driver.find_element("css selector","input[id='LastName']").send_keys("Naniah")
time.sleep(1)
driver.find_element("css selector","input[id='Email']").send_keys("email@gmail.com")
time.sleep(1)
driver.find_element("css selector","input[id='Company']").send_keys("Movie Heroine")
time.sleep(1)
driver.find_element("css selector","input[id='Password']").send_keys("harish@123")
time.sleep(1)
driver.find_element("css selector","input[id='ConfirmPassword']").send_keys("harish@123")
time.sleep(1)
driver.find_element("css selector","button[id='register-button']").click()