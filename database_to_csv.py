import json
import csv

with open("/Users/derekconnolly/Downloads/export.json", 'r') as jsonFile:
    data = json.load(jsonFile)

suggestions = data['suggestions']


for k, v in suggestions.items():
    print(v['Name'])

