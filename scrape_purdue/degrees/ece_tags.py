from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
import pickle
import json

# set up scraping
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver_service = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(options=options, service=driver_service)
f_ece = open("../../backend/MakeMyDegree/fixture/ece_tags.json", "w", encoding="utf-8")
all_tags = []

# connect to CompE degree page 
catoid = 10
poid = 12687
url = f'https://catalog.purdue.edu/preview_program.php?catoid={catoid}&poid={poid}'
driver.get(url)
degree_name = driver.find_element(by=By.ID, value="acalog-page-title")
# get and filter the degrees
elem = driver.find_elements(by=By.CLASS_NAME, value='acalog-core')
# tag_pattern = re.compile(r'(.+)\s(\((\d+)\scredits?\))\s?\n((((.*)\s\-\s(.*))\n?)+)')
tag_pattern = re.compile(r'(.+)\s(\((\d+)\scredits?\))\s?\n')
course_pattern = re.compile(r'[A-Z]+\s\d\d\d\d\d')
for e in elem:
  content = e.text
  # examine and prune e.text
  search_out = tag_pattern.search(content)
  if search_out:
    tag_name = search_out.group(1)
    credits = int(search_out.group(3))
    course_list = list(set(course_pattern.findall(content)))
    all_tags.append({
      "tag_name": tag_name,
      "credits": credits,
      "course_list": course_list
    })

# special handling for compE
all_tags[2]["course_list"] = ["ECE 47700", "ECE 49022", "ECE41200"]
all_tags[4]["tag_name"] = "C Programming"
all_tags[6]["tag_name"] = "Math Option 1"
all_tags[7]["tag_name"] = "Math Option 2"
additional = [
  ["Science Requirement", 4, ["PHYS 27200", "BIOL 11000", "BIOL 11100", "BIOL 12100", "BIOL 13500", "BIOL 13100", "CHM 11600", "CHM 12400", "PHYS 31000", "PHYS 32200", "PHYS 34200", "PHYS 34400"]],
]

url = f'https://catalog.purdue.edu/preview_program.php?catoid=10&poid=13430'
driver.get(url)
# get and filter the degrees
elem = driver.find_elements(by=By.CLASS_NAME, value='acalog-course')
course_pattern = re.compile(r'[A-Z]+\s\d\d\d\d\d')
gen_ed_list = []
for e in elem:
  gen_ed_list.append(course_pattern.search(e.text).group(0))
print(gen_ed_list.index("WGSS 28200"))
additional.append(
  ["Introductory Level General Education Courses", 12, gen_ed_list[:187]]
)
additional.append(
  ["Advanced Level General Education Courses", 6, gen_ed_list[187:]]
)

for x in additional:
  all_tags.append({
    "tag_name": x[0],
    "credits": x[1],
    "course_list": x[2]
  })

json.dump(all_tags, f_ece)
f_ece.close()
driver.close()
