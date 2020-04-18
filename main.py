# import sklearn
import csv
import numpy as np
import pandas as pd
import myTtest

def load_labels(f):
    labels = pd.read_csv(f)
    labels = labels.to_numpy()
    labels = labels.reshape((labels.shape[0],))
    return labels, len(labels)


def load_features(f):
    features= pd.read_csv(f)
    features = features.to_numpy()
    return features,len(features)


def runTtest(features,labels,runs,folds,testSize,featureSel): # add features
    return myTtest.tTest(features,labels,runs,folds,testSize,featureSel)


if __name__ == "__main__":
    # print(load_labels("resources/wellness_nonverbal_condition_lable.csv")[0])
    # print(load_features("resources/wellness_nonverbal_features.csv")[0][0])
    pass
