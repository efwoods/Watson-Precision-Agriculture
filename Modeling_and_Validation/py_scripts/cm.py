'''

    The program generates the confusion_matrix from the parsed json file

    Example Use:

    python cm.py --watson_output "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/watson.json"
    --ground_truth "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/truth_labels.json"
     --class_num 0

'''


import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
from parser import parse
from sklearn.metrics import classification_report,confusion_matrix
import sys, argparse
from sklearn.metrics import confusion_matrix


def plotConfusionMatrix(y_test, y_pred,cmap=plt.cm.Blues):
    pred = []
    for i in watson_data:
        if(i > .5):
            pred.append(1)
        else:
            pred.append(0)
    # Compute confusion matrix
    cm = confusion_matrix(y_test, pred)

    plt.figure()
    plt.imshow(cm,cmap=cmap)#(cm, interpolation='nearest', cmap=cmap)
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse the Json')
    parser.add_argument('--watson_output', help='file name', type=str, required=True)
    parser.add_argument('--ground_truth', help='file name', type=str, required=True)
    parser.add_argument('--class_num', help='class number to use from json', type=int, required=True)

    args = parser.parse_args()

    parsed_data = parse(args.watson_output,args.ground_truth,args.class_num)
    watson_data = np.asarray(parsed_data[0])
    ground_truth = np.asarray(parsed_data[1])

    pred = []
    for i in watson_data:
        if(i > .5):
            pred.append(1)
        else:
            pred.append(0)

    print(confusion_matrix(watson_data,np.asarray(pred)))
    plotConfusionMatrix(watson_data,ground_truth)
