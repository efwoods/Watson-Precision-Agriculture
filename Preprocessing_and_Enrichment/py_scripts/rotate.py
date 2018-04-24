import sys, os, shutil, zipfile, json, argparse, re

#from truth.py import find_truth
# Import Pillow:
from PIL import Image

# function definitions
def rotate(filename, finalDirectory):
	img = Image.open(filename)
	shutil.copy(filename, finalDirectory) # positiveTrainingDirectory/negative/test
	for x in range(45, 360, 45):
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

# walks through the folder of the current working directory, then each subfolder, then each file. 

#For the first for files, each file is rotated by 45 degrees and saved until the rotation completes a full rotation cycle of 360 degrees. 

# parse arguements
parser = argparse.ArgumentParser(description='Curate a set of data for Modeling and Validation')
parser.add_argument('--positive', help='Directory to the examples you want Watson to recognize\n\n', type=str, required=True)
parser.add_argument('--negative', help='Directory to the examples Watson should not recognize\n', type=str, required=True)
parser.add_argument('--split', help='SPLITS the data. Accepts an integer between 0 and 100. This value indicates the percentage of images to be used as TRAINING images. The remaining will be rotated and sorted as TEST images\n', type=int, required=True)
parser.add_argument('--destination', help='Final DESTINATION directory. The final destination is expected to be located in Modeling and Validation\n', type=str, required=True)
args = parser.parse_args()

# validate that user argument input is acceptable


positive_image_total = len(os.listdir(args.p))	# identify the total number of images in the directory

if(args.n):	
	negative_image_total = len(os.listdir(args.n))

percent = float(args.s)/100 # calculate the percentage of images to be used as positive examples
positive_count = int(positive_image_total * percent) # the integer number of images that will be used as positive examples

if(args.n):
	negative_count = int(negative_image_total * percent)

	if ((positive_count == 0) or (positive_count == positive_image_total) or (negative_count == 0) or (negative_count == negative_image_total)): # positive_count must be between 0 and the total number of images in the file to leave data for the test data

###
		print("Error incorrect split. Please choose a different split.")
		sys.exit(1) 	
	else:
		# create a folder of processed data with three subfolders: negative examples, positive examples, test images made of negative and positive images
		locate = "/" # may need to make /Flight
		cwd = os.getcwd()
		positivePath = cwd[:-10] + args.p[3:]
		if(args.n):
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

		if(args.n):
			negativeSaveDirectory = args.n[args.n.find(locate):args.n.rfind(locate)]
			negativeSaveDirectory = negativeSaveDirectory.replace("/", " ")
			negativeSaveDirectory = negativeSaveDirectory.replace(" ", "_")
			negativeSaveDirectory = negativeSaveDirectory[1:]
			negativeSaveDirectory = parentDir + "/" + negativeSaveDirectory

		os.mkdir(positiveSaveDirectory)
		if(args.n):
			os.mkdir(negativeSaveDirectory)
		os.mkdir(testSaveDirectory)

		os.chdir(positivePath)
		process(positiveSaveDirectory, testSaveDirectory, positive_count)

		if(args.n):	
			os.chdir(negativePath)
			process(negativeSaveDirectory, testSaveDirectory, negative_count)

		# create ground_truth json file 
		print(testSaveDirectory)
	
else:
	if ((positive_count == 0) or (positive_count == positive_image_total)): # positive_count must be between 0 and the total number of images in the file to leave data for the test data

###
		print("Error incorrect split. Please choose a different split.")
		sys.exit(1) 	
	else:
		# create a folder of processed data with three subfolders: negative examples, positive examples, test images made of negative and positive images
		locate = "/" # may need to make /Flight
		cwd = os.getcwd()
		positivePath = cwd[:-10] + args.p[3:]
		if(args.n):
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

		if(args.n):
			negativeSaveDirectory = args.n[args.n.find(locate):args.n.rfind(locate)]
			negativeSaveDirectory = negativeSaveDirectory.replace("/", " ")
			negativeSaveDirectory = negativeSaveDirectory.replace(" ", "_")
			negativeSaveDirectory = negativeSaveDirectory[1:]
			negativeSaveDirectory = parentDir + "/" + negativeSaveDirectory

		os.mkdir(positiveSaveDirectory)
		if(args.n):
			os.mkdir(negativeSaveDirectory)
		os.mkdir(testSaveDirectory)

		os.chdir(positivePath)
		process(positiveSaveDirectory, testSaveDirectory, positive_count)

		if(args.n):	
			os.chdir(negativePath)
			process(negativeSaveDirectory, testSaveDirectory, negative_count)

		# create ground_truth json file 
		print(testSaveDirectory)

print('Test Save Dir:')
print(testSaveDirectory)
print('Positive Save Dir:')
print(positiveSaveDirectory)
if(args.n):
	print('Negative Save Dir:')
	print(negativeSaveDirectory)

