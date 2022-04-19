# import pickle
# import json

# with open("ece_tags.pickle", "rb") as f:
#   ece = pickle.load(f)
# for a in ece:
#   a["course_list"] = list(a["course_list"])
# with open("ece_tags.json", "w") as f:
#   json.dump(ece, f)

import json
with open("ece_tags.json", "w") as f:
  ece = json.load(f)
