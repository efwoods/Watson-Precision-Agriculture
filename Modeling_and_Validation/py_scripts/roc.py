'''

    The program generates the roc from the parsed json file


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

#Step 1,
# get data from Json

#Step 2
# Compute ROC curve and ROC area for each class
# y_score = parsed from watson
# y_test = a file to be read in
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

    fpr["healthy"], tpr["healthy"], _ = roc_curve(y_test, y_score)
    roc_auc["healthy"] = auc(fpr["healthy"], tpr["healthy"])

    print(fpr)
    print(tpr)
    print(roc_auc)

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    return [fpr,tpr,roc_auc]
#Step 3
#plot the data
def plotRoc(info):

    fpr = info[0]
    tpr = info[1]
    roc_auc = info[2]

    plt.figure()
    lw = 2
    plt.plot(fpr["healthy"], tpr["healthy"], color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc["healthy"])
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Test Example')
    plt.legend(loc="lower right")
    plt.show()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse the Json')
    parser.add_argument('--watson_output', help='file name', type=str, required=True)
    parser.add_argument('--ground_truth', help='file name', type=str, required=True)
    parser.add_argument('--numclasses', help='file name', type=int, required=True)

    args = parser.parse_args()

    parsed_data = parse(args.watson_output,args.ground_truth)
    watson_data = np.asarray(parsed_data[0])
    ground_truth = np.asarray(parsed_data[1])
    #data = calcRocMulti(args.numclasses,ground_truth,watson_data)
    print(watson_data)
    print(ground_truth)
    data = calcRocSingle(ground_truth,watson_data)
    # pred = []
    # for i in watson_data:
    #     if(i > .5):
    #         pred.append(1)
    #     else:
    #         pred.append(0)
    #
    # print(confusion_matrix(ground_truth,pred))
    #plotRoc(data)
