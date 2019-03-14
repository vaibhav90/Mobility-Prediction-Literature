import json
import numpy as np
import matplotlib.pyplot as plt
import re
import json
import csv

with open('cleaned_human_mobility_complete.txt') as f:
    data = json.load(f)


clean_set = []

def unique(dirty_data):

    seen = []

    for item in dirty_data:

        compare = item[0]

        if compare not in seen:

            seen.append(compare)

            clean_set.append(item)

unique(data)


#with open('filtered_human_mobility.txt', 'w', encoding = "ISO-8859-1") as outfile:
#    json.dump(clean_set, outfile)
#    outfile.close()


with open("filtered_mobility_prediction.csv",'w') as resultFile:

    wr = csv.writer(resultFile, dialect='excel')

    wr.writerows(clean_set)

    resultFile.close()
