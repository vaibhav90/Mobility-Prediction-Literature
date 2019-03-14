import re
import json

with open('significant_locations.txt', 'r') as f:
    temp = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
temp = [x.strip() for x in temp]

content = []

for i in range(len(temp)):
  if temp[i]:
    content.append(temp[i])

title = []
title.append(content[0])


for i in range(len(content)-2):

  if 'CITATIONS' in content[i] and content[i+1] != 'DOWNLOAD':
    title.append(content[i+1])

  if 'CITATIONS' in content[i] and content[i+1] == 'DOWNLOAD':
    title.append(content[i+2])

date = []
authors = []
venue = []
key_words = []
for i in range(len(content)):
  if re.match(r'.*([1-2][0-9]{3})', content[i][0:5]):
    date.append(content[i][0:5])
    authors.append(content[i+1])
    venue.append(content[i][5:])
    key_words.append([content[i+3], content[i+4], content[i+5]])

pattern = re.compile(r"\((\d+)\)")
citations = []
for i in range(len(content)):
  if "CITATIONS*" in content[i]:
    citations.append(pattern.findall(content[i]))

citations = [int(item) for sublist in citations for item in sublist]


merger_list = list(zip(title, date, venue, authors, key_words))

with open('significant_locations_db.txt', 'w') as f:
  json.dump(merger_list, f)
  f.close()