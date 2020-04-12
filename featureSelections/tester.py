import pandas as pd 
import tensorflow as tf
import ccm

features = pd.read_csv(r'resources\wellness_nonverbal_features.csv')
labels = pd.read_csv(r'resources\wellness_nonverbal_condition_lable.csv')

#ccm needs: X,Y, num of features, type_y, epsilon
X = features
print(labels)
print(X)

