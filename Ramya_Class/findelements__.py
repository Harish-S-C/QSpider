import time

'''
1.  wap to print the elements present at the footer of https://demowebshop.tricentis.com/
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# print(footer_elements)      ## list of web-elements     ## [wb1, wb2, wb3, wb4, wb5, wb6,....wb22]

for ele in footer_elements:
    print(ele.text)

print(footer_elements[10].text)

for ele in footer_elements[-10::]:
    print(ele.text)

for ele in footer_elements[7:15:1]:
    print(ele.text)

#####################################################################################
'''
2.  wap to print the elements present in the categories section in https://demowebshop.tricentis.com/
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# print(categories)           ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]

for ele in categories:
    print(ele.text)

# ## fetching last three elements of the list
# for ele in categories[-3::]:
#     print(ele.text)

#####################################################################################
'''
3.  wap to print all the elements present in the popular searches in https://www.myntra.com/
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
# print(popular_searches)     ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6,...]

for ele in popular_searches:
    print(ele.text)

#####################################################################################
'''
4.  wap to print all the links present in https://www.python.org/
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.python.org/')
time.sleep(2)

'''
all links --> href attribute --> anchor tags
'''

all_links = driver.find_elements('tag name', 'a')
# print(all_links)        ## list of web-elements         ## [a1, a2, a3, a4, a5, a6, a7, a8, a9]

for link in all_links:
    print(link.get_attribute('href'))

#####################################################################################
'''
5.  wap to write the data to the textboxes present in demo.html
'''
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\Sel-M15-Aug11\files_\demo.html')
time.sleep(2)
all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# print(all_textboxes)        ## list of web-elements         ## [tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9]

data_list = ['dark', 'GOT', 'heart beat', 'wednesday', 'breaking bad', 'parizaat', 'arrow', 'peaky blinders', 'demon slayer']

for textbox, data in zip(all_textboxes, data_list):
    textbox.send_keys(data)












