from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import re
import pickle
import json

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver_service = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)

f_requisites = open('all_purdue_requisites.json', 'w')
all_requisites = []

# url = f'https://wl.mypurdue.purdue.edu/'
# driver.get(url)
# username_elem = driver.find_element(by=By.ID, value="username")
# username_elem.send_keys('zhan3624')
# username_elem = driver.find_element(by=By.ID, value="password")
# username_elem.send_keys('0709,push')
# print(driver.find_element(by=By.NAME, value="submit").click())
# driver.find_element(by=By.ID, value='layout_8').click()

# # url = f'https://selfservice.mypurdue.purdue.edu/prod/bzwkpreq.p_main'
# # url = f'https://selfservice.mypurdue.purdue.edu/prod/bzwkpreq.p_disp_cat_term_date'
# # url = f'https://selfservice.mypurdue.purdue.edu/prod/bzwkpreq.p_display_prereqs'
# elems = driver.find_elements(by=By.CLASS_NAME, value='listItem')
# for e in elems:
#   if e.text == 'Course Prerequisite Report':
#     print("clicked!")
#     e.click()

url = "https://wl.mypurdue.purdue.edu/static_resources/portal/jsp/ss_redir_lp5.jsp?pg=272"
driver.get(url)
# Purdue authentication
driver.find_element(by=By.ID, value="username").send_keys('zhan3624')
driver.find_element(by=By.ID, value="password").send_keys('0709,push')
print(driver.find_element(by=By.NAME, value="submit").click())
# Select term 'Spring 2022'
form_elem = driver.find_element(by=By.ID, value='term_input_id')
select_fr = Select(form_elem)
select_fr.select_by_visible_text('Spring 2022')
form_elem.submit()
# select all valid course code headers:
form_elem = driver.find_element(by=By.ID, value='subj_id')
# for e in form_elem:
#   print('-------------------------------------')
#   print(e.text)
select_fr = Select(form_elem)
select_fr.select_by_index(0)
form_elem.submit()

print(driver.save_screenshot('screenshot.png'))
# clean up
driver.close()
f_requisites.close()