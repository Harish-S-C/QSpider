'''
Synchronization :   Matching the speed of the webdriver to the web-application.

There are 2 types of synchronization
*   unconditional synchronization   :   No conditions are passed.
        we achieve unconditional synchronization by passing time.sleep(n)
        This is a static wait.
        Unnecessary wait is too much in unconditional synchronization

*   conditional synchronization     :   Conditions are passed.
        There are 2 types
        *   implicit_wait   :   The conditions are already defined internally
                                SYNTAX  :   driver.implicitly_wait(n)
                                The driver will wait until the element is available on the application,
                                as soon as the element is available, it will start performing the operations right away.
                                No unnecessary wait.

        *   explicit_wait   :   The conditions are given externally.
                                We have to import expected_conditions and WebDriverWait

                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions
                                    WebDriverWait       --> class
                                    expected_conditions --> module

                                wait_obj = WebDriverWait(driver, timeouttime)

'''

import time

## time.sleep()
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\loading.html')
time.sleep(20)
driver.find_element('xpath', '//input[@name="fname"]').send_keys('Sawan')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('kumar')

###################################################################################################

## implicit_wait

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.implicitly_wait(30)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\loading.html')

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Sawan')
time.sleep(1)
driver.find_element('xpath', '//input[@name="lname"]').send_keys('kumar')

###################################################################################################

## explicit_wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 30)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\loading.html')

wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))

driver.find_element('xpath', '//input[@name="fname"]').send_keys('Sawan')
driver.find_element('xpath', '//input[@name="lname"]').send_keys('kumar')

###################################################################################################

## Eg2
## time.sleep()

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()
time.sleep(40)
driver.find_element('xpath', '//button[text()="Click Me"]').click()


###################################################################################################
## Eg2
## implicit_wait

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
driver.implicitly_wait(50)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()
driver.find_element('xpath', '//div[text()="100%"]')
time.sleep(1)
driver.find_element('xpath', '//button[text()="Click Me"]').click()

###################################################################################################

## Eg3
## explicit_wait

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 50)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()
wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
time.sleep(1)
driver.find_element('xpath', '//button[text()="Click Me"]').click()

###################################################################################################

## Eg3
## explicit_wait
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

wait_obj = WebDriverWait(driver, 10)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id', 'user-name').send_keys('standard_userrrrrrr')
time.sleep(1)
driver.find_element('id', 'password').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('id', 'login-button').click()
time.sleep(2)

try:
    wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
    print("succesfull login")
except:
    print("unsuccesfull login")





































