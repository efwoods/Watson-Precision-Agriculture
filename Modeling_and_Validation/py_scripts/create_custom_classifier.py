import sys
import os
import json
from watson_developer_cloud import VisualRecognitionV3

#sys.path.insert(0, '~/watson/Watson-Precision-Agriculture/')
#sys.path.insert(1, '/home/efwoods/watson/Watson-Precision-Agriculture')
#positive = high_stress_snips_IMG_7575_non_rotated.zip
#negative = non_high_stress_snips_IMG_7575_initial_negatives.zip
#zipfile = sys.argv[1]
#print(zipfile.slpittext()[0])
#print(zipfile)
#print(positive)
#print(negative)
'''with open('api_key') as rawkey:
    key=rawkey.readlines().strip()
print(key)
'''

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open(sys.argv[2], 'rb') as positive, open(sys.argv[3], 'rb') as negative:
    model = visual_recognition.create_classifier(
        sys.argv[1],
        positive_positive_examples=positive,
        negative_examples=negative)
print(json.dumps(model, indent=2))

