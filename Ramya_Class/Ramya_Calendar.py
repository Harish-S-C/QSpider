import time


# ## Solution1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.makemytrip.com/')
driver.maximize_window()
time.sleep(2)

## closing the login form
driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
time.sleep(2)

## click on departure
driver.find_element('xpath', '//span[text()="Departure"]').click()
time.sleep(2)

def select_date(month, date):
    while True:
        try:
            driver.find_element('xpath', f'//div[text()="{month}"]/../..//p[text()="{date}"]').click()
            break
        except:
            driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()

select_date('October 2025', 20)


##############################################################################################################

## Solution2
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.makemytrip.com/')           ## login form will appear
# driver.maximize_window()
# time.sleep(2)
#
# ## closing the login form
# driver.find_element('xpath', '//span[@class="commonModal__close"]').click()
# time.sleep(2)
#
# ## click on departure
# driver.find_element('xpath', '//span[text()="Departure"]').click()
# time.sleep(2)
#
# while True:
#     month = driver.find_element('xpath', '(//div[@class="DayPicker-Caption"])[1]')
#     print(month.text)
#
#     if month.text == 'October 2025':
#         driver.find_element('xpath', '(//p[text()="30"])[1]').click()
#         break
#     else:
#         driver.find_element('xpath', '//span[@aria-label="Next Month"]').click()































