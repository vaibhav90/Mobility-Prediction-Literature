import json
import numpy as np
import matplotlib.pyplot as plt
import re
import json
from similarity.jarowinkler import JaroWinkler
from similarity.qgram import QGram
from similarity.cosine import Cosine
from similarity.ngram import NGram
from similarity.levenshtein import Levenshtein
from similarity.normalized_levenshtein import NormalizedLevenshtein
import csv
from similarity.qgram import QGram


with open('filtered_levenshtein_human_mobility.txt') as f:
    data = json.load(f)

with open('sim_score.txt') as f:
    sim_score = json.load(f)


d = len(sim_score)
c = 0

qgram_filtered = []

for i in range(len(sim_score)):

    #print(i, sim_score[i][1]/d)

    if sim_score[i][1]/d < 120:

        #c+=1
        #print(i+1, sim_score[i][1]/d)

        qgram_filtered.append(data[i])



with open('qgram_human_mobility.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(qgram_filtered, outfile)
    outfile.close()



with open("qgram_human_mobility.csv",'w') as resultFile:

    wr = csv.writer(resultFile, dialect='excel')

    wr.writerows(qgram_filtered)

    resultFile.close()
