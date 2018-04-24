#expects python classify_image.py image

import sys
import json
from watson_developer_cloud import VisualRecognitionV3

free_key = '988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
IBM_key = '2dc79bad5c8e2677012abe8fbff37d296cec070c'

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key= IBM_key)

with open(sys.argv[1], 'rb') as images_file:#, open(sys.argv[2], 'rb') as img2:
    classes = visual_recognition.classify(
        images_file, #img2,
        parameters=json.dumps({
			"classifier_id": "High_Water_Stress_Classifier_210568720",
      		        'owners': ['me'],#, 'IBM'], 
			'threshold': 0.0,
        }))
print(json.dumps(classes, indent=2))

#with open('./fruitbowl.jpg', 'rb') as images_file:
