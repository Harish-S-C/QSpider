import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

# data=driver.find_element("xpath","(//table[@name='BookTable']//tr/td)[6]")
# print(data.text)

# for r in range(2, 8):
#     for c in range(1, 5):
#         data = driver.find_element('xpath', f'//table[@name="BookTable"]//tr[{r}]/td[{c}]')
#         print(data.text, end='\t\t')
#     print()




































