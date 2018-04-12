#1 indicates healthy
import json
with open('truth_labels.json', 'w+') as outfile:
    json.dump({
    "filename": "12_Flight 1_Spirea_Healthy.png",
    "class":"Healthy"
     }, outfile)
