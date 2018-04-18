#!/bin/python

# 1 indicates positive training class
import json, argparse, os

def find_truth():
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
		print('Found directory: %s' % dirName)
		for fname in fileList:
			print('\t%s' % fname)
			if ((fname.find("Health") >= 0) or (fname.find("None")>=0)):
				classifier = 0
			else:
				classifier = 1

			with open('mixed_truth_labels.json', 'a') as outfile:
			    json.dump({
			    "filename": fname,
			    "class": classifier,
			     }, outfile)

parser = argparse.ArgumentParser(description='Parse a Directory and Create a JSON output of ground truth')
parser.add_argument('--d', help='Directory of the test images', type=str, required=True)
#parser.add_argument('--n', help='Directory to the NEGATIVE examples', type=str, required=True)
#parser.add_argument('--s', help='SPLITS the data. Accepts an int between 0 and 100. This value indicates the percentage of images to be used as TRAINING images.', type=int, required=True)
#parser.add_argument('--d', help='Final DESTINATION directory. Expected to be located in Modeling and Validation', type=str, required=True)
args = parser.parse_args()
os.chdir(args.d)
find_truth()
