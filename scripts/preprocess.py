import json
import numpy as np
import matplotlib.pyplot as plt
import re
import json


with open('human_mobility_complete.txt') as f:
    data = json.load(f)


article_clean = []

for i in range(len(data)):

    temp = data[i][0].strip('" .*-/')

    article_clean.append(temp)


[r.pop(0) for r in data]

x = np.array(data)
y = np.array(article_clean)

cleaned_complete_human_mobility = np.c_[y,x].tolist()


with open('cleaned_human_mobility_complete.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(cleaned_complete_human_mobility, outfile)


