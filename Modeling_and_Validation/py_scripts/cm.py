'''

    The program generates the confusion_matrix from the parsed json file

    Example Use:

    python cm.py --watson_output "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/watson.json"
    --ground_truth "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/truth_labels.json"
     --class_num 0

'''


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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


def plotConfusionMatrix(watson_data,truth_data,threshold,output,cmap=plt.cm.Blues):
    pred = []
    for i in watson_data:
        if(i > threshold):
            pred.append(1)
        else:
            pred.append(0)
    # Compute confusion matrix
    print(pred)
    cm = confusion_matrix(truth_data, pred,)

    print(confusion_matrix(truth_data,np.asarray(pred)))

    plt.figure()
    ax = sns.heatmap(cm,annot=True,cmap=cmap,cbar=False,xticklabels =["Predicted Positive", "Predicted Negative" ], yticklabels=["Actual Positive", "Actual Negative" ])#(cm, interpolation='nearest', cmap=cmap)
    ax.texts[0].set_text("FP: " + ax.texts[0].get_text())
    ax.texts[1].set_text("TN: " + ax.texts[1].get_text())
    ax.texts[2].set_text("TP: " + ax.texts[2].get_text())
    ax.texts[3].set_text("FN: " + ax.texts[3].get_text())
    plt.title('Confusion Matrix for High Water Stress Detection')
    #plt.tight_layout()

    #plt.show()
    plt.savefig(output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse the Json')
    parser.add_argument('--watson_output', help='file name', type=str, required=True)
    parser.add_argument('--ground_truth', help='file name', type=str, required=True)
    parser.add_argument('--class_num', help='class number to use from json', type=int, required=True)
    parser.add_argument('--threshold', help='threshhold for prediction', type=float, required=True)
    parser.add_argument('--output', help='output', type=str, required=True)


    args = parser.parse_args()

    parsed_data = parse(args.watson_output,args.ground_truth,args.class_num)
    watson_data = np.asarray(parsed_data[0])
    ground_truth = np.asarray(parsed_data[1])


    plotConfusionMatrix(watson_data,ground_truth,args.threshold,args.output)
