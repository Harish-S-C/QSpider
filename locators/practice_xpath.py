#Relative xpath(//tagname[@attribute_name="attribute_value"]

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='username']").send_keys("Admin")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='password']").send_keys("admin123")
# time.sleep(1)
# driver.find_element("xpath","//button[@type='submit']").click()
# time.sleep(10)
#
# print(driver.title)
# print(driver.current_url)
# print(driver.name)
# driver.close()

###########################################################################################
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://demo.nopcommerce.com/")
# print(driver.name)
# print(driver.title)
# print(driver.current_url)
# time.sleep(1)
#
# driver.find_element("xpath","//a[text()='Sitemap']").click()
# time.sleep(5)
# driver.find_element("xpath","//a[text()='New products']").click()
# time.sleep(5)
# driver.find_element("xpath","//a[text()='Wishlist']").click()
# time.sleep(15)
#
# driver.close()

############################################################################################
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
# driver.find_element("xpath","//a[text()='Register']").click()
# driver.find_element("xpath","(//input[@type='text'])[2]").send_keys("Harish")
# time.sleep(1)
# driver.find_element("xpath","(//input[@type='text'])[3]").send_keys("Chikkammmanavar")
# time.sleep(1)
# driver.find_element("xpath","(//input[@type='text'])[4]").send_keys("Techno Touch Business Solutions")
# time.sleep(10)
#
# driver.close()

#########################################################################################
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://demo.nopcommerce.com/")
# time.sleep(1)
# driver.find_element("xpath","(//input[contains(@type,text)])[2]").send_keys("Tabs")
# time.sleep(1)
# driver.find_element("xpath","(//button[contains(@type,'submit')])[1]").click()
# time.sleep(15)
# driver.close()

##########################################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://demo.nopcommerce.com/")
# time.sleep(1)
# driver.find_element("xpath","//a[text()='Log in']").click()
# time.sleep(1)
# driver.find_element("xpath","(//input[starts-with(@type,'email')])[1]").send_keys("harishsc10@gmail.com")
# time.sleep(1)
# driver.find_element("xpath","(//input[starts-with(@type,'password')])[1]").send_keys("Harish123")
# time.sleep(1)
# driver.find_element("xpath","//button[text()='Log in']").click()
# time.sleep(15)
#
#
# driver.close()