#expects python delete_classifier.py classifier_id

import sys
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

response = visual_recognition.delete_classifier(classifier_id=sys.argv[1])
print(json.dumps(response, indent=2))
