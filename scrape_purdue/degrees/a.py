import pickle

ece = open("ece_tags.pickle", "rb")
tags = pickle.load(ece)
print(tags[-2:])
print(len(tags))