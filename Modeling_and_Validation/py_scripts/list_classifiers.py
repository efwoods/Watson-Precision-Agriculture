# runs as a standalone file;
# Outputs a list of all the classifiers the account has created 

import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

classifiers = visual_recognition.list_classifiers(verbose=True)
print(json.dumps(classifiers, indent=2))