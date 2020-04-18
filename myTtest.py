import scipy.io
import numpy as np
import pandas as pd
from math import log
from statistics import mean, stdev
from sklearn.model_selection import train_test_split
from skfeature.function.statistical_based import t_score
from sklearn.model_selection import StratifiedShuffleSplit
from jaccard_stability import jaccard_stability




def tTest(X,y,runs,ens,testSize,featureSel, Stratified = False):
    n_samples, n_features = np.shape(X)
    n_labels = np.shape(y)
    sel_features = featureSel
    print(sel_features)



    FeatSel = np.zeros((ens, sel_features))
    Fvotes = np.zeros((1, n_features))
    fea_final = np.zeros((runs, sel_features))
    for run in range(runs):
        for en in range(ens):
            if Stratified:
                sss = StratifiedShuffleSplit(runs,test_size=testSize)
                for train_index, test_index in sss.split(X,y):
                    X_train, X_test = X[train_index], X[test_index]
                    y_train, y_test = y[train_index], y[test_index]
            else:
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testSize) # train test split code
            
            score = t_score.t_score(X_train, y_train)
            # print(score)
            FeatSel[en, :] = score[0:sel_features]
        
        Fvotes = [np.count_nonzero(FeatSel == x) for x in range(n_features)]

        idxs = np.array(Fvotes).argsort()[::-1][:n_features]
        fea_final[run,:] = idxs[0:sel_features]

    # test stability
    JI = jaccard_stability(fea_final)
    np.savetxt('Ttest_fea_final.csv', fea_final, delimiter=',',fmt='%d')
    return ('jaccard=', JI)
    

if __name__ == "__main__":
    features = pd.read_csv(r'resources\wellness_nonverbal_features.csv')
    labels = pd.read_csv(r'resources\wellness_nonverbal_condition_lable.csv')
    X = features.to_numpy()
    y = labels.to_numpy()
    y = y.reshape((y.shape[0],))
    runs = 10
    ens = 100 #folds?
    testSize = 0.2 #this should pull from GUI