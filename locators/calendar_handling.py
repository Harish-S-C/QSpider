# from selenium import webdriver
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options)
#
# driver.get("https://www.makemytrip.com/")
# driver.maximize_window()
# time.sleep(2)
# driver.find_element("xpath","//span[@class='commonModal__close']").click()
# time.sleep(2)
# driver.find_element("xpath","(//span[@class='lbl_input appendBottom10'])[3]").click()
# time.sleep(5)
# driver.find_element("xpath","//div[text()='July']/../..//p[text()='31']").click()
# driver.close()


from selenium import webdriver
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options)

driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath","//span[@class='commonModal__close']").click() #to close the small window
time.sleep(2)
driver.find_element("xpath","(//span[@class='lbl_input appendBottom10'])[3]").click() #to click the dropdown of date selector
time.sleep(5)
#Afterwards we need to identify the web welement by dependent and Independdent webelement
#Example here we need to select the date ,month and year for that first we need to identify which is dependent and which is independent web element(here Date is dependent & Mon,year is independent)
#Note for any Backtraversing first we need to write independent weebelement and we need to write dependent webelement
def select(mon,date):
    while True:
        try:
            driver.find_element("xpath",f"//div[text()='{mon}']/../..//p[text()='{date}']").click() #this is backtraversing
            break
            #Note if we get the date within the present date selector then need to break and to work in try block if it not get then need to click on right arrow button in except block
            #while condition need to apply if we dont know the end value
            #then in order to make dynamic so that we need to pass the date and month in function method
        except:
            driver.find_element("xpath","//span[@class='DayPicker-NavButton DayPicker-NavButton--next']").click()

select("September 2026","1")

###################################################################################################

