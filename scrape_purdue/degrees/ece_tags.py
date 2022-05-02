from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
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
all_tags[2]["course_list"] = ["ECE 47700", "ECE 49022", "ECE 41200", "ECE 49595"]
all_tags[4]["tag_name"] = "C Programming"
all_tags[4]["credits"] = 3
all_tags[6]["tag_name"] = "Math Option 1"
all_tags.pop(7)
additional = [
    ["Science Requirement", 4, ["PHYS 27200", "BIOL 11000", "BIOL 11100", "BIOL 12100", "BIOL 13500", "BIOL 13100", "CHM 11600", "CHM 12400", "PHYS 31000", "PHYS 32200", "PHYS 34200", "PHYS 34400"]],
]

# adding FYE requirements
url = 'https://catalog.purdue.edu/preview_program.php?catoid=10&poid=15989'
driver.get(url)
degree_name = driver.find_element(by=By.ID, value="acalog-page-title")
# get and filter the degrees
elem = driver.find_elements(by=By.CLASS_NAME, value='acalog-core')
tag_pattern = re.compile(r'(.+)\s(\(((\d+)(\-\d+)?)\scredits?\))\s?\n')
fye_tags = []
for e in elem:
    content = e.text
    # print(content)
    # examine and prune e.text
    search_out = tag_pattern.search(content)
    if search_out:
        tag_name = search_out.group(1)
        credits = int(search_out.group(4))
        course_list = list(set(course_pattern.findall(content)))
        tag_name = "FYE" + tag_name[14:]
        fye_tags.append([tag_name, credits, course_list])
fye_tags[-1][-1].extend(["COM 11400", "ENGL 10600", "ENGL 10800", "SCLA 10100"])
additional.extend(fye_tags)

# adding gen ed requirements
url = 'https://catalog.purdue.edu/preview_program.php?catoid=13&poid=16848'
# url = 'https://catalog.purdue.edu/preview_program.php?catoid=10&poid=13430'
driver.get(url)
# get and filter the degrees
elem = driver.find_elements(by=By.CLASS_NAME, value='acalog-course')
course_pattern = re.compile(r'[A-Z]+\s\d\d\d\d\d')
gen_ed_list = []
for e in elem:
    gen_ed_list.append(course_pattern.search(e.text).group(0))
print(gen_ed_list.index("WGSS 28200"))
additional.append(
    ["Introductory Level General Education Courses", 12, gen_ed_list[:gen_ed_list.index("WGSS 28200")]]
)
additional.append(
    ["Advanced Level General Education Courses", 6, gen_ed_list[gen_ed_list.index("WGSS 28200"):]]
)
all_adv = additional[-1][-1]
dept = set([a.split()[0] for a in all_adv])
dept_dict = dict()
for a in all_adv:
    if a.split()[0] in dept_dict and len(dept_dict[a.split()[0]]) < 5:
        dept_dict[a.split()[0]].append(a)
    elif a.split()[0] not in dept_dict:
        dept_dict[a.split()[0]] = [a]
additional[-1][-1] = [b for a in dept_dict.values() for b in a]

for x in additional:
    all_tags.append({
        "tag_name": x[0],
        "credits": x[1],
        "course_list": x[2]
    })

json.dump(all_tags, f_ece)
f_ece.close()
driver.close()
