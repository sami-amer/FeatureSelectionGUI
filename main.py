# import sklearn
import csv
import numpy as np
import pandas 

def load_labels(f):
    labels = []
    length = 0
    with open(f, "r") as f:
        for line in f:
            length += 1
            line = line.strip("\n")
            labels.append(float(line))
    return labels, length


def load_features(f):
    features = []
    length = 0
    with open(f, "r") as f:
        for line in f:
            line = line.split(",")
            line[-1] = line[-1].strip("\n")
            featuresLength = len(line)
            for feature in range(featuresLength):
                features.append([line[feature]])
            break
        for line in f:
            length += 1
            line = line.split(",")
            line[-1] = line[-1].strip("\n")
            for feature in range(featuresLength):
                features[feature].append(line[feature])
    return features, length

def run_ccm(features,labels):
    '''
    epsilon set to 0.1 until further notice
    '''
    type_Y = 'binary'
    num_features = len(features)
    epsilon = 0.1
    return 


if __name__ == "__main__":
    # print(load_labels("resources/wellness_nonverbal_condition_lable.csv")[0])
    # print(load_features("resources/wellness_nonverbal_features.csv")[0][0])
    pass
