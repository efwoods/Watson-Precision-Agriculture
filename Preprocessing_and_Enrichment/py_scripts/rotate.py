# Input: Void
# Output: a rotated image

import sys, os, shutil, zipfile

# Import Pillow:
from PIL import Image

workingDirectory = '/home/efwoods/watson/Watson-Precision-Agriculture/Preprocessing_and_Enrichment/Data/Flight 1/Spirea/Low Water Stress'

savingDirectory = '/home/efwoods/watson/Watson-Precision-Agriculture/Preprocessing_and_Enrichment/Data/Flight 1/Spirea/Rotated_Low_Water_Stress'

# walks through the folder of the current working directory, then each subfolder, then each file. 

#For the first for files, each file is rotated by 5 degrees and saved until the rotation completes a full rotation cycle of 360 degrees. 

#This results in 72 images including the original file. 

#These images are saved and moved to a new location before the new images are zipped.
count = 0
os.mkdir(savingDirectory)
os.chdir(workingDirectory)
for folderName, subfolders, filenames in os.walk(workingDirectory):
	print('The current folder is ' + folderName)

	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': ' + filename)
		number_of_images = len(os.listdir(workingDirectory)) - 1
		if count < number_of_images:
			count += 1
			img = Image.open(filename)
			for x in range(5, 360, 5):
				img2 = img.rotate(x, expand=True)
				extension = len(filename) - 4	# the number of characters minus the length of the extension
				truncated_filename = filename[:extension]	# the truncated name of the file
				saveName = truncated_filename + '_rotation_degree_' + str(x) + '.png'
				img2.save(saveName)
				shutil.move(saveName, savingDirectory)
			shutil.copy(filename, savingDirectory)
	print('')
