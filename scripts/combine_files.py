import json
import csv

with open('mobility_prediction_db.txt', 'r') as f:
  mobility_prediction = json.load(f)
  f.close()

with open('limits_predictabilitys_db.txt', 'r') as f:
  limits_predictability = json.load(f)
  f.close()

with open('link_prediction_db.txt', 'r') as f:
  link_prediction = json.load(f)
  f.close()

with open('next_place_prediction_using_MMC_db.txt', 'r') as f:
  next_place = json.load(f)
  f.close()

with open('significant_locations_db.txt', 'r') as f:
  significant_locations = json.load(f)
  f.close()

print(len(mobility_prediction))
print(len(limits_predictability))
print(len(link_prediction))
print(len(next_place))
print(len(significant_locations))

all_papers = mobility_prediction
all_papers = all_papers + limits_predictability + link_prediction + next_place + significant_locations

print(len(all_papers))

with open("output_check.csv", 'w') as resultFile:
  wr = csv.writer(resultFile, dialect='excel')
  wr.writerows(all_papers)
  resultFile.close()