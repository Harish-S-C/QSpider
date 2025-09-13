'''
text    :   It is a property. It will give the text of the web-element

'''
import time

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# home = driver.find_element('xpath', '//a[@data-group="home"]')
# print(home.text)
#
# beauty = driver.find_element('xpath', '//a[@data-group="beauty"]')
# print(beauty.text)

#####################################################################################
'''
get_attribute() :   It is a Selenium WebDriver method used to fetch the value of an attribute of a web element.
                    It returns the string value of the attribute.
                    SYNTAX  :   web_element.get_attribute("attr_name")
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# beauty = driver.find_element('xpath', '(//a[text()="Beauty"])[1]')
# print(beauty.get_attribute('href'))
# print(beauty.get_attribute('data-color'))
# print(beauty.get_attribute('style'))

#####################################################################################
'''
is_enabled  :   is_enabled() is a boolean method in Selenium WebDriver used to check whether a web element is 
                enabled (i.e., can be interacted with) or disabled.
                
                Returns:
                    True → if the element is enabled
                    False → if the element is disabled

'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.instagram.com/')           ## login form will appear
time.sleep(2)

ele = driver.find_element('xpath', '//div[text()="Log in"]')
print(ele.is_enabled())


































