import sys
import os
import json
import argparse
from watson_developer_cloud import VisualRecognitionV3

parser = argparse.ArgumentParser(description='Send Data for Modeling and Validation')
parser.add_argument('--p1', help='Directory to the POSITIVE examples', type=str, required=True)
parser.add_argument('--p2', help='Directory to the POSITIVE examples', type=str, required=True)
parser.add_argument('--p3', help='Directory to the POSITIVE examples', type=str, required=True)
parser.add_argument('--n', help='Directory to the NEGATIVE examples', type=str, required=True)
parser.add_argument('--name', help='Name of the Classifier', type=str, required=True)
args = parser.parse_args()

visual_recognition = VisualRecognitionV3(
    '2016-05-20',
    api_key='988d558c4a7e45a98f2aa9f1d52a66d5be30287d')

with open(args.p1, 'rb') as Cornus_Obliqua_High_Water_Stress, open(args.p2, 'rb') as Hydrangea_Quercifolia_High_Water_Stress, open(args.p3, 'rb') as Spirea_High_Water_Stress, open(args.n, 'rb') as negative:
    model = visual_recognition.create_classifier(
        args.name,
        Cornus_Obliqua_High_Water_Stress_positive_examples = Cornus_Obliqua_High_Water_Stress,
	Hydrangea_Quercifolia_High_Water_Stress_positive_examples = Hydrangea_Quercifolia_High_Water_Stress,
	Spirea_High_Water_Stress_positive_examples = Spirea_High_Water_Stress,
        negative_examples = negative)
print(json.dumps(model, indent=2))
