# Input: Void
# Output: a rotated image

import sys, os, shutil, zipfile, json, argparse, re

# Import Pillow:
from PIL import Image

# function definitions
def rotate(filename, finalDirectory):
	img = Image.open(filename)
	shutil.copy(filename, finalDirectory) # positiveTrainingDirectory/negative/test
	for x in range(5, 360, 5):
		img2 = img.rotate(x)
		extension = len(filename) - 4	# the number of characters minus the length of the extension
		truncated_filename = filename[:extension]	# the truncated name of the file
		saveName = truncated_filename + '_rotation_degree_' + str(x) + '.png'
		img2.save(saveName)
		shutil.move(saveName, finalDirectory)

# first pass positiveTrainingDirectory with positive split_count then negativeTrainingDirectory
def process(trainingDirectory, testDirectory, split_count):
	rootDir = '.'
	for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    		print('Found directory: %s' % dirName)
		count = 0
    	for fname in fileList:
        	print('\t%s' % fname)
		
		if count < split_count:
			rotate(fname, trainingDirectory)
			count += 1		
		else:
			print(fname)
			rotate(fname, testDirectory)
'''	
			with open('truth.json', 'w') as outfile:
			    json.dump({
			    "filename":filename,
			    "class": args.c,
			    "type": args.type,
			    "score": '-1' 
			     }, outfile)
'''
#	print('')


#print(args)

#workingDirectory = '/home/efwoods/watson/Watson-Precision-Agriculture/Preprocessing_and_Enrichment/Data/Flight 1/Spirea/Healthy

#savingDirectory = '/home/efwoods/watson/Watson-Precision-Agriculture/Preprocessing_and_Enrichment/Data/Flight 1/Spirea/Rotated_Cropped_Healthy_Spirea'

# walks through the folder of the current working directory, then each subfolder, then each file. 

#For the first for files, each file is rotated by 5 degrees and saved until the rotation completes a full rotation cycle of 360 degrees. 

#This results in 72 images including the original file. 

#These images are saved and moved to a new location before the new images are zipped.

#os.mkdir(args.sD)

# parse arguements
parser = argparse.ArgumentParser(description='Curate a set of data for Modeling and Validation')
parser.add_argument('--p', help='Directory to the POSITIVE examples', type=str, required=True)
parser.add_argument('--n', help='Directory to the NEGATIVE examples', type=str, required=True)
parser.add_argument('--s', help='SPLITS the data. Accepts an int between 0 and 100. This value indicates the percentage of images to be used as TRAINING images.', type=int, required=True)
parser.add_argument('--d', help='Final DESTINATION directory. Expected to be located in Modeling and Validation', type=str, required=True)
args = parser.parse_args()

# validate that user argument input is acceptable


positive_image_total = len(os.listdir(args.p))	# identify the total number of images in the directory
negative_image_total = len(os.listdir(args.n))
percent = float(args.s)/100 # calculate the percentage of images to be used as positive examples
positive_count = int(positive_image_total * percent) # the integer number of images that will be used as positive examples
negative_count = int(negative_image_total * percent)
if ((positive_count == 0) or (positive_count == positive_image_total) or (negative_count == 0) or (negative_count == negative_image_total)): # positive_count must be between 0 and the total number of images in the file to leave data for the test data
	print("Error incorrect split. Please choose a different split.")
	sys.exit(1) 	
else:
	# create a folder of processed data with three subfolders: negative examples, positive examples, test images made of negative and positive images
	locate = "/" # may need to make /Flight
	cwd = os.getcwd()
	positivePath = cwd[:-10] + args.p[3:]
	negativePath = cwd[:-10] + args.n[3:]
	basePath = cwd[:cwd.rfind("/")] + "/"
	
	positiveSaveDirectory = args.p[args.p.find(locate):args.p.rfind(locate)]
	positiveSaveDirectory = positiveSaveDirectory.replace("/", " ")
	positiveSaveDirectory = positiveSaveDirectory.replace(" ", "_")
	positiveSaveDirectory = positiveSaveDirectory[1:]
	
	parentDir = basePath + positiveSaveDirectory + "_classifier"
	os.mkdir(parentDir)
	os.chdir(parentDir)
	
	positiveSaveDirectory = parentDir + "/" + positiveSaveDirectory
	
	testSaveDirectory = positiveSaveDirectory + "_test"

	negativeSaveDirectory = args.n[args.n.find(locate):args.n.rfind(locate)]
	negativeSaveDirectory = negativeSaveDirectory.replace("/", " ")
	negativeSaveDirectory = negativeSaveDirectory.replace(" ", "_")
	negativeSaveDirectory = negativeSaveDirectory[1:]
	negativeSaveDirectory = parentDir + "/" + negativeSaveDirectory

#args.p[args.p.find(locate):args.p.rfind(locate)]

#	baseDirectory = args.p[:args.p.rfind(locate)]
#	baseDirectory[baseDirectory.find("/"):baseDirectory.rfind("/")]
#	temporary =  args.p[:args.p.rfind(locate)]
#
#	targetName = temporary[temporary.rfind(locate)+1:]
#	parentDirectory = baseDirectory + "/"+ targetName + "_processed" + "_" + str(percent) + "%split"
#	positiveTrainingDirectory = parentDirectory + "/PostiveTrainingData" + "_" + targetName
#	negativeTrainingDirectory = parentDirectory + "/NegativeTrainingData" + "_" + targetName
#	testingDirectory = parentDirectory + "/TestData" + "_" + targetName
	
#	os.mkdir(parentDirectory)
	os.mkdir(positiveSaveDirectory)
	os.mkdir(negativeSaveDirectory)
	os.mkdir(testSaveDirectory)

	os.chdir(positivePath)
	process(positiveSaveDirectory, testSaveDirectory, positive_count)
	os.chdir(negativePath)
	process(negativeSaveDirectory, testSaveDirectory, negative_count)
'''
	# zip folders for Modeling and Validation
	os.chdir(parentDir)
	src = parentDir

	print('Beginning Zipping')

	shutil.make_archive(positiveSaveDirectory, 'zip')

	print('Zipping Test')	
		
	shutil.make_archive(testSaveDirectory, 'zip')
	print('Beginning Zipping  Negative')
	shutil.make_archive(negativeSaveDirectory, 'zip')

	
	print('Completed zipping')
	src = parentDir
	dst = '/home/efwoods/Watson-Precision-Agriculture/Modeling_and_Validation/classifiers'
#	dst = args.d + "/"+ targetName + "_processed" + "_" + str(percent) + "%split"

	shutil.copytree(src, dst, symlinks=False, ignore=None)
	print('Completed copying tree')
	shutil.rmtree(src)
'''
	print('Rotate.py Complete, Meatbag')
	
#workingDirectory = args.p
#os.chdir(workingDirectory)	# move to the workingDirectory

#plt.show


