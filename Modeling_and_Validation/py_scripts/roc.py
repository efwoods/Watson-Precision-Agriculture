'''

    The program generates the roc from the parsed json file

    Example Use:

    roc.py --watson_output "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/watson.json"
    --ground_truth "../classifiers/Flight_1_Cornus_Obliqua_High_Water_Stress_classifier/truth_labels.json"
    --numclasses 1


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


def calcRocMulti(n_classes,y_test, y_score):
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    return [fpr,tpr,roc_auc]

def calcRocSingle(y_test, y_score):
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)

    return [fpr,tpr,roc_auc]


#plot the data
def plotRoc(info,output):

    fpr = info[0]
    tpr = info[1]
    roc_auc = info[2]

    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='Watson ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--',label='Random ROC curve (area = %0.2f)' % (.50))
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for High Water Stress Detection')
    plt.legend(loc="lower right")
    plt.savefig(output)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse the Json')
    parser.add_argument('--watson_output', help='file name', type=str, required=True)
    parser.add_argument('--ground_truth', help='file name', type=str, required=True)
    parser.add_argument('--class_num', help='file name', type=int, required=True)
    parser.add_argument('--output', help='output', type=str, required=True)

    args = parser.parse_args()

    parsed_data = parse(args.watson_output,args.ground_truth, args.class_num)
    watson_data = np.asarray(parsed_data[0])
    ground_truth = np.asarray(parsed_data[1])

    data = calcRocSingle(ground_truth,watson_data)

    plotRoc(data,args.output)
