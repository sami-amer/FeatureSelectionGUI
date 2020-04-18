import pandas as pd 
import tensorflow as tf
import myTtest
import numpy as np

features = pd.read_csv(r'resources\wellness_nonverbal_features.csv')
labels = pd.read_csv(r'resources\wellness_nonverbal_condition_lable.csv')
X = features.to_numpy()
Y = labels.to_numpy()
Y = Y.reshape((Y.shape[0],)) # makes it a (n,) array

# myTtest.Ttest(X,Y)
