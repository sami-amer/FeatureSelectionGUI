import pandas as pd 
import tensorflow as tf
import ccm
import numpy as np

features = pd.read_csv(r'resources\wellness_nonverbal_features.csv')
labels = pd.read_csv(r'resources\wellness_nonverbal_condition_lable.csv')

#ccm needs: X,Y, num of features, type_y, epsilon
X = features.to_numpy() # makes the data frame into a numpy array
Y = labels.to_numpy()
numFeatures = X.shape[1] # gets the number of columns in X
type_Y = 'binary'
epsilon = 0.1

Y = Y.reshape((Y.shape[0],)) # makes it a (n,) array


print(ccm.ccm(X,Y,numFeatures,type_Y,epsilon))
