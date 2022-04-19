# import pickle
# import json

# with open("all_courses.pickle", "rb") as f:
#   courses = pickle.load(f)
# for a in courses:
#   a["terms"] = list(a["terms"])
# with open("all_courses.json", "w") as f:
#   json.dump(courses, f)

import json

with open("all_courses.json", "r") as f:
  courses = json.load(f)
with open("../degrees/ece_tags.json", "r") as f:
  ece = json.load(f)
# print(courses[:10])
# print(ece[:10])
years = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025']
model_fixtures = []
for i, a_course in enumerate(courses):
  terms = []
  for x in a_course["terms"]:
    if 'fall' in x.lower():
      terms.extend(['Fa'+y for y in years])
    elif 'spring' in x.lower():
      terms.extend(['Sp'+y for y in years])
    elif 'summer' in x.lower():
      terms.extend(['Sm'+y for y in years])
  a_course["terms"] = terms
  model_courses = {
    "model": "MakeMyDegree.Course",
    "pk": i + 1,
    "fields": a_course
  }
  model_fixtures.append(model_courses)
with open("model_all_courses.json", "w") as f:
  json.dump(model_fixtures, f)