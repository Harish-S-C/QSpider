# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

# driver.get("https://www.flipkart.com/")
# driver.find_element("xpath","//span[text()='Mobiles & Tablets']").click()
# time.sleep(1)
# driver.find_element("xpath","//span[text()='Home & Furniture']").click()
# time.sleep(1)
# driver.find_element("xpath","//span[text()='Electronics']").click()
# time.sleep(1)


###############################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome()
#
# driver.get('D:\\Python\\selenium_training\\Ramya\\css_selector_dup.html')
# time.sleep(2)
# driver.find_element("xpath","html/body/input[1]").send_keys("Harish")
# time.sleep(1)
# driver.find_element("xpath","html/body/input[2]").send_keys("harish@123")
# time.sleep(1)


###############################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.saucedemo.com/")
# driver.maximize_window()
# driver.find_element("xpath","//input[@id='user-name']").send_keys("problem_user")
# time.sleep(1)
# driver.find_element("xpath","//input[@id='password']").send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='login-button']").click()

##########################################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# driver.maximize_window()
# driver.find_element("xpath","//input[@name='firstname']").send_keys("Harish")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='lastname']").send_keys("Chikkammanavar")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='reg_email__']").send_keys("harishhc10@gmail.com")
# time.sleep(1)
# driver.find_element("xpath","//input[@name='reg_passwd__']").send_keys("1234567890")
# time.sleep(1)
# driver.find_element("xpath","//button[@name='websubmit']").click()

########################################################################################

# from selenium import webdriver
# import time
#
# driver=webdriver.Firefox()
#
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# driver.find_element("xpath","//span[text()='Mobiles & Tablets']").click()
# time.sleep(1)
# driver.find_element("xpath","//*[text()='Home & Furniture']").click()


####################################################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.youtube.com/")
# driver.maximize_window()
# driver.find_element("xpath","//input[@name='search_query']").send_keys("KGF")
# time.sleep(2)
# driver.find_element("xpath","//button[@title='Search']").click()
# time.sleep(5)
#
# driver.close()

###########################################################################################
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# driver.maximize_window()
#
# driver.find_element("xpath","(//input[@type='text'])[1]").send_keys("Giridhar")
# time.sleep(1)
# driver.find_element("xpath","(//input[@type='text'])[2]").send_keys("Lakshmi")
# time.sleep(5)
#
# driver.close()

#################################################################################################
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
# driver.get("https://www.malabargoldanddiamonds.com/")
# driver.maximize_window()
#
# driver.find_element("xpath","//a[contains(text(),'Platinum')]").click()

###################################################################################################
# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)

# driver.get("https://demo.nopcommerce.com/")
# time.sleep(1)
# driver.find_element("xpath","//a[text()='Log in']").click()
# time.sleep(1)
# driver.find_element("xpath","//input[contains(@id,'Email')]").send_keys("harishsc10@gmail.com")
# time.sleep(1)
# driver.find_element("xpath","//input[starts-with(@name,'Password')]").send_keys("123456789")
# time.sleep(1)
# driver.find_element("xpath","(//button[@type='submit'])[2]").click()


###################################################################################################
# from selenium import webdriver
# import time

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get('file:///D:/Python/selenium_training/Files/demo.html')
# # driver.find_element("xpath","(//input[@name='download'])[6]").click()
# driver.find_element("xpath","//td[text()='Perl']/..//input[@name='download']").click()
# driver.find_element("xpath","//td[text()='Java']/..//input[@name='download']").click()
#
# driver.find_element("xpath","//td[text()='Android']/..//a[text()='Download']").click()
# time.sleep(5)
# driver.find_element("xpath","//td[text()='3.141']/..//a[text()='Download']").click()

####################################################################################################

# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.tradingview.com/")
# driver.maximize_window()
# time.sleep(3)
#
# driver.find_element("xpath","//span[text()='Search']").click()
# time.sleep(2)
# driver.find_element("xpath","//input[@name='query']").send_keys("TATAMOTORS")
# time.sleep(2)
# driver.find_element("xpath","(//em[text()='TATAMOTORS'])[3]").click()
# time.sleep(2)
# Sellrate = driver.find_element("xpath","(//span[text()='TATAMOTORS']/../../..//span[@translate='no'])[1]")
# print(Sellrate.text)
# time.sleep(5)
# driver.close()

##################################################################################################################

from selenium import webdriver
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://in.tradingview.com/')
time.sleep(2)

driver.find_element('xpath', '//span[text()="Search"]').click()
time.sleep(2)

driver.find_element('xpath', '//input[@name="query"]').send_keys('Tatamotors')
time.sleep(2)

driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
time.sleep(2)

tatamotors = driver.find_element('xpath', "//span[text()='TATAMOTORS']/../../..//span[@class='highlight-maJ2WnzA highlight-BSF4XTsE price-qWcO4bp9']")
print(tatamotors.text)















# (//em[text()="TATAMOTORS"])[3]