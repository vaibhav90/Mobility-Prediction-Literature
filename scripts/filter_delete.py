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


with open('filtered_human_mobility.txt') as f:
    data = json.load(f)

temp_article = []

for i in range(len(data)):

    temp_article.append(data[i][0])

print(len(data))


my_string = "human moblity prediction spatiotemporal next place future location point-of-interest hotspot forecasting modelling mobility behaviors traffic trajectory mobile phone"

p = []

filter_thresh_45 = []

for i in range(len(temp_article)):

    jarowinkler = JaroWinkler()

    sim = jarowinkler.similarity(my_string, temp_article[i])

    if sim > 0.45:

        filter_thresh_45.append(data[i])


normalized_levenshtein = NormalizedLevenshtein()


filter_normalized_levenshtein = []

for i in range(len(filter_thresh_45)):

    sim = normalized_levenshtein.distance(my_string, filter_thresh_45[i][0])

    if sim >= 0.7:

        filter_normalized_levenshtein.append(filter_thresh_45[i])


with open('filtered_levenshtein_human_mobility.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(filter_normalized_levenshtein, outfile)
    outfile.close()



with open("filtered_levenshtein_mobility_prediction.csv",'w') as resultFile:

    wr = csv.writer(resultFile, dialect='excel')

    wr.writerows(filter_normalized_levenshtein)

    resultFile.close()
