import sys
import os
import json
import argparse
from watson_developer_cloud import VisualRecognitionV3

parser = argparse.ArgumentParser(description='Send Data for Modeling and Validation')
parser.add_argument('--p1', help='Directory to the POSITIVE examples', type=str, required=True)
parser.add_argument('--n', help='Directory to the NEGATIVE examples', type=str, required=True)
parser.add_argument('--name', help='Name of the Classifier', type=str, required=True)
args = parser.parse_args()

free_key = '988d558c4a7e45a98f2aa9f1d52a66d5be30287d'
IBM_key = '2dc79bad5c8e2677012abe8fbff37d296cec070c'

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key= IBM_key)

with open(args.p1, 'rb') as High_Water_Stress, open(args.n, 'rb') as negative:
    model = visual_recognition.create_classifier(
        args.name,
	High_Water_Stress_positive_examples = High_Water_Stress,
        negative_examples = negative)
print(json.dumps(model, indent=2))
