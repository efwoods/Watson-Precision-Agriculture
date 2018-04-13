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

def parse(p_file):

    with open(p_file,'r') as f:
        data = json.load(f)

    test_vector = []
    truth_vector = []
    for i in data:
        test_vector.append(float(i["score"]))
        truth_vector.append(int(i["class"]))

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
