from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import pickle

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver_service = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)
f = open('all_courses.txt', 'w', encoding="utf-8")
err = open('err_all_courses.txt', 'w', encoding="utf-8")
course_name_pattern = re.compile(r'(([A-Z]+)\s(\d\d\d\d\d))\s\-\s((.)+)')
term_offered_pattern = re.compile(r'Typically offered (.*)\.C')
credits_pattern = re.compile(r'((Credits)|(Credit Hours)): (\d+)\.\d\d')
all_courses = []

# get all available courses from all pages
# using pdf version since its easier to deal with
page_nums = range(1, 80)
for page_num in page_nums:
  # f.write(f"\n\n\n\n\n*******************page {page_num}*************************\n")
  url = f'https://catalog.purdue.edu/content.php?filter%5B27%5D=-1&filter%5B29%5D=&filter%5Bcourse_type%5D=-1&filter%5Bkeyword%5D=&filter%5B32%5D=1&filter%5Bcpage%5D={page_num}&cur_cat_oid=14&expand=1&navoid=16894&print=1&filter%5Bexact_match%5D=1#acalog_template_course_filter'
  driver.get(url)
  elem = driver.find_elements(by=By.CLASS_NAME, value='width')
  print(f'total number of course in page {page_num}: {len(elem)}')
  for e in elem:
    try:
      lines = e.text.split('\n')
      course = lines[0]
      description = lines[1]
      search_out = course_name_pattern.search(course)
      course_code = ''
      course_title = ''
      if search_out:
        new_course = dict()
        course_code = search_out.group(1)
        course_title = search_out.group(4)
        course_credits = credits_pattern.search(description).group(4)
        term_offered_out = term_offered_pattern.search(description)
        term_offered = set()
        if term_offered_out:
          term_offered = term_offered_out.group(1)
          term_offered = set(term_offered.split(' '))
        new_course["course_tag"] = course_code
        new_course["course_name"] = course_title
        new_course["course_credits"] = int(course_credits)
        new_course["description"] = description
        new_course["terms"] = term_offered
        all_courses.append(new_course)
        f.write(new_course.__str__())
        f.write('\n')
    except Exception as error:
      print(error)
      err.write(e.text)

f_pkl = open('all_courses.pickle', 'wb')
pickle.dump(all_courses, f_pkl)

# clean up
driver.close()
f.close()
err.close()
f_pkl.close()