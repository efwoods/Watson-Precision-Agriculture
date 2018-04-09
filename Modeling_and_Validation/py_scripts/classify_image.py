#expects python classify_image.py image

import sys
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open(sys.argv[1], 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        parameters=json.dumps({
            'owners': ['me'],#, 'IBM'], 
			'threshold': 0.0,
#			"classifier_id": "high_stress_1739667928"
        }))
print(json.dumps(classes, indent=2))
