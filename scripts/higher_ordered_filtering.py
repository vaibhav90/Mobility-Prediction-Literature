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


qgram = QGram(2)

cum_score = []

for i in range(len(data)):

    temp = 0

    for j in range(len(data)):

        sim = qgram.distance(data[i][0], data[j][0])

        temp = temp+sim

    cum_score.append([i, temp])
    print(i)

with open('sim_score.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(cum_score, outfile)
    outfile.close()
