import sys
import os
import json
import argparse
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

with open(args.p1, 'rb') as High_Water_Stress, open(args.p2, 'rb') as Low_Water_Stress, open(args.p3, 'rb') as Low_Phosphorus_Fertilizer, open(args.n, 'rb') as negative:
    model = visual_recognition.create_classifier(
        args.name,
        High_Water_Stress_positive_examples = High_Water_Stress,
	Low_Water_Stress_positive_examples = Low_Water_Stress,
	Low_Phosphorus_Fertilizer_positive_examples = Low_Phosphorus_Fertilizer,
        negative_examples = negative)
print(json.dumps(model, indent=2))
