import pandas as pd
import sqlite3
import os
import csv
import json

with open('data/mobility_prediction.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []

for i in range(len(your_list)):

    if(your_list[i][0] != ''):

        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


mobility_prediction = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/mobility_modelling.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []

for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


mobility_modelling = list(zip(article, authors, venue, year, impact, new_velocity, link))


with open('data/predictability_limits.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


predictability_limits = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/trajectory_prediction.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


trajectory_prediction = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/future_locations.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


future_locations = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/next_location.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []



for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])


authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


next_location = list(zip(article, authors, venue, year, impact, new_velocity, link))


with open('data/next_poi.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []



for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')

new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


next_poi = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/next_trajectory.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []



for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')

new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


next_trajectory = list(zip(article, authors, venue, year, impact, new_velocity, link))


with open('data/next_visit.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


next_visit = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/prediction_model.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


prediction_model = list(zip(article, authors, venue, year, impact, new_velocity, link))




with open('data/spatiotemporal_pred.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])


authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


spatiotemporal_pred = list(zip(article, authors, venue, year, impact, new_velocity, link))



with open('data/spatio-temporal_traj.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])



authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')


spatiotemporal_traj = list(zip(article, authors, venue, year, impact, new_velocity, link))


with open('data/gis_mobility.csv', 'r', encoding = "ISO-8859-1") as f:
    reader = csv.reader(f)
    next(reader, None)
    your_list = list(reader)


article = []
authors = []
venue = []
year =  []
impact = []
velocity = []
link = []


for i in range(len(your_list)):

    if(your_list[i][0] != ''):


        article.append(your_list[i][0])

        venue.append(your_list[i][2])

        year.append(your_list[i][3])

        impact.append(your_list[i][4])

        velocity.append(your_list[i][5])

        link.append(your_list[i][6])


authors = [[] * 1 for i in range(len(article))]

j = -1

for i in range(len(your_list)):

    if your_list[i][0] != '':

        j+=1

        authors[j].append(your_list[i][1])

    else:

        authors[j].append(your_list[i][1])


new_impact = []

for i in range(len(impact)):

    if impact[i] != '':

        new_impact.append(impact[i])

    else:

        new_impact.append('0')


new_velocity = []

for i in range(len(velocity)):

    if velocity[i] != '':

        new_velocity.append(velocity[i])

    else:

        new_velocity.append('0')



gis_mobility = list(zip(article, authors, venue, year, impact, new_velocity, link))



human_mobility_complete = mobility_prediction + mobility_modelling + trajectory_prediction + predictability_limits + future_locations + next_location + next_poi + next_trajectory + next_visit + prediction_model + spatiotemporal_pred + spatiotemporal_traj + gis_mobility



print(len(human_mobility_complete))



with open('human_mobility_complete_temp.txt', 'w', encoding = "ISO-8859-1") as outfile:
    json.dump(human_mobility_complete, outfile)
