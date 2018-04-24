#expects python delete_classifier.py classifier_id

import sys
import json
from watson_developer_cloud import VisualRecognitionV3

free_key = '988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
IBM_key = '2dc79bad5c8e2677012abe8fbff37d296cec070c'

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key=IBM_key)

response = visual_recognition.delete_classifier(classifier_id=sys.argv[1])
print(json.dumps(response, indent=2))
