# import sklearn
import csv
import numpy as np
import pandas as pd

def load_labels(f):
    labels = pd.read_csv(f)
    return labels, len(labels)


def load_features(f):
    features= pd.read_csv(f)
    return features,len(features)

def run_ccm(features,labels):
    '''
    epsilon set to 0.1 until further notice
    '''
    type_Y = 'binary'
    num_features = len(features)
    epsilon = 0.1
    return None


if __name__ == "__main__":
    # print(load_labels("resources/wellness_nonverbal_condition_lable.csv")[0])
    # print(load_features("resources/wellness_nonverbal_features.csv")[0][0])
    pass
