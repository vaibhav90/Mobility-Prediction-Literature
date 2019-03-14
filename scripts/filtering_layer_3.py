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

with open('qgram_human_mobility.txt') as f:
    data = json.load(f)

cosine = Cosine(2)

profiles = []

for i in range(len(data)):

    temp = data[i][0].strip('"')

    profiles.append(cosine.get_profile(temp))

for i in range(len(profiles)):

    print(profiles[i])


profile_sim = []

for i in range(len(profiles)):

    sim_score = 0

    for j in range(len(profiles)):

        temp = cosine.similarity_profiles(profiles[i], profiles[j])

        sim_score = sim_score + temp

    profile_sim.append([i, sim_score])

    print(i)



with open('cosine_similarity.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(profile_sim, outfile)
    outfile.close()


