# runs as a standalone file;
# Outputs a list of all the classifiers the account has created 

import json, argparse
from watson_developer_cloud import VisualRecognitionV3

parser = argparse.ArgumentParser(description='Send Data for Modeling and Validation')
parser.add_argument('--k', help='1 to use the IBM account', type=int, required=True)
args = parser.parse_args()

free_key = '988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
IBM_key = '2dc79bad5c8e2677012abe8fbff37d296cec070c'
if (args.k == 1):
	key = IBM_key
else:
	key = free_key


visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key= key)

classifiers = visual_recognition.list_classifiers(verbose=True)
print(json.dumps(classifiers, indent=2))
