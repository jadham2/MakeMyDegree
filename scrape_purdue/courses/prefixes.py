import pickle
import re

f_course = open("all_courses.pickle", "rb")
f_prefix_txt = open("prefixes.txt", "w")
f_prefix_pkl = open("prefixes.pickle", "wb")

courses = pickle.load(f_course)
all_prefixes = list(sorted(list(set([re.search(r'[A-Z]+', a["course_code"]).group(0) for a in courses]))))

for x in all_prefixes:
  print(x)
  f_prefix_txt.write(f'{x}\n')
pickle.dump(all_prefixes, f_prefix_pkl)

f_course.close()
f_prefix_pkl.close()
f_prefix_txt.close()