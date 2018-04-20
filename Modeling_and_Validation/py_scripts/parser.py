'''

    The program parses through a json file, the file name, the class, the type, the classification score


    The Parse file returns a array:

    Example Json Input (one line):
    {"score": "0.863", "type": "test", "class": "0", "filename": "12_Flight 1_Spirea_Healthy.png"}
    #score is from watson

    Example Output:
    Array:        0          |        1        |
                0.863                 0
                <score>            <class>

'''

import json
import numpy as np
import sys, argparse
import os



def parse(watson_output, ground_truth):

    #will return these
    test_vector = []
    truth_vector = []

    with open(ground_truth,'r') as f:
        data = json.load(f)

    with open(watson_output,'r') as f:
        watson = json.load(f)

    d = {}#dictionary for files
    for entry in range(len(data)):
        d[data[entry]['filename']] = data[entry]['class']


    files = []#files used to train
    for entry in range(len(watson['images'])):
        files.append(os.path.basename(watson['images'][entry]['image']))
        truth_vector.append( float(watson['images'][entry]['classifiers'][0]['classes'][0]["score"]))

    for f in files:
        test_vector.append(float(d[f]));

    #Check if u desire, Note: Should be assert statement
    #print(len(test_vector))
    #print(len(truth_vector))

    return [test_vector,truth_vector]



# if __name__ == '__main__':
#
#     parser = argparse.ArgumentParser(description='Parse the Json')
#     parser.add_argument('--file', help='file name', type=str, required=True)
#
#     args = parser.parse_args()
#
#     info_list = parse(args.file)
#     print(info_list)
