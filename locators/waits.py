#time
import time

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("D:\\Python\\selenium_training\\Files\\loading.html")
# driver.maximize_window()
# time.sleep(20)
# driver.find_element("name","fname").send_keys("Harish")
# time.sleep(2)
# driver.find_element("name","lname").send_keys("Chikkammanavar")


###################################################################################################
#implicit wait

# from selenium import webdriver
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.implicitly_wait(30)
#
# driver.get("D:\\Python\\selenium_training\\Files\\loading.html")
# driver.maximize_window()
# driver.find_element("name","fname").send_keys("Harish")
# driver.find_element("name","lname").send_keys("Chikkammanavar")

###################################################################################################
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# wait_obj = WebDriverWait(driver, 10)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(2)

# try:
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#     print("succesfull login")
#     print(driver.title)
# except:
#     print("unsuccesfull login")
#########################################################################################
# try:
#     wait_obj.until(expected_conditions.title_is(title='Swag Labs'))
#     print("succesfull login")
#     print(driver.title)
# except:
#     print("unsuccesfull login")


#########################################################################################
# from  selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# wait_obj = WebDriverWait(driver, 50)
#
# driver.get(r"D:\Python\selenium_training\Files\progressbar.html")
# driver.find_element("xpath","//button[text()='Click Me']").click()
# wait_obj.until(expected_conditions.visibility_of_element_located(("xpath","//div[text()='100%']")))
# time.sleep(2)
# driver.find_element("xpath","//button[text()='Click Me']").click()
# time.sleep(15)

#########################################################################################
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# wait_obj = WebDriverWait(driver, 50)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
# driver.find_element("name","q").send_keys("Selenium")
# time.sleep(1)
# driver.find_element("name","btnK").click()
# wait_obj.until(expected_conditions.visibility_of_element_located(("xpath","//h3[text()='Selenium']")))
# time.sleep(2)
# driver.find_element("xpath","//h3[text()='Selenium']").click()

#########################################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

wait_obj = WebDriverWait(driver, 50)

# driver.implicitly_wait(30)
driver.get(r"D:\Python\selenium_training\Files\loading.html")
driver.maximize_window()
wait_obj.until(expected_conditions.visibility_of_element_located(("xpath","//div[contains(@id,'myDiv')]")))
time.sleep(2)
driver.find_element("name","fname").send_keys("Harish")

