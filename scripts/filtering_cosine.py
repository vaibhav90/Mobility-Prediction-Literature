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

with open('cosine_similarity.txt') as f:
    data = json.load(f)

print(data)

cosine_similar = []

for i in range(len(data)):

    if data[i][1] > 350:

        print(data[i])




